"""LaTeX spans ($...$) inside prose -> plain Unicode text for a spreadsheet cell.

Handles what the lesson specs use: \\frac, \\sqrt, \\sqrt[3], ^{...}, \\cdot, \\times, \\div,
\\left/\\right, \\le(q), \\ge(q), \\ne(q), \\approx, \\pi, \\text{}. Anything else raises, so a
new command can never slip through as raw LaTeX. Fractions and roots get parentheses unless
their argument is a single number, letter or power, so precedence never changes:
\\frac{a+b}{c} -> (a + b)/c, (\\frac{2}{3})^{3} -> (2/3)³."""
import re

SUP = dict(zip("0123456789+-=()nimxyabkp", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱᵐˣʸᵃᵇᵏᵖ"))
SIMPLE = {r"\cdot": " · ", r"\times": " × ", r"\div": " ÷ ", r"\leq": " ≤ ", r"\le": " ≤ ", r"\geq": " ≥ ",
          r"\ge": " ≥ ", r"\neq": " ≠ ", r"\ne": " ≠ ", r"\approx": " ≈ ", r"\pi": "π", r"\pm": " ± ",
          r"\%": "%", r"\,": " ", r"\;": " ", r"\:": " ", r"\!": "", r"\quad": " ", r"{,}": ","}


def _brace(s, j):
    """s[j] is '{': return (inside, index after the matching '}')."""
    depth = 0
    for k in range(j, len(s)):
        depth += (s[k] == "{") - (s[k] == "}")
        if depth == 0:
            return s[j + 1:k], k + 1
    raise ValueError(f"unbalanced braces in {s!r}")


def _atomic(t):
    """True when t needs no parentheses as a fraction part or root argument."""
    t = t.strip()
    if re.fullmatch(r"−?(\d{1,3}(,\d{3})+|\d+)(\.\d+)?|[A-Za-z]|π", t):
        return True
    if re.fullmatch(r"(\d+(\.\d+)?|[A-Za-z])[⁰¹²³⁴⁵⁶⁷⁸⁹⁻ⁿᵐˣʸᵃᵇᵏᵖ]+", t):
        return True
    if t.startswith("(") and t.endswith(")"):
        depth = 0
        for i, ch in enumerate(t):
            depth += (ch == "(") - (ch == ")")
            if depth == 0 and i < len(t) - 1:
                return False
        return True
    return False


def _wrap(t):
    t = t.strip()
    return t if _atomic(t) else f"({t})"


def math(s):
    """One LaTeX math span -> Unicode."""
    s = s.replace(r"\left", "").replace(r"\right", "").replace(r"\dfrac", r"\frac").replace(r"\tfrac", r"\frac")
    out, i = [], 0
    while i < len(s):
        if s.startswith(r"\frac", i):
            a, j = _brace(s, i + 5); b, j = _brace(s, j)
            f = _wrap(math(a)) + "/" + _wrap(math(b))
            before = "".join(out).rstrip()[-1:]
            after = s[j:].lstrip()[:1]
            if (before and (before.isalnum() or before in ")⁰¹²³⁴⁵⁶⁷⁸⁹ⁿᵐˣʸᵃᵇᵏᵖ")) or (after and (after.isalnum() or after in "(\\")):
                f = "(" + f + ")"          # juxtaposed with a factor: keep the fraction one factor
            out.append(f); i = j
        elif s.startswith(r"\sqrt[3]", i):
            a, j = _brace(s, i + 8); out.append("∛" + _wrap(math(a))); i = j
        elif s.startswith(r"\sqrt", i):
            a, j = _brace(s, i + 5); out.append("√" + _wrap(math(a))); i = j
        elif s.startswith(r"\text", i) or s.startswith(r"\mathrm", i):
            k = s.index("{", i); a, j = _brace(s, k); out.append(a); i = j
        elif s[i] == "^":
            if s[i + 1] == "{":
                a, j = _brace(s, i + 1)
            else:
                a, j = s[i + 1], i + 2
            a = math(a).replace("−", "-")
            out.append("".join(SUP[c] for c in a) if all(c in SUP for c in a) else "^(" + a + ")"); i = j
        elif s[i] == "\\":
            for k, v in sorted(SIMPLE.items(), key=lambda kv: -len(kv[0])):
                if s.startswith(k, i) and not (k[1:].isalpha() and s[i + len(k):i + len(k) + 1].isalpha()):
                    out.append(v); i += len(k); break
            else:
                raise ValueError(f"unhandled LaTeX at {s[i:i + 12]!r} in {s!r}")
        elif s[i] in "{}":
            i += 1                                   # grouping braces
        elif s[i] == "-":
            out.append("−"); i += 1                  # a math minus
        else:
            out.append(s[i]); i += 1
    t = re.sub(r" {2,}", " ", "".join(out)).strip()
    return re.sub(r"\( ", "(", re.sub(r" \)", ")", t))


def text(s):
    """Prose with $...$ spans -> plain text."""
    if s is None:
        return ""
    return re.sub(r"\$([^$]*)\$", lambda m: math(m.group(1)), s)
