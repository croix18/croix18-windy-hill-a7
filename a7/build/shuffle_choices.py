#!/usr/bin/env python3
"""Spread the keyed answers of a unit's multiple-choice items across the letters.

    python3 shuffle_choices.py u3            → rewrites u3/l*.py and u3/unit.py in place, prints every change

Every spec was written with the keyed answer first (correct=0 — a writing convenience), and the
decks and banks printed the options in spec order, so every single-answer item keyed A and every
select-all keyed the first options. Students noticed (3 Oct 2026). This script permutes each
item's options ONCE, in the source, so the spec stays the single readable truth and letter
references in the teacher prose stay literal:

  - `choices` are reordered; `correct` follows; `errors` is re-keyed; `form_only` is re-lettered;
    an `answer` that names the letter ("A", "A — 4⁵", "A, B, C and D") is regenerated.
  - Letters inside the item's OWN teacher prose (note, note_a, why, wrong, the error texts) are
    remapped where they unambiguously name an option: B–F standing alone, and A when followed by
    is/was/gives/means/and/or/—/:/,  — never the article in "A board full of B".
  - Letters are assigned per file from a seeded shuffle so consecutive items differ and no letter
    takes more than its share; select-alls take a seeded permutation of all positions.
  - Letter references OUTSIDE the item (a Teacher Edition line saying "a board full of B on Q5")
    are listed at the end for the author to fix by hand — they are not touched.

The gate `balancecheck` (lessonbuild / unitbuild) refuses a build whose keyed letters cluster.
"""
import ast, sys, os, re, random, glob

HERE = os.path.dirname(os.path.abspath(__file__))
PROSE = ("note", "note_a", "why", "wrong", "hint", "gloss")
LETTER = re.compile(r"(?<![A-Za-z0-9.\\])([B-F])(?![A-Za-z0-9])"
                    r"|(?<![A-Za-z0-9.\\])(A)(?=\s+(?:is|was|gives|means|and|or|—|–)\b|\s*(?::|,|\)|—|$))")


def remap_text(text, perm_letter):
    """perm_letter: old letter -> new letter. Replaces unambiguous option references."""
    def sub(m):
        L = m.group(1) or m.group(2)
        return perm_letter.get(L, L)
    return LETTER.sub(sub, text)


def seg(src, node):
    return ast.get_source_segment(src, node)


def plan_letters(n_items, n_choices_list, rng):
    """One keyed letter per single-answer item: cycle through shuffled blocks of the alphabet so
    consecutive items differ and the counts stay within one of each other."""
    out, block = [], []
    for k in n_choices_list:
        if not block:
            block = list(range(k)); rng.shuffle(block)
            if out and block[0] == out[-1]:
                block.append(block.pop(0))
        v = block.pop(0)
        out.append(v % k)
    return out


def process(path, rng, report):
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    items = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, "id", None) == "dict":
            kws = {k.arg: k for k in node.keywords}
            if "choices" in kws and "correct" in kws:
                items.append((node, kws))
    items.sort(key=lambda t: (t[0].lineno, t[0].col_offset))
    singles = [(n, k) for n, k in items if not isinstance(k["correct"].value, (ast.List, ast.Tuple))]
    targets = plan_letters(len(singles), [len(k["choices"].value.elts) for n, k in singles], rng)
    target_of = {id(n): t for (n, k), t in zip(singles, targets)}
    edits = []   # (start, end, new_text) as absolute offsets — ast columns count UTF-8 BYTES
    blines = src.encode("utf-8").splitlines(keepends=True)
    offs = [0]
    for ln in blines:
        offs.append(offs[-1] + len(ln))
    def span(node):
        return offs[node.lineno - 1] + node.col_offset, offs[node.end_lineno - 1] + node.end_col_offset

    for node, kws in items:
        choices = kws["choices"].value.elts
        n = len(choices)
        corr_node = kws["correct"].value
        multi = isinstance(corr_node, (ast.List, ast.Tuple))
        old_correct = [c.value for c in corr_node.elts] if multi else [corr_node.value]
        # new order: a permutation `order` where order[new_pos] = old_pos
        if multi:
            order = list(range(n)); rng.shuffle(order)
            # a select-all must not keep the keyed set as a prefix
            tries = 0
            while sorted(i for i, o in enumerate(order) if o in old_correct) == list(range(len(old_correct))) and tries < 50:
                rng.shuffle(order); tries += 1
        else:
            t = target_of[id(node)]
            others = [i for i in range(n) if i != old_correct[0]]
            rng.shuffle(others)
            order = others[:t] + [old_correct[0]] + others[t:]
        new_pos = {o: i for i, o in enumerate(order)}
        perm_letter = {chr(65 + o): chr(65 + i) for o, i in new_pos.items()}
        new_correct = sorted(new_pos[o] for o in old_correct)
        # 1. choices
        ch_src = [seg(src, c) for c in choices]
        s, e = span(kws["choices"].value)
        edits.append((s, e, "[" + ", ".join(ch_src[o] for o in order) + "]"))
        # 2. correct
        s, e = span(corr_node)
        edits.append((s, e, "[" + ", ".join(map(str, new_correct)) + "]" if multi else str(new_correct[0])))
        # 3. errors
        if "errors" in kws and isinstance(kws["errors"].value, ast.Dict):
            d = kws["errors"].value
            pairs = []
            for kn, vn in zip(d.keys, d.values):
                kl = kn.value
                new_k = perm_letter[kl]
                vtxt = seg(src, vn)
                pairs.append((new_k, f'"{new_k}": ' + remap_text(vtxt, perm_letter)))
            pairs.sort()
            s, e = span(d)
            edits.append((s, e, "{" + ", ".join(p[1] for p in pairs) + "}"))
        # 4. form_only
        if "form_only" in kws:
            fo = kws["form_only"].value
            s, e = span(fo)
            edits.append((s, e, '"' + "".join(sorted(perm_letter[c] for c in fo.value)) + '"'))
        # 5. answer
        if "answer" in kws and isinstance(kws["answer"].value, ast.Constant):
            a = kws["answer"].value.value
            letters = [chr(65 + i) for i in new_correct]
            if multi:
                m = re.fullmatch(r"([A-F](?:, [A-F])*) and ([A-F])", a)
                if m:
                    new_a = ", ".join(letters[:-1]) + " and " + letters[-1] if len(letters) > 1 else letters[0]
                else:
                    new_a = remap_text(a, perm_letter)
            else:
                m = re.fullmatch(r"([A-F])( — .*)?", a, re.S)
                if m:
                    new_a = letters[0] + (m.group(2) or "")
                else:
                    new_a = remap_text(a, perm_letter)
            if new_a != a:
                s, e = span(kws["answer"].value)
                q = seg(src, kws["answer"].value)[0]
                edits.append((s, e, q + new_a.replace("\\", "\\\\") + q if "\\" in new_a else q + new_a + q))
        # 6. prose
        for fld in PROSE:
            if fld in kws and isinstance(kws[fld].value, ast.Constant) and isinstance(kws[fld].value.value, str):
                txt = seg(src, kws[fld].value)
                new = remap_text(txt, perm_letter)
                if new != txt:
                    s, e = span(kws[fld].value)
                    edits.append((s, e, new))
                    for m in LETTER.finditer(txt):
                        report.append(f"{os.path.basename(path)}:{node.lineno} {fld}: …{txt[max(0,m.start()-30):m.end()+30]}…  → {perm_letter.get(m.group(1) or m.group(2))}")
        report.append(f"{os.path.basename(path)}:{node.lineno}  keyed {','.join(chr(65+c) for c in old_correct)} → {','.join(chr(65+c) for c in new_correct)}   order {order}")
    # apply edits from the end, on the byte string the offsets were measured on
    b = src.encode("utf-8")
    for s, e, new in sorted(edits, key=lambda x: -x[0]):
        b = b[:s] + new.encode("utf-8") + b[e:]
    open(path, "wb").write(b)
    return len(items)


if __name__ == "__main__":
    unit = sys.argv[1]
    files = sorted(glob.glob(os.path.join(HERE, unit, "l[0-9]*.py"))) + [os.path.join(HERE, unit, "unit.py")]
    report, total = [], 0
    for f in files:
        rng = random.Random(f"{unit}/{os.path.basename(f)}/2026-10-03")
        total += process(f, rng, report)
    print("\n".join(report))
    print(f"\n{total} multiple-choice items permuted in {len(files)} files")
    # letter references outside the items, for the author
    OUT = re.compile(r"\b(?:option|options|full of|shows|picks|chose)\s+([A-F])\b|\b([A-F]) on (?:Q|question|whiteboard|board)")
    for f in files:
        for i, ln in enumerate(open(f, encoding="utf-8"), 1):
            if OUT.search(ln) and "choices=" not in ln and "errors=" not in ln:
                print(f"HAND-CHECK {os.path.basename(f)}:{i}: {ln.strip()[:140]}")
