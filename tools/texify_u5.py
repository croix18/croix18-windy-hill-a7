"""One-off (18 Oct): typeset Unit 5's mathematics in $…$ — Croix: "Can you rewrite the math to be
in latex?" Student-facing strings only (stems, board rows, prompts, asks, choices, hints, glosses,
headings, the target/essential lines, vocabulary definitions). Equations, fractions, ratios and
units with exponents become LaTeX; a bare quantity in prose ("a 4 cm side") stays text; existing
$…$ segments are left alone. Usage: python3 tools/texify_u5.py a7/build/u5/l01.py …"""
import re, sys, tokenize, io, ast

KEYS = {"stem", "text", "qtext", "prompt", "ask", "choices", "hint", "gloss", "heading",
        "target", "essential", "yesterday", "today", "vocab"}

FRAC = {"½": (1, 2), "¼": (1, 4), "¾": (3, 4), "⅓": (1, 3), "⅔": (2, 3), "⅕": (1, 5), "⅖": (2, 5),
        "⅗": (3, 5), "⅘": (4, 5), "⅙": (1, 6), "⅚": (5, 6), "⅛": (1, 8), "⅜": (3, 8), "⅝": (5, 8),
        "⅞": (7, 8), "⅑": (1, 9)}
SUP = {"²": "2", "³": "3"}
UNITS = ["US dollars", "US dollar", "Canadian dollars", "Canadian dollar", "dollars", "dollar",
         "fl oz", "mi/h", "km/h", "sq ft", "cups", "cup", "euros", "euro", "pesos", "CAD", "gal", "lb", "kg", "oz",
         "mL", "cm", "mm", "km", "mi", "in", "ft", "yd", "m", "L", "c", "g", "h", "min", "s", "tanks", "servings",
         "parts", "recipes"]
UNIT_RE = "(?:" + "|".join(re.escape(u) for u in sorted(UNITS, key=len, reverse=True)) + ")[²³]?"
FR = "[½¼¾⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅑]"
NUM = rf"(?:\d{{1,3}}(?:,\d{{3}})+(?:\.\d+)?|\d+(?:\.\d+)?{FR}?|{FR})"
MONEY = rf"\x01{NUM}"
QTY = rf"(?:{MONEY}|{NUM}(?:\s?{UNIT_RE})?|k²|k|P|A)"
OP = r"\s*[=×÷+−]\s*|\s-\s"
# an expression: quantities joined by = × ÷ + −, at least one operator
EXPR = re.compile(rf"(?<![\w$\\]){QTY}(?:(?:{OP}){QTY})+(?![\w$])")
# a ratio with colons: "¼ in : 1 ft", "1 : 50", "2 : 4 : 5", "1 cm : 50 km" (spaces round the colon — "Nov 5:" is not one)
RATIO = re.compile(rf"(?<![\w$\\]){QTY}(?:\s:\s{QTY})+(?![\w$])")
# a lone unit with an exponent: "20 ft²", "ft²", "in³"
SQ = re.compile(rf"(?<![\w$\\])(?:{NUM}\s?)?(?:ft|in|m|cm|yd|mi|km)[²³](?![\w$])")
# a lone mixed/unicode fraction with an optional number: "3¾ cups", "¼ in" is caught by RATIO/EXPR or here
UF = re.compile(r"(?<![\w$\\])\d*[½¼¾⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅑](?![\w$])")
LONE_K = re.compile(r"(?<![\w$\\])k(?=[\s.,;:?)]|$)")


def tex_qty(q):
    q = q.strip()
    if q in ("k", "P", "A"):
        return q
    if q == "k²":
        return "k^{2}"
    if q.startswith("\x01"):
        return "\\$" + q[1:].replace(",", "{,}")
    m = re.match(rf"^({NUM})\s?({UNIT_RE})?$", q)
    if not m:
        return q
    n, u = m.group(1), m.group(2)
    # mixed / unicode fraction
    for ch, (a, b) in FRAC.items():
        if ch in n:
            n = n.replace(ch, rf"\frac{{{a}}}{{{b}}}")
    n = n.replace(",", "{,}")
    if u:
        sup = ""
        if u[-1] in SUP:
            sup = "^{" + SUP[u[-1]] + "}"; u = u[:-1]
        return rf"{n}\,\text{{{u}}}{sup}"
    return n


def tex_expr(s):
    parts = re.split(r"(\s*[=×÷+−]\s*|\s-\s|\s:\s)", s)
    out = []
    for p in parts:
        t = p.strip()
        if t == "=": out.append(" = ")
        elif t == "×": out.append(r" \times ")
        elif t == "÷": out.append(r" \div ")
        elif t == "+": out.append(" + ")
        elif t in ("−", "-"): out.append(" - ")
        elif t == ":": out.append(" : ")
        elif t == "": continue
        else: out.append(tex_qty(t))
    return "$" + "".join(out).strip() + "$"


def texify(s):
    # leave existing $…$ alone (\$ is money, not a delimiter)
    s = s.replace("\\$", "\x01")
    segs = re.split(r"(\$[^$]*\$)", s)
    for i, seg in enumerate(segs):
        if seg.startswith("$"):
            continue
        seg = EXPR.sub(lambda m: tex_expr(m.group(0)), seg)
        seg = RATIO.sub(lambda m: tex_expr(m.group(0)), seg)
        seg = SQ.sub(lambda m: tex_expr(m.group(0)), seg)
        seg = UF.sub(lambda m: tex_expr(m.group(0)), seg)
        seg = LONE_K.sub("$k$", seg)
        segs[i] = seg
    return "".join(segs).replace("\x01", "\\$")


def transform_source(src):
    toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    out = []; key = None; pos = (1, 0); lines = src.splitlines(keepends=True)
    def text_between(a, b):
        (r1, c1), (r2, c2) = a, b
        if r1 == r2: return lines[r1 - 1][c1:c2]
        return lines[r1 - 1][c1:] + "".join(lines[r1:r2 - 1]) + lines[r2 - 1][:c2]
    for i, t in enumerate(toks):
        if t.type == tokenize.NAME and i + 1 < len(toks) and toks[i + 1].string == "=" and toks[i + 1].type == tokenize.OP:
            key = t.string
        if t.type == tokenize.STRING and key in KEYS and t.string[0] in "'\"":
            q = t.string[0]
            if t.string[-1] == q and not t.string.startswith(('"""', "'''")):
                try:
                    val = ast.literal_eval(t.string)
                except Exception:
                    val = None
                if isinstance(val, str):
                    new = texify(val).replace("\\", "\\\\").replace(q, "\\" + q)
                    out.append(text_between(pos, t.start)); out.append(q + new + q); pos = t.end
                    continue
    out.append(src[sum(len(l) for l in lines[:pos[0] - 1]) + pos[1]:])
    return "".join(out)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        src = open(p, encoding="utf-8").read()
        new = transform_source(src)
        open(p, "w", encoding="utf-8").write(new)
        print(p, "ok" if new != src else "unchanged")


PLAIN_KEYS = {"target", "essential", "yesterday", "today"}     # plain text boxes on the title slide: no $…$


def detex(s):
    """$…$ back to readable plain text, for the title slide's boxes."""
    def one(m):
        t = m.group(1)
        t = re.sub(r"(\d)\\frac\{(\d+)\}\{(\d+)\}", lambda k: k.group(1) + {("1","2"):"½",("1","4"):"¼",("3","4"):"¾",("1","3"):"⅓",("2","3"):"⅔"}.get((k.group(2),k.group(3)), f" {k.group(2)}/{k.group(3)}"), t)
        t = re.sub(r"\\frac\{(\d+)\}\{(\d+)\}", lambda k: {("1","2"):"½",("1","4"):"¼",("3","4"):"¾",("1","3"):"⅓",("2","3"):"⅔"}.get((k.group(1),k.group(2)), f"{k.group(1)}/{k.group(2)}"), t)
        t = re.sub(r"\\text\{([^}]*)\}", r"\1", t)
        t = t.replace("\\ ", " ").replace("^{2}", "²").replace("^{3}", "³").replace(" \\times ", " × ").replace(" \\div ", " ÷ ").replace("{,}", ",").replace("\\$", "$")
        return re.sub(r"\s+", " ", t).strip()
    return re.sub(r"\$([^$]+)\$", one, s)


def detex_source(src):
    toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    out = []; key = None; pos = (1, 0); lines = src.splitlines(keepends=True)
    def text_between(a, b):
        (r1, c1), (r2, c2) = a, b
        if r1 == r2: return lines[r1 - 1][c1:c2]
        return lines[r1 - 1][c1:] + "".join(lines[r1:r2 - 1]) + lines[r2 - 1][:c2]
    for i, t in enumerate(toks):
        if t.type == tokenize.NAME and i + 1 < len(toks) and toks[i + 1].string == "=" and toks[i + 1].type == tokenize.OP:
            key = t.string
        if t.type == tokenize.STRING and key in PLAIN_KEYS and t.string[0] in "'\"":
            q = t.string[0]
            try:
                val = ast.literal_eval(t.string)
            except Exception:
                val = None
            if isinstance(val, str) and "$" in val:
                new = detex(val).replace("\\", "\\\\").replace(q, "\\" + q)
                out.append(text_between(pos, t.start)); out.append(q + new + q); pos = t.end
    out.append(src[sum(len(l) for l in lines[:pos[0] - 1]) + pos[1]:])
    return "".join(out)


SPLIT_KEYS = {"prompt", "text"}     # slide rows are one line each: a long sentence pair with math becomes two rows


def split_rows(src):
    """In prompt=[…] and text=[…] lists, a row over ~72 characters that carries $…$ and more than one
    sentence is split at its sentence boundaries into separate rows."""
    toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    out = []; key = None; pos = (1, 0); lines = src.splitlines(keepends=True)
    def text_between(a, b):
        (r1, c1), (r2, c2) = a, b
        if r1 == r2: return lines[r1 - 1][c1:c2]
        return lines[r1 - 1][c1:] + "".join(lines[r1:r2 - 1]) + lines[r2 - 1][:c2]
    for i, t in enumerate(toks):
        if t.type == tokenize.NAME and i + 1 < len(toks) and toks[i + 1].string == "=" and toks[i + 1].type == tokenize.OP:
            key = t.string
        if t.type == tokenize.STRING and key in SPLIT_KEYS and t.string[0] in "'\"":
            q = t.string[0]
            try:
                val = ast.literal_eval(t.string)
            except Exception:
                val = None
            if isinstance(val, str) and "$" in val and len(val) > 72 and not val.startswith("**"):
                sents = re.split(r"(?<=[.;?])\s+(?=[A-Z0-9$\\])", val)
                if len(sents) > 1:
                    enc = lambda x: q + x.replace("\\", "\\\\").replace(q, "\\" + q) + q
                    out.append(text_between(pos, t.start)); out.append(", ".join(enc(x) for x in sents)); pos = t.end
    out.append(src[sum(len(l) for l in lines[:pos[0] - 1]) + pos[1]:])
    return "".join(out)
