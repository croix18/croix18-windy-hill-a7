#!/usr/bin/env python3
"""A7 Unit 5 practice: the independent check.   python3 verify.py → exits 1 on any problem.

Everything here is read from what a student sees (dump.json, written by u5_check.js: the printed stems, parts, choices,
worked lines and Hint questions) and from the unit's own specs — never from the page's engine:
- every question read again with this file's reader and its key worked out again in exact arithmetic (sympy): the scale
  factors, the perimeters and areas, the plan's real lengths and areas, the conversions and the chain, the closest square
  unit, the money, the tanks, the recipe, the mixture, the select-alls and the faster of two speeds;
- every worked line's value is the key; every Hint question "What is …?" is worth its answer, and the Hint ends on the key;
  no modelled mistake is the key; no part (b) Hint asks for part (a)'s number;
- every conversion ratio printed is a line of the FAST reference sheet as the unit's reference sheet prints it;
- Form A and Form B: their keys are read from a7/build/u5/unit.py with the same reader, test_forms.js must hold exactly
  those, and no question on the page is one of them; nor is a question of the practice test or the review that go home;
- ruling 43: no question on the page uses the numbers of something a lesson showed — read from the lesson specs
  (a7/build/u5/l*.py: warm-ups, notes, worked examples, Your Turns, their check tuples) and the reference sheet, matched by
  kind of question — a check of its own, not the engine's list;
- the page's fixed text (its notes and messages) holds no number that is a test answer."""
import json, os, re, sys, importlib.util
from sympy import Rational as R, ceiling, sqrt, Integer, sympify

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "..", "..", "build", "u5")
probs = []
def bad(msg):
    if len(probs) < 60: probs.append(msg)
    probs.append(None)

def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

# ------------------------------------------------------------------ TeX and the page's text, as plain words and numbers
def tex_plain(s):
    s = str(s)
    s = re.sub(r"\$([^$]*)\$", lambda m: m.group(1), s.replace("\\$", "＄"))
    s = re.sub(r"(\d)\\frac\{(\d+)\}\{(\d+)\}", r"\1 \2/\3", s)
    s = re.sub(r"\\frac\{(\d+)\}\{(\d+)\}", r"\1/\2", s)
    s = re.sub(r"\\text\{([^}]*)\}", r"\1", s)
    s = s.replace("\\,", " ").replace("\\;", " ").replace("\\times", "×").replace("\\div", "÷").replace("\\rightarrow", "→").replace("\\cdot", "·")
    s = re.sub(r"\^\{(\d)\}", r"^\1", s).replace("{,}", ",").replace("＄", "$").replace("\\%", "%").replace("²", "^2").replace("³", "^3")
    s = re.sub(r"\\[A-Za-z]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def num(s):
    s = str(s).strip().replace(",", "")
    m = re.match(r"^(\d+) (\d+)/(\d+)$", s)
    if m: return Integer(m.group(1)) + R(int(m.group(2)), int(m.group(3)))
    m = re.match(r"^(\d+)/(\d+)$", s)
    if m: return R(int(m.group(1)), int(m.group(2)))
    return R(s)

def frac(s):
    n, d = s.split("/"); return R(int(n), int(d))

NUMRE = r"\d[\d,]*(?:\.\d+)?(?: \d+/\d+)?|\d+/\d+"
def ks(q):                                           # a number in a key, as test_forms.js writes it
    q = R(q)
    if q.q == 1: return str(q.p)
    s = format(float(q), ".10f").rstrip("0").rstrip(".")
    assert R(s) == q, q
    return s
def kfrac(q):
    q = R(q); return str(q.p) if q.q == 1 else "%d/%d" % (q.p, q.q)

UNIT_OF = {"inches": "in", "centimeters": "cm", "pounds": "lb", "kilograms": "kg", "gallons": "gal", "liters": "L", "miles": "mi", "kilometers": "km",
           "feet": "ft", "meters": "m", "cups": "c", "ounces": "oz", "grams": "g"}
def scale(s):
    m = re.match(r"^1 in : (\d+) ft$", s)
    if m: return Integer(m.group(1))
    m = re.match(r"^1/(\d+) in : (\d+) ft$", s)
    if m: return Integer(m.group(1)) * Integer(m.group(2))
    return None

# ------------------------------------------------------------------ the reader: a question's keys, and its answer
def read(qn, st, P, opts):
    """st: the stem; P: the parts' stems; opts: the choices. → (keys, answers, correct). Raises on a question it cannot read."""
    keys, ans, correct = [], [], None
    def need(m, what):
        if not m: raise ValueError("cannot read %s: %s | %s" % (what, st, " | ".join(P)))
        return m
    if qn in (1, 2):
        m = need(re.match(r"^A (\d+) (cm|m|ft) side of a figure is (\d+) \2 in its scale copy\. Find the scale factor\.$", st), "the sides")
        a, b = int(m.group(1)), int(m.group(3)); keys.append(("sf", "%d>%d" % (a, b))); ans.append(R(b, a))
    elif qn == 3:
        m = need(re.match(r"^A figure is scaled by a scale factor of ([\d.]+)\. Select ALL of the statements that are true about the copy\.$", st), "k")
        k = R(m.group(1)); keys.append(("sel3", ks(k))); correct = []
        for i, o in enumerate(opts):
            x = re.match(r"^(Each side|The perimeter) is ([\d.]+) times as long\.$", o); y = re.match(r"^The area is ([\d.]+) times as large\.$", o)
            if x: ok = R(x.group(2)) == k
            elif y: ok = R(y.group(1)) == k * k
            elif re.match(r"^Each angle is ([\d.]+) times as large\.$", o): ok = False
            else: raise ValueError("a statement I cannot read: " + o)
            if ok: correct.append(i)
    elif qn == 4:
        m = need(re.match(r"^A (\d+) (cm|in|ft|m) by (\d+) \2 rectangle is scaled by k = ([\d.]+)\.$", st), "the rectangle")
        w, h, k = int(m.group(1)), int(m.group(3)), R(m.group(4))
        keys += [("rect", "%d,%d|%s" % (min(w, h), max(w, h), ks(k))), ("rectWH", "%d,%d" % (min(w, h), max(w, h)))]
        ans += [2 * (w + h) * k, w * h * k * k]
    elif qn == 5:
        m = need(re.match(r"^A figure has area ([\d,]+) (cm|in|ft|m)\^2\. Its scale copy has area ([\d,]+) \2\^2\. What is the scale factor\?$", st), "the areas")
        A, B = num(m.group(1)), num(m.group(3)); k = sqrt(B / A)
        if not k.is_Rational: raise ValueError("the area ratio is not a square")
        keys.append(("areaK", "%s>%s" % (A, B))); ans.append(k)
    elif qn == 6:
        m = need(re.match(r"^A floor plan is drawn at (.+?)\. A room is ([\d.]+) in by ([\d.]+) in on the plan\.$", st), "the plan")
        r, p, q = need(scale(m.group(1)), "the scale"), R(m.group(2)), R(m.group(3))
        need(re.match(r"^Find the real length of the wall drawn %s in long\.$" % re.escape(m.group(2)), P[0]) and P[1] in ("Find the room’s real area.", "Find the room's real area."), "the parts")
        keys += [("room", "%s|%s,%s" % (ks(r), ks(min(p, q)), ks(max(p, q)))), ("wall", "%s|%s" % (ks(r), ks(p)))]
        ans += [p * r, p * r * q * r]
    elif qn == 7:
        m = need(re.match(r"^A plan is drawn at (.+?)\. A real wall is (\d+) ft long\. How long is it on the plan\?$", st), "the wall")
        r, L = need(scale(m.group(1)), "the scale"), int(m.group(2)); keys.append(("plan", "%s|%d" % (ks(r), L))); ans.append(R(L) / r)
    elif qn == 8:
        m = need(re.match(r"^A plan is drawn at 1 in : (\d+) ft\. A room is ([\d.]+) in by ([\d.]+) in on the plan\.(?: 1 ft = 0\.305 m\.)? Find the room[’']s real area(?: in square meters)?\.$", st), "the room")
        r, p, q = Integer(m.group(1)), R(m.group(2)), R(m.group(3)); keys.append(("room", "%s|%s,%s" % (ks(r), ks(min(p, q)), ks(max(p, q))))); ans.append(p * r * q * r)
        if "square meters" in st: keys.append(("amount", "ft2|" + ks(p * r * q * r)))   # the transfer item's area in ft², an amount the page's Q14 could print
    elif qn == 9:
        m = need(re.match(r"^1 in = 2\.54 cm\. How many centimeters is (\d+) in\?$", st), "the inches")
        keys.append(("conv", "in>cm|" + m.group(1))); keys.append(("amount", "in/cm|" + m.group(1))); ans.append(int(m.group(1)) * R("2.54"))
    elif qn == 10:
        m = need(re.match(r"^1 (\w+) = ([\d.]+) (\w+) and 1 \3 = ([\d.]+) \1\. Select ALL of the expressions that give the number of (\w+) in (\d+) (\w+)\.$", st), "the ratios")
        one = {m.group(1): m.group(2), m.group(3): m.group(4)}; to = UNIT_OF[m.group(5)]; n = int(m.group(6)); frm = m.group(7)
        need({frm, to} == {m.group(1), m.group(3)}, "the units"); keys.append(("conv", "%s>%s|%d" % (frm, to, n))); correct = []
        keys.append(("amount", "%s|%d" % (PAIR_OF[frm], n)))
        for i, o in enumerate(opts):
            x = need(re.match(r"^(\d+) (×|÷) ([\d.]+)$", o), "a choice"); u1 = [u for u in one if one[u] == x.group(3)]
            need(int(x.group(1)) == n and len(u1) == 1, "a choice's ratio")
            if (x.group(2) == "×" and u1[0] == frm) or (x.group(2) == "÷" and u1[0] == to): correct.append(i)
    elif qn == 11:
        m = need(re.match(r"^1 yd = 3 ft, 1 ft = 12 in, 1 in = 2\.54 cm\. How many centimeters is ([\d.]+) yd\?$", st), "the yards")
        n = R(m.group(1)); keys.append(("chain", "yd>cm|" + ks(n))); keys.append(("amount", "in/cm|" + ks(n * 36))); ans.append(n * 36 * R("2.54"))
    elif qn == 12:
        m = re.match(r"^1 kg = 2\.204 lb\. How many pounds is (\d+) kg\?$", st)
        if m: keys.append(("conv", "kg>lb|" + m.group(1))); ans.append(int(m.group(1)) * R("2.204"))
        else:
            m = need(re.match(r"^1 lb = 0\.454 kg\. How many kilograms is (\d+) lb\?$", st), "the mass"); keys.append(("conv", "lb>kg|" + m.group(1))); ans.append(int(m.group(1)) * R("0.454"))
        keys.append(("amount", "lb/kg|" + m.group(1)))
    elif qn == 13:
        m = need(re.match(r"^1 gal = 3\.785 L\. How many liters is (\d+) gal\?$", st), "the gallons")
        keys.append(("conv", "gal>L|" + m.group(1))); keys.append(("amount", "gal/L|" + m.group(1))); ans.append(int(m.group(1)) * R("3.785"))
    elif qn == 14:
        m = need(re.match(r"^1 (in|ft|m|cm|mi|km) = ([\d.]+) (in|ft|m|cm|mi|km)\. An? ([a-z ]+) is ([\d,]+) \1\^2 in area\. Which is closest to its area in square (\w+)\?$", st), "the area")
        need(UNIT_OF[m.group(6)] == m.group(3), "the unit asked"); A, r = num(m.group(5)), R(m.group(2)); keys.append(("sqconv", "%s2>%s2|%s" % (m.group(1), m.group(3), A))); keys.append(("amount", "%s2|%s" % (m.group(1), A)))
        if opts:
            vals = [num(need(re.match(r"^([\d,.]+) %s\^2$" % m.group(3), o), "a choice").group(1)) for o in opts]
            OTHER = {"in": "0.39", "cm": "2.54", "ft": "3.28", "m": "0.305", "mi": "0.62", "km": "1.61"}
            exact, alt = A * r * r, A / R(OTHER[m.group(1)]) ** 2
            best = lambda x: min(range(len(vals)), key=lambda i: abs(vals[i] - x))
            correct = best(exact)
            if best(alt) != correct: raise ValueError("the sheet's two routes pick different choices")
    elif qn == 15:
        m = need(re.match(r"^Rate on Nov \d+: 1 US dollar = ([\d.,]+) ([A-Za-z ]+)\.$", st), "the rate"); r, cur = num(m.group(1)), m.group(2)
        a = need(re.match(r"^How many %s is \$(\d+)\?$" % cur, P[0]), "part a"); b = need(re.match(r"^How many US dollars is ([\d.,]+) %s\?$" % cur, P[1]), "part b")
        d, c = int(a.group(1)), num(b.group(1)); keys += [("curA", "%s|%d" % (ks(r), d)), ("curB", "%s|%s" % (ks(r), ks(c)))]; ans += [d * r, c / r]
    elif qn == 16:
        m = need(re.match(r"^A ([a-z ]+) gets (\d+) miles per gallon and its tank holds (\d+) gal\.$", st), "the car")
        mm, g = int(m.group(2)), int(m.group(3)); b = need(re.match(r"^It makes a ([\d,]+)-mi trip\. How many tanks of gas does the trip use\? \(Part of a tank counts as a whole tank\.\)$", P[1]), "part b")
        D = num(b.group(1)); keys += [("tank", "%d|%d" % (mm, g)), ("trip", "%d|%d|%s" % (mm, g, D)), ("range", str(mm * g)), ("tripD", str(D))]; ans += [Integer(mm * g), ceiling(D / (mm * g))]
    elif qn == 17:
        m = need(re.match(r"^A recipe for (\d+) servings uses (%s) cups of (\w+)\.$" % NUMRE, st), "the recipe"); s, c, food = int(m.group(1)), num(m.group(2)), m.group(3)
        a = need(re.match(r"^How much %s for (\d+) servings\?$" % food, P[0]), "part a"); b = need(re.match(r"^With (%s) cups on hand, how many servings can be made\?$" % NUMRE, P[1]), "part b")
        t, h = int(a.group(1)), num(b.group(1)); keys += [("recA", "%d|%s|%d" % (s, kfrac(c), t)), ("recB", "%d|%s|%s" % (s, kfrac(c), kfrac(h))), ("recK", "%s|%s" % (ks(R(t, s)), kfrac(c)))]
        ans += [c * t / s, h / c * s]
    elif qn == 18:
        m = re.match(r"^Paint is mixed (\d+) : (\d+) : (\d+)\. A batch uses (\d+) gal of the (first|second|third) color\. How many gallons is the whole batch\?$", st)
        if m: parts, which, n = [int(m.group(i)) for i in (1, 2, 3)], ["first", "second", "third"].index(m.group(5)), int(m.group(4))
        else:
            m = need(re.match(r"^(\w+) is mixed ([a-z ]+) : ([a-z ]+) : ([a-z ]+) = (\d+) : (\d+) : (\d+)\. A batch uses (\d+) (\w+) of ([a-z ]+)\. How many \9 is the whole batch\?$", st), "the mixture")
            parts, n = [int(m.group(i)) for i in (5, 6, 7)], int(m.group(8)); which = [m.group(2), m.group(3), m.group(4)].index(m.group(10))
        keys.append(("mix", "%s|%d|%d" % (":".join(map(str, sorted(parts))), parts[which], n))); ans.append(R(n, parts[which]) * sum(parts))
    elif qn == 19:
        m = re.match(r"^1 mi = 1\.61 km\. A (\w+) does (\d+) km/h; a (\w+) does (\d+) mi/h\. Which is faster\?", st)
        if m: kmh, mph, A, B = int(m.group(2)), int(m.group(4)), m.group(1), m.group(3)
        else:                                       # the forms' transfer item: a drive, two cars or trucks, two speeds
            m = need(re.match(r"^1 mi = 1\.61 km\. A drive is (\d+) km long\. (\w+) A averages (\d+) mi/h; \w+ B averages (\d+) km/h\.", st), "the speeds")
            kmh, mph = int(m.group(4)), int(m.group(3)); A = B = None
        keys.append(("speed", "%d|%d" % (kmh, mph))); keys.append(("speedM", str(mph)))
        if A and "Type its name" in st:              # the page: the faster one's name and the mi/h speed in km/h
            conv = mph * R("1.61"); ans.append(conv)
        if opts:
            conv = mph * R("1.61"); fast = A if conv < kmh else B; correct = []
            for i, o in enumerate(opts):
                x = re.match(r"^The (\w+): (\d+) mi/h = ([\d.]+) km/h, and ([\d.]+) > ([\d.]+)\.$", o)
                if x and int(x.group(2)) == mph and R(x.group(3)) == conv and x.group(1) == fast and {R(x.group(4)), R(x.group(5))} == {R(kmh), conv} and R(x.group(4)) > R(x.group(5)):
                    correct.append(i)
            if len(correct) != 1: raise ValueError("%d right choices" % len(correct))
            correct = correct[0]
    else:
        raise ValueError("no question %d" % qn)
    return keys, ans, correct

# ------------------------------------------------------------------ the test's three forms and the review, from unit.py
U = load(os.path.join(BUILD, "unit.py")).U
def form_items(secs):
    out, qn = [], 0
    for sec in secs:
        for it in sec["items"]:
            qn += 1
            out.append((qn, tex_plain(it.get("stem", "")), [tex_plain(p.get("stem", "")) for p in it.get("parts", [])], [tex_plain(c) for c in it.get("choices", [])], it))
    return out
PAIR_OF = {"in": "in/cm", "cm": "in/cm", "mi": "mi/km", "km": "mi/km", "lb": "lb/kg", "kg": "lb/kg", "gal": "gal/L", "L": "gal/L", "ft": "ft/m", "m": "ft/m", "c": "c/L", "oz": "oz/g", "g": "oz/g"}
FORM_KEYS = {}
for f in ("A", "B", "practice"):
    FORM_KEYS[f] = set()
    for qn, st, P, opts, it in form_items(U["assessment"]["forms"][f]):
        try:
            keys, ans, correct = read(qn, st, P, opts)
        except ValueError as e:
            bad("Form %s question %d: %s" % (f, qn, e)); continue
        FORM_KEYS[f].update(keys)
        if it.get("transfer"): continue
        # the forms' own answers agree with this reader: a test question worked out differently here is a problem in one or the other
        if correct is not None:
            got = [ "ABCDE".index(x) for x in re.findall(r"\b([A-E])\b", tex_plain(it.get("answer", ""))) ]
            want = sorted(correct) if isinstance(correct, list) else [correct]
            if sorted(got) != want: bad("Form %s question %d: its key %s, worked out here %s" % (f, qn, it.get("answer"), want))
        for a_, v in zip([p.get("answer", "") for p in it.get("parts", [])] or [it.get("answer", "")], ans):
            t = tex_plain(a_).replace("$", "").replace("¾", " 3/4").replace("½", " 1/2").replace("¼", " 1/4")
            m = re.search(NUMRE, re.sub(r"^\s*(?:k =|About)\s*", "", t))
            if not m or num(m.group(0).strip()) != v: bad("Form %s question %d: its key %s, worked out here %s" % (f, qn, a_, v))
# test_forms.js holds exactly Form A's and Form B's keys
src = open(os.path.join(HERE, "test_forms.js"), encoding="utf-8").read()
TF = {}
for f in ("A", "B"):
    m = re.search(r"\b%s: \{(.*?)\}" % f, src, re.S)
    TF[f] = set((s, k) for s, body in re.findall(r"(\w+): \[([^\]]*)\]", m.group(1)) for k in re.findall(r"'([^']*)'", body))
    rk = set(FORM_KEYS[f])
    if rk != TF[f]:
        bad("test_forms.js Form %s is not the form: only in the file %s; only in the form %s" % (f, sorted(TF[f] - rk)[:6], sorted(rk - TF[f])[:6]))
TEST = FORM_KEYS["A"] | FORM_KEYS["B"]
# the review that goes home (3 Nov): its questions in the page's slots, read with their own patterns
REVIEW = set()
for sec in U["review"]:
    for it in sec["items"]:
        st = tex_plain(it.get("stem", "")); P = [tex_plain(p.get("stem", "")) for p in it.get("parts", [])]
        for pat, f in [
            (r"^A (\d+) cm side of a figure is (\d+) cm in its scale copy", lambda m: [("sf", "%s>%s" % (m.group(1), m.group(2)))]),
            (r"^A scale copy is made at k = ([\d.]+)\. A side of the original is (\d+) cm", lambda m: [("sf", "%s>%s" % (m.group(2), ks(R(m.group(2)) * R(m.group(1)))))]),
            (r"area (\d+) cm\^2 and its scale copy has area (\d+) cm\^2", lambda m: [("areaK", "%s>%s" % (m.group(1), m.group(2)))]),
            (r"^A (\d+) cm by (\d+) cm rectangle is scaled by k = (\d+/\d+|[\d.]+)", lambda m: [("rect", "%d,%d|%s" % (min(int(m.group(1)), int(m.group(2))), max(int(m.group(1)), int(m.group(2))), ks(num(m.group(3)))))]),
            (r"^A plan is drawn at (.+?)\. A real wall is (\d+) ft long", lambda m: [("plan", "%s|%s" % (ks(scale(m.group(1))), m.group(2)))]),
            (r"^A plan is drawn at (.+?)\. A wall is ([\d.]+) in long on it", lambda m: [("wall", "%s|%s" % (ks(scale(m.group(1))), m.group(2)))]),
            (r"floor plan drawn at (.+?), on which a room is ([\d.]+) in by ([\d.]+) in", lambda m: [("room", "%s|%s,%s" % (ks(scale(m.group(1))), ks(min(R(m.group(2)), R(m.group(3)))), ks(max(R(m.group(2)), R(m.group(3)))))), ("wall", "%s|%s" % (ks(scale(m.group(1))), m.group(2)))]),
            (r"^1 (\w+) = ([\d.]+) (\w+)\. How many (\w+) is (\d+) (\w+)\?", lambda m: [("conv", "%s>%s|%s" % (m.group(6), m.group(3), m.group(5)))]),
            (r"How many centimeters is (\d+) yd\?", lambda m: [("chain", "yd>cm|" + m.group(1))]),
            (r"^1 ft = 0\.305 m\. How many square meters is ([\d.]+) ft\^2", lambda m: [("sqconv", "ft2>m2|" + m.group(1))]),
            (r"^1 m = 3\.28 ft\. A \w+ is ([\d.]+) m\^2 in area", lambda m: [("sqconv", "m2>ft2|" + m.group(1))]),
            (r"converts (\d+) cm to inches", lambda m: [("conv", "cm>in|" + m.group(1))]),
            (r"^A car gets (\d+) miles per gallon and its tank holds (\d+) gal", lambda m: [("tank", "%s|%s" % (m.group(1), m.group(2)))]),
            (r"A train does (\d+) km/h; a bus does (\d+) mi/h", lambda m: [("speed", "%s|%s" % (m.group(1), m.group(2)))]),
            (r"^Paint is mixed (\d+) : (\d+) : (\d+)\. A batch uses (\d+) gal of the (first|second|third) color", lambda m: [("mix", "%s|%s|%s" % (":".join(map(str, sorted(int(m.group(i)) for i in (1, 2, 3)))), m.group(1 + ["first", "second", "third"].index(m.group(5))), m.group(4)))]),
        ]:
            m = re.search(pat, st)
            if m: REVIEW.update(f(m))
        m = re.match(r"^Rate on Nov \d+: 1 US dollar = ([\d.]+) (\w+)\.$", st)
        if m:
            a = re.match(r"^How many \w+ is \$(\d+)\?$", P[0]); b = re.match(r"^How many US dollars is (\d+) \w+\?$", P[1])
            REVIEW.update([("curA", "%s|%s" % (m.group(1), a.group(1))), ("curB", "%s|%s" % (m.group(1), b.group(1)))])
        m = re.match(r"^A recipe for (\d+) servings uses (%s) cups of \w+\.$" % NUMRE, st)
        if m:
            t = re.match(r"^How much \w+ for (\d+) servings\?$", P[0]); h = re.match(r"^With (%s) cups on hand" % NUMRE, P[1])
            REVIEW.update([("recA", "%s|%s|%s" % (m.group(1), kfrac(num(m.group(2))), t.group(1))), ("recB", "%s|%s|%s" % (m.group(1), kfrac(num(m.group(2))), kfrac(num(h.group(1)))))])
        m = re.match(r"^A car gets (\d+) miles per gallon and its tank holds (\d+) gal", st)
        if m and P:
            d = re.search(r"an? ([\d,]+)-mi trip", P[1]); REVIEW.add(("trip", "%s|%s|%s" % (m.group(1), m.group(2), num(d.group(1)))))
HOME = FORM_KEYS["practice"] | REVIEW

# ------------------------------------------------------------------ ruling 43: what the lessons showed, read as the page's keys
RAT2DIR = {"2.54": "in>cm", "0.39": "cm>in", "0.454": "lb>kg", "2.204": "kg>lb", "3.785": "gal>L", "0.264": "L>gal", "1.61": "mi>km", "0.62": "km>mi",
           "0.305": "ft>m", "3.28": "m>ft", "0.24": "c>L", "4.23": "L>c", "28.35": "oz>g", "0.0352": "g>oz"}
INV = {"in>cm": "cm>in", "cm>in": "in>cm", "lb>kg": "kg>lb", "kg>lb": "lb>kg", "gal>L": "L>gal", "L>gal": "gal>L", "mi>km": "km>mi", "km>mi": "mi>km",
       "ft>m": "m>ft", "m>ft": "ft>m", "c>L": "L>c", "L>c": "c>L", "oz>g": "g>oz", "g>oz": "oz>g"}
RATS = "|".join(re.escape(k) for k in sorted(RAT2DIR, key=len, reverse=True))
MIX = r"\d+ \d+/\d+|\d+/\d+|\d+(?:\.\d+)?"
def texts(x):
    if isinstance(x, str): return [x]
    if isinstance(x, dict): return [t for k, v in x.items() if k not in ("check", "yt_check", "fig") for t in texts(v)]
    if isinstance(x, (list, tuple)): return [t for v in x for t in texts(v)]
    return []
def check_fracs(chk):
    """the F(b, a) of a check tuple, as (a, b): a scale factor's copy over its original"""
    out = []
    for m in re.finditer(r"F\((\d+),\s*(\d+)\)", str(chk)): out.append((int(m.group(2)), int(m.group(1))))
    return out
def lesson_keys(t, chk=None, fig=None):
    """the page's keys for what one shown thing works: read from its words, its math, its figure and its check tuple"""
    K = set(); sc = [scale(x) for x in re.findall(r"(?:1/\d+|1) in : \d+ ft", t)]
    copyctx = re.search(r"copy|copied|scale factor", t)
    # scale factors: a side that becomes another, a pair of rectangles, k = b/a, a check's F(b, a)
    for m in re.finditer(r"A (\d+) cm side becomes (\d+) cm in the copy", t): K.add(("sf", "%s>%s" % m.groups()))
    for m in re.finditer(r"(\d+) cm → (\d+) cm", t): K.add(("sf", "%s>%s" % m.groups()))
    rects = [((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))) for m in re.finditer(r"An? (\d+) cm by (\d+) cm rectangle is copied at (\d+) cm by (\d+) cm", t)]
    if fig and fig.get("kind") == "rects": rects.append((tuple(fig["a"]), tuple(fig["b"])))
    for (a1, a2), (b1, b2) in rects:
        K.update([("sf", "%d>%d" % (a1, b1)), ("sf", "%d>%d" % (a2, b2))])
        if R(b1, a1) == R(b2, a2): K.add(("rect", "%d,%d|%s" % (min(a1, a2), max(a1, a2), ks(R(b1, a1)))))   # the copy's sides are on the board: its perimeter and area are one step away
    for m in re.finditer(r"k = \{?\d+\}? = (\d+) (\d+) × \1 = (\d+)", t): K.update([("sf", "%s>%s" % (m.group(2), m.group(3))), ("sf", "%s>%s" % (m.group(3), m.group(2)))])   # k = √16 = 4, then 3 × 4 = 12 (5.02 Example 2): the pair, both ways
    for m in re.finditer(r"A = (\d+) × (\d+)\^2 = \d+ × \d+ = (\d+)", t): K.add(("areaK", "%s>%s" % (m.group(1), m.group(3))))   # A = 18 × 4² = 288 (5.02's Your Turn), the area ratio run backwards
    if copyctx and not re.search(r"area", t):
        for m in re.finditer(r"k = ([^.;|]*)", t):
            for f in re.finditer(r"(?<![\d.])(\d+)/(\d+)(?![\d.])", m.group(1)): K.add(("sf", "%s>%s" % (f.group(2), f.group(1))))
        for m in re.finditer(r"(?<![\d.])(\d+)/(\d+) = [\d.]+(?![\d/])", t): K.add(("sf", "%s>%s" % (m.group(2), m.group(1))))
        for a, b in check_fracs(chk): K.add(("sf", "%d>%d" % (a, b)))
    # rectangles scaled, and a rectangle's perimeter and area
    for m in re.finditer(r"A (\d+) cm by (\d+) cm rectangle is scaled by k = (\d+(?:\.\d+)?)", t):
        w, h = int(m.group(1)), int(m.group(2)); K.update([("rect", "%d,%d|%s" % (min(w, h), max(w, h), m.group(3))), ("rectWH", "%d,%d" % (min(w, h), max(w, h)))])
    for m in re.finditer(r"perimeter and the area of a (\d+) cm by (\d+) cm rectangle", t):
        w, h = int(m.group(1)), int(m.group(2)); K.add(("rectWH", "%d,%d" % (min(w, h), max(w, h))))
    if fig and fig.get("kind") == "rects" and re.search(r"perimeter|area|P:|A:", t):
        (w, h), (W, H) = tuple(fig["a"]), tuple(fig["b"]); K.add(("rectWH", "%d,%d" % (min(w, h), max(w, h))))
    # areas: k from two areas; an area scaled
    for m in re.finditer(r"area (\d+) cm\^2\.? (?:\| )?Its scale copy has area (\d+) cm\^2", t): K.add(("areaK", "%s>%s" % m.groups()))
    for m in re.finditer(r"A: (\d+) → (\d+)", t): K.add(("areaK", "%s>%s" % m.groups()))
    for m in re.finditer(r"(?<![\d.])(\d+)/(\d+) = (\d+) = k\^2", t): K.add(("areaK", "%s>%s" % (m.group(2), m.group(1))))
    for m in re.finditer(r"A figure of area (\d+) cm\^2 is scaled by k = (\d+)", t): K.add(("areaK", "%s>%d" % (m.group(1), int(m.group(1)) * int(m.group(2)) ** 2)))
    for m in re.finditer(r"sqrt\(F\((\d+),\s*(\d+)\)\)", str(chk)): K.add(("areaK", "%s>%s" % (m.group(2), m.group(1))))
    # plans: a room at a scale, its walls, a real wall drawn
    for m in re.finditer(r"(?:A )?room (?:is )?([\d.]+) in by ([\d.]+) in(?: on the plan)?(?: at ((?:1/\d+|1) in : \d+ ft))?", t):
        r = scale(m.group(3)) if m.group(3) else (sc[0] if sc else None)
        if r is None: continue
        p, q = R(m.group(1)), R(m.group(2)); K.update([("room", "%s|%s,%s" % (ks(r), ks(min(p, q)), ks(max(p, q)))), ("wall", "%s|%s" % (ks(r), ks(p))), ("wall", "%s|%s" % (ks(r), ks(q)))])
    if fig and fig.get("kind") == "rect" and fig.get("names"):
        r = scale(fig["names"][0]); p, q = R(str(fig["a"][0])), R(str(fig["a"][1]))
        if r: K.update([("room", "%s|%s,%s" % (ks(r), ks(min(p, q)), ks(max(p, q)))), ("wall", "%s|%s" % (ks(r), ks(p))), ("wall", "%s|%s" % (ks(r), ks(q)))])
    if re.search(r"plan|drawing", t):
        for m in re.finditer(r"(?<![\d.])(\d+) ÷ (\d+) = ([\d.]+) in", t): K.update([("plan", "%s|%s" % (m.group(2), m.group(1))), ("wall", "%s|%s" % (m.group(2), ks(R(m.group(3)))))])
    for m in re.finditer(r"At ((?:1/\d+|1) in : \d+ ft), how long is a (\d+)-ft wall", t): K.add(("plan", "%s|%s" % (ks(scale(m.group(1))), m.group(2))))
    # conversions: n × ratio, n ÷ ratio, "How many … is n u?"
    for m in re.finditer(r"(?<![\d.])(\d+(?:\.\d+)?) ?(?:in|cm|lb|kg|gal|L|mi|km|ft|m|c|oz|g|km/h|mi/h)? ?([×÷]) ?(%s)(?![\d])" % RATS, t):
        d = RAT2DIR[m.group(3)]; d = d if m.group(2) == "×" else INV[d]
        if not re.search(r"\^2|square", t[max(0, m.start() - 12):m.end() + 4]): K.add(("conv", "%s|%s" % (d, ks(R(m.group(1))))))
    for m in re.finditer(r"How many (\w+) is (\d+) (in|cm|lb|kg|gal|L|mi|km|ft|m)\?", t):
        if m.group(1) in UNIT_OF: K.add(("conv", "%s>%s|%s" % (m.group(3), UNIT_OF[m.group(1)], m.group(2))))
    # square units across systems
    for m in re.finditer(r"(?<![\d.])(\d+) (in|ft|m|cm|mi|km)\^2 = ([\d.]+) (in|ft|m|cm|mi|km)\^2", t):
        if m.group(2) != m.group(4) and {m.group(2), m.group(4)} not in ({"ft", "in"}, {"m", "cm"}): K.add(("sqconv", "%s2>%s2|%s" % (m.group(2), m.group(4), m.group(1))))
    SQR = {"2.54": "cm", "0.39": "in", "0.305": "m", "3.28": "ft", "1.61": "km", "0.62": "mi"}     # a square unit through a ratio across systems
    for m in re.finditer(r"(?<![\d.])(\d+) (in|ft|m|cm|mi|km)\^2 = (?:[\d.]+ × )?(2\.54|0\.39|0\.305|3\.28|1\.61|0\.62)(?:\^2| × \3)", t):
        K.add(("sqconv", "%s2>%s2|%s" % (m.group(2), SQR[m.group(3)], m.group(1))))
    if re.search(r"1 ft = 0\.305 m, so 1 ft\^2", t): K.add(("sqconv", "ft2>m2|1"))
    # money
    if re.search(r"dollar|euro|CAD", t):
        for m in re.finditer(r"(?<![\d.])(\d+) × ([01]\.\d+)(?: = \$?([\d.]+))?", t):
            K.add(("curA", "%s|%s" % (ks(R(m.group(2))), m.group(1))))
            if m.group(3): K.add(("curB", "%s|%s" % (ks(R(m.group(2))), ks(R(m.group(3))))))
        for m in re.finditer(r"(?<![\d.])(\d+(?:\.\d+)?) ÷ ([01]\.\d+)(?: = \$?(\d+))?", t):
            K.add(("curB", "%s|%s" % (ks(R(m.group(2))), ks(R(m.group(1))))))
            if m.group(3): K.add(("curA", "%s|%s" % (ks(R(m.group(2))), m.group(3))))
    # a tank, a trip
    for m in re.finditer(r"(?<![\d.])(\d+) × ([\d.]+) = [\d.]+ mi per tank", t):
        K.add(("tank", "%s|%s" % (m.group(1), ks(R(m.group(2))))))
        for d in re.finditer(r"([\d,]+) ÷ [\d.]+ (?:≈|=) ", t): K.add(("trip", "%s|%s|%s" % (m.group(1), ks(R(m.group(2))), num(d.group(1)))))
    # recipes
    rm = re.search(r"A recipe for (\d+) servings uses (%s) cups" % MIX, t)
    if rm:
        s_, c_ = rm.group(1), kfrac(num(rm.group(2)))
        for m in re.finditer(r"for (\d+) servings\?", t): K.add(("recA", "%s|%s|%s" % (s_, c_, m.group(1))))
        for m in re.finditer(r"With (%s) cups on hand" % MIX, t): K.add(("recB", "%s|%s|%s" % (s_, c_, kfrac(num(m.group(1))))))
    for m in re.finditer(r"k = (\d+)/(\d+) = [\d.]+ (?:\S+ )*?[\d.]+ × (%s) = (%s) cups" % (MIX, MIX), t):
        K.add(("recA", "%s|%s|%s" % (m.group(2), kfrac(num(m.group(3))), m.group(1)))); K.add(("recK", "%s|%s" % (ks(R(int(m.group(1)), int(m.group(2)))), kfrac(num(m.group(3))))))
    if rm:
        for m in re.finditer(r"for (\d+) servings\?", t): K.add(("recK", "%s|%s" % (ks(R(int(m.group(1)), int(rm.group(1)))), kfrac(num(rm.group(2))))))
    # mixtures
    for m in re.finditer(r"(\d+) ?: ?(\d+) ?: ?(\d+),? (\d+) gal of the (first|second|third)", t):
        K.add(("mix", "%s:%s:%s|%d|%s" % (m.group(1), m.group(2), m.group(3), ["first", "second", "third"].index(m.group(5)), m.group(4))))
    for m in re.finditer(r"(\d+) : (\d+) : (\d+) with (\d+) gal of \w+ has k = (\d+)", t):
        parts = [int(m.group(i)) for i in (1, 2, 3)]; part = int(m.group(4)) // int(m.group(5))
        if part in parts: K.add(("mix", "%s|%d|%s" % (":".join(map(str, parts)), parts.index(part), m.group(4))))
    # two speeds in two units
    for m in re.finditer(r"(\d+) km/h × 0\.62 = [\d.]+ mi/h,? (?:so )?(?:[\d.]+ [<>] )?(\d+)", t): K.add(("speed", "%s|%s" % (m.group(1), m.group(2))))
    return K

SHOWN = []                                            # (where, its words, the page's keys it works)
def add_shown(where, obj, chk=None, fig=None):
    t = " | ".join(tex_plain(s) for s in texts(obj)); SHOWN.append((where, t, lesson_keys(t, chk, fig)))
for f in sorted(os.listdir(BUILD)):
    if not re.match(r"^l\d\d\.py$", f): continue
    L = load(os.path.join(BUILD, f)).L
    for i, w in enumerate(L["warmup"]): add_shown("%s warm-up %d" % (L["code"], i + 1), {"stem": w["stem"], "answer": w["answer"]}, w.get("check"))
    for i, nn in enumerate(L["notes"]): add_shown("%s Notes %s" % (L["code"], nn.get("numeral", i + 1)), {k: nn.get(k) for k in ("head", "note", "math", "items2", "items")}, None, nn.get("fig"))
    for i, e in enumerate(L["examples"]):
        add_shown("%s Example %d" % (L["code"], i + 1), {k: e.get(k) for k in ("prompt", "ask", "worked")}, e.get("check"), e.get("fig"))
        if e.get("your_turn"): add_shown("%s Example %d Your Turn" % (L["code"], i + 1), e["your_turn"], e.get("yt_check"), e["your_turn"].get("fig"))
for i, sec in enumerate(U["reference"]):
    add_shown("the reference sheet, section %d" % (i + 1), [b for b in sec["blocks"] if isinstance(b, str)], None)
    for b in sec["blocks"]:
        if isinstance(b, dict) and b.get("table"):
            for row in b["table"][1][1:]: add_shown("the reference sheet, section %d's table" % (i + 1), " · ".join(row), None)
SHOWN_KEYS = {}
for where, t, K in SHOWN:
    for k in K: SHOWN_KEYS.setdefault(k, where)
def shown_hits(slot, key):
    if slot == "sel3":                               # a scale factor alone: shown when a notes line says k is this number
        return [where for where, t, K in SHOWN if re.search(r"angle|perimeter|area", t) and (re.search(r"(?:^|[^\d.])k = (?:[^=|]*= )?%s(?![\d./])" % re.escape(key), t) or re.search(r"= %s = k(?![\^²])" % re.escape(key), t))]
    return [SHOWN_KEYS[(slot, key)]] if (slot, key) in SHOWN_KEYS else []

# ------------------------------------------------------------------ the page
D = json.load(open(os.path.join(HERE, "dump.json")))
FAST = set()
for row in U["reference"][1]["blocks"][0]["table"][1][1:]:
    for cell in row: FAST.update(x.strip() for x in cell.split("·"))
TEST_ANSWERS = set()
for f in ("A", "B"):
    for qn, st, P, opts, it in form_items(U["assessment"]["forms"][f]):
        for a in [it.get("answer", "")] + [p.get("answer", "") for p in it.get("parts", [])]:
            for x in re.findall(r"\d[\d,]*(?:\.\d+)?", tex_plain(a)):
                if num(x) > 1: TEST_ANSWERS.add(num(x))
for t in D.get("fixed", []):
    for x in re.findall(r"\d[\d,]*(?:\.\d+)?(?: \d+/\d+)?|\d+/\d+", t):
        if num(x) in TEST_ANSWERS: bad("the page's fixed text has a test answer, %s: %s" % (x, t))

def chain_value(h):
    """the last value of a worked line "a × b = c" (or its only value)"""
    t = re.sub(r"(\d),(?=\d{3})", r"\1", h).replace("−", "-").replace("×", "*").replace("÷", "/")
    t = re.sub(r"(\d+) (\d+)/(\d+)", r"(\1+\2/\3)", t)
    seg = [s for s in re.split(r"[=≈]", t)][-1]
    seg = re.sub(r"[A-Za-z$²]+.*$", "", seg).strip()
    return sympify(seg.replace("/", "/"), rational=True) if seg else None

n = {"items": 0, "parts": 0, "mc": 0, "multi": 0, "lines": 0, "hints": 0, "models": 0, "ratios": 0, "shown": 0}
shown_report = {}
for S in D["sets"]:
    for it in S["items"]:
        n["items"] += 1; qn = it["q"]; P = [p["stem"] for p in it["parts"]]
        try:
            keys, ans, correct = read(qn, it["stem"], P, it.get("opts") or [])
        except ValueError as e:
            bad("set %d Q%d: %s" % (S["seed"], qn, e)); continue
        for k in keys:
            if k in TEST: bad("set %d Q%d is the test's: %s %s" % (S["seed"], qn, k[0], k[1]))
            if k in HOME: bad("set %d Q%d is the practice test's or the review's: %s %s" % (S["seed"], qn, k[0], k[1]))
            h = shown_hits(*k)
            if h:
                n["shown"] += 1; shown_report.setdefault(k, h)
                bad("set %d Q%d uses numbers a lesson showed (%s): %s %s" % (S["seed"], qn, ", ".join(h[:2]), k[0], k[1]))
        for m in re.finditer(r"1 (\w+) = ([\d.,]+) (\w+)", it["stem"]):
            n["ratios"] += 1
            r = "1 %s = %s %s" % m.groups()
            if r not in FAST and not r.startswith("1 US dollar"): bad("set %d Q%d prints a ratio not on the FAST sheet: %s" % (S["seed"], qn, r))
        if it["type"] in ("mc", "multi"):
            n[it["type"]] += 1
            want = sorted(correct) if it["type"] == "multi" else correct
            got = sorted(it["correct"]) if it["type"] == "multi" else it["correct"]
            if want != got: bad("set %d Q%d keyed %s, worked out here %s" % (S["seed"], qn, got, want))
            continue
        if len(ans) != len(it["parts"]): bad("set %d Q%d: %d parts read, %d on the page" % (S["seed"], qn, len(ans), len(it["parts"]))); continue
        for pi, (p, a) in enumerate(zip(it["parts"], ans)):
            n["parts"] += 1; where = "set %d Q%d%s" % (S["seed"], qn, p["label"])
            if frac(p["ans"]) != a: bad("%s: the key is %s, worked out here %s" % (where, p["ans"], a))
            kt = re.sub(r"^[a-z ]+ ", "", p["keyText"]).replace(",", "")
            if num(kt) != a: bad("%s: what a student types for the key, %s, is not %s" % (where, kt, a))
            for l in p["sol"]:
                if l["h"]:
                    n["lines"] += 1
                    try:
                        v = chain_value(l["h"])
                        if v != a: bad("%s: worked line %s is worth %s, not %s" % (where, l["h"], v, a))
                    except Exception as e: bad("%s: cannot read worked line %s" % (where, l["h"]))
            if not p["walk"] or frac(p["walk"][-1]["ans"]) != a: bad("%s: the Hint does not end on the key" % where)
            for s in p["walk"]:
                n["hints"] += 1
                m = re.match(r"^What is ([\d.,()+\-×÷ /]+)\?", s["ask"])
                if m and not re.search(r"\d \d", m.group(1).replace(" × ", "*").replace(" ÷ ", "/")):
                    try:
                        v = chain_value(m.group(1))
                        if v is not None and v != frac(s["ans"]): bad("%s: the Hint asks %s, worth %s, and expects %s" % (where, m.group(1), v, frac(s["ans"])))
                    except Exception: pass
                if pi > 0 and frac(s["ans"]) == ans[0]: bad("%s: part (b)'s Hint asks for part (a)'s answer" % where)
            for mo in p["models"]:
                n["models"] += 1
                if frac(mo["v"]) == a: bad("%s: a modelled mistake is the key" % where)

nprob = sum(1 for p in probs if p is None)
print("verify (sympy): %d questions read back, %d typed parts, %d multiple choice, %d select-all, %d worked lines, %d Hint steps, %d mistakes, %d printed ratios; "
      "Form A %d keys, Form B %d, the practice test and the review %d; %d things the lessons and the reference sheet show; %d problem(s)"
      % (n["items"], n["parts"], n["mc"], n["multi"], n["lines"], n["hints"], n["models"], n["ratios"], len(FORM_KEYS["A"]), len(FORM_KEYS["B"]), len(HOME), len(SHOWN), nprob))
for p in probs:
    if p: print("  " + p)
if "--shown" in sys.argv:
    for k in sorted(SHOWN_KEYS): print("  shown: %s %s — %s" % (k[0], k[1], SHOWN_KEYS[k]))
    for k3 in ["5", "6", "7", "8", "9", "10", "1.5", "2", "2.5", "3", "3.5", "4", "4.5", "0.4", "0.5", "0.8", "1.2", "1.6"]:
        h = shown_hits("sel3", k3)
        if h: print("  shown: sel3 %s — %s" % (k3, ", ".join(h)))
    for k in sorted(FORM_KEYS["practice"]): print("  practice: %s %s" % k)
    for k in sorted(REVIEW): print("  review: %s %s" % k)
sys.exit(1 if nprob else 0)
