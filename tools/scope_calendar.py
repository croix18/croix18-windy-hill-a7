#!/usr/bin/env python3
"""Lay the A7 scope & sequence onto the 2026-27 Lake County calendar, one period per row.
Edit PLAN (in order) and re-run; the markdown table is regenerated from it.
Calendar: Aug 10 2026 - May 28 2027, holidays per the board-approved calendar (verify
against the school copy). Wednesdays are 43-minute periods: absorbed on the day, not planned."""
import datetime as d, json, re, os
HERE=os.path.dirname(os.path.abspath(__file__))
SK=json.load(open(os.path.join(HERE,"..","a7","reference","ixl_skills_by_lesson.json")))
SMARTSCORE=67   # A7 students stop at a SmartScore of 67
THREAD_SKILLS={"T-A1":["14.1","14.2"],"T-A2":["14.3","14.4"],"T-B1":["16.1"],"T-B2":["16.2"],"T-C1":["17.1"],"T-C2":["17.2","17.3"]}
def lessons_for(code):
    if code in THREAD_SKILLS: return THREAD_SKILLS[code]
    m=re.match(r'^(\d+)\.(\d+)(?:[+–-](.*))?',code)
    if not m or code.endswith(("X1","X2","X")) : return []
    u=m.group(1); first=int(m.group(2)); rest=m.group(3)
    nums=[first]
    if rest:
        for part in re.split(r'[+–-]',rest):
            part=part.strip()
            if part.isdigit(): nums.append(int(part))
        if "–" in code:  # a range like 14.01–04
            nums=list(range(first,nums[-1]+1))
    return [f"{u}.{n}" for n in nums]
def ixl(code):
    main=[];also=[]
    for L in lessons_for(code):
        v=SK.get(L,{"main":[],"also":[]})
        main+= [x for x in v["main"] if x not in main]; also+=[x for x in v["also"] if x not in also and x not in main]
    return main,also
start=d.date(2026,9,23)          # first day after the Unit 2 exam (Sep 21-22)
end=d.date(2027,5,28)
hol={d.date(2026,10,12),d.date(2026,11,11),d.date(2027,1,18),d.date(2027,2,15),
     d.date(2027,3,5),d.date(2027,4,16),d.date(2027,1,4),d.date(2027,1,5)}
hol|={d.date(2026,11,x) for x in range(23,28)}
x=d.date(2026,12,21)
while x<=d.date(2027,1,1): hol.add(x); x+=d.timedelta(1)
hol|={d.date(2027,3,x) for x in range(22,27)}
days=[]; x=start
while x<=end:
    if x.weekday()<5 and x not in hol: days.append(x)
    x+=d.timedelta(1)

# (unit, lesson code, title, benchmark(s), kind) kind: L lesson, T woven thread, X exam, R review block
PLAN=[
 (3,"3.01","Product laws of exponents","7.NSO.1.1 · 8.NSO.1.3","L"),
 (3,"3.02","Quotient laws of exponents","7.NSO.1.1 · 8.NSO.1.3","L"),
 (3,"3.03","Exponential expressions","8.NSO.1.3","L"),
 (3,"3.04","Negative exponent law","8.NSO.1.3","L"),
 (3,"3.05","Applying exponent laws","8.NSO.1.3","L"),
 (3,"3.06+07","Evaluating and equivalent expressions with integer exponents","8.NSO.1.3","L"),
 (3,"T-A1","Thread A: the same laws with variable bases (14.1–14.2)","8.AR.1.1","T"),
 (3,"T-A2","Thread A: negative exponents and multiple laws, variable bases (14.3–14.4)","8.AR.1.1","T"),
 (3,"3.08","Large numbers in scientific notation","8.NSO.1.4","L"),
 (3,"3.09","Small numbers in scientific notation; how many times larger","8.NSO.1.4","L"),
 (3,"3.X1","Unit 3 exam, day 1","","X"),
 (3,"3.X2","Unit 3 exam, day 2","","X"),
 (4,"4.01","Add and subtract in scientific notation","8.NSO.1.5","L"),
 (4,"4.02+03","Multiply and divide in scientific notation","8.NSO.1.5","L"),
 (4,"4.04","Real-world scientific notation; significant digits","8.NSO.1.6","L"),
 (4,"4.05","Expressions with radicals (perfect squares to 225, cubes −125 to 125)","8.NSO.1.7","L"),
 (4,"4.06","Order of operations with exponents and radicals","8.NSO.1.7","L"),
 (4,"4.07+08","Real-world order-of-operations problems","8.NSO.1.7","L"),
 (4,"4.X1","Unit 4 exam, day 1","","X"),
 (4,"4.X2","Unit 4 exam, day 2","","X"),
 (5,"5.01","Scale drawings","7.GR.1.5","L"),
 (5,"5.02+03","Scale factor: perimeter and area (k and k²)","7.GR.1.5","L"),
 (5,"5.04","Real-world scale drawings","7.GR.1.5","L"),
 (5,"5.06+07","Converting length across systems; currency","7.AR.3.3","L"),
 (5,"5.08+09","Converting mass, area and volume across systems","7.AR.3.3","L"),
 (5,"5.10+11","Multi-step proportion problems","7.AR.3.3 · 7.AR.4.5","L"),
 (5,"5.X1","Unit 5 exam, day 1","","X"),
 (5,"5.X2","Unit 5 exam, day 2","","X"),
 (6,"6.01+02","Triangle Inequality Theorem; converse of the Pythagorean Theorem","8.GR.1.3","L"),
 (6,"6.03","Pythagorean Theorem (memorize)","8.GR.1.1","L"),
 (6,"6.04","Pythagorean Theorem in real-world problems","8.GR.1.1","L"),
 (6,"6.05","Distance on the coordinate plane","8.GR.1.2","L"),
 (6,"6.06","Real-world coordinate-plane problems; perimeter","8.GR.1.2","L"),
 (6,"T-B1","Thread B: angle pairs — supplementary, complementary, vertical, adjacent (16.1)","8.GR.1.4","T"),
 (6,"T-B2","Thread B: interior and exterior angles of a triangle (16.2)","8.GR.1.5","T"),
 (6,"6.07+08","Similar triangles; indirect measurement","8.GR.2.4","L"),
 (6,"6.X1","Unit 6 exam, day 1","","X"),
 (6,"6.X2","Unit 6 exam, day 2","","X"),
 (7,"7.01","Graphing proportional relationships","7.AR.4.3","L"),
 (7,"7.02+03","Constant of proportionality (table, graph, description)","7.AR.4.2","L"),
 (7,"7.04","Is it proportional?","7.AR.4.1 · 8.AR.3.1","L"),
 (7,"7.05+06","Equations of proportional relationships; translating representations","7.AR.4.4","L"),
 (7,"7.07","Comparing proportional relationships","7.AR.4.5","L"),
 (7,"7.X1","Unit 7 exam, day 1","","X"),
 (7,"7.X2","Unit 7 exam, day 2","","X"),
 (0,"PM2-R1","PM2 review 1: number system, exponents, scientific notation (whiteboards)","8.NSO.1.1–1.7","R"),
 (0,"PM2-R2","PM2 review 2: equations, inequalities, Pythagorean, angles (whiteboards)","8.AR.2 · 8.GR.1","R"),
 (0,"PM2-R3","PM2 review 3: proportional → linear preview; mixed FAST-shaped round","8.AR.3 · 8.AR.1.1","R"),
 (8,"8.01+02","Circle relationships; circumference","7.GR.1.3","L"),
 (8,"8.03","Radius and diameter from circumference","7.GR.1.3","L"),
 (8,"8.04+05","Area of a circle","7.GR.1.4","L"),
 (8,"8.06","Circumference and area problems; sectors","7.GR.1.4","L"),
 (8,"8.08+09","Sectors and circle graphs","7.GR.1.4 · 7.DP.1.4","L"),
 (9,"9.01+02","Surface area of cylinders from nets","7.GR.2.1 · 7.GR.2.2","L"),
 (9,"9.03+04+05","Volume of cylinders; problems","7.GR.2.3","L"),
 (9,"8/9.X1","Units 8–9 exam, day 1","","X"),
 (9,"8/9.X2","Units 8–9 exam, day 2","","X"),
 (10,"10.01","Proportional relationships revisited (linear ⇒ proportional?)","8.AR.3.1","L"),
 (10,"10.02+03","Slope from two points, graphs, tables","8.AR.3.2","L"),
 (10,"10.04","Slope in context","8.AR.3.2 · 8.AR.3.5","L"),
 (10,"10.05","Slope-intercept form; graph a line","8.AR.3.4","L"),
 (10,"10.06","Graphing from tables and contexts","8.AR.3.4","L"),
 (10,"10.07+08","Interpreting slope and intercept (graphs, equations, tables, descriptions; F↔C)","8.AR.3.5","L"),
 (10,"10.09","Writing equations of lines","8.AR.3.3","L"),
 (10,"10.10","Writing equations for contexts; lines of fit preview","8.AR.3.3 · 8.AR.3.5","L"),
 (10,"10.X1","Unit 10 exam, day 1","","X"),
 (10,"10.X2","Unit 10 exam, day 2","","X"),
 (11,"11.01","Equations with like terms and the distributive property","8.AR.2.1","L"),
 (11,"11.02","Variables on both sides","8.AR.2.1","L"),
 (11,"11.03","One, none, infinitely many solutions","8.AR.2.1","L"),
 (11,"11.04","Multi-step equations","8.AR.2.1","L"),
 (11,"11.05+06","Systems: which points are solutions; how many solutions","8.AR.4.1 · 8.AR.4.2","L"),
 (11,"11.07","Solving systems by graphing","8.AR.4.3","L"),
 (11,"11.08","Systems in context (approximate solutions)","8.AR.4.3","L"),
 (11,"11.X1","Unit 11 exam, day 1","","X"),
 (11,"11.X2","Unit 11 exam, day 2","","X"),
 (12,"12.01+02","Relations; domain and range","8.F.1.1","L"),
 (12,"12.03","Is it a function?","8.F.1.1","L"),
 (12,"12.04+05","Describing graphs: increasing, decreasing, constant","8.F.1.3","L"),
 (12,"12.06","Sketching graphs from descriptions","8.F.1.3","L"),
 (12,"12.07","Functions from equations, tables, graphs","8.F.1.2","L"),
 (12,"12.08+09","Is it linear? (graphs, equations, tables)","8.F.1.2 · 8.AR.3.1","L"),
 (12,"12.X1","Unit 12 exam, day 1","","X"),
 (12,"12.X2","Unit 12 exam, day 2","","X"),
 (13,"13.01+02+03","Choosing and creating displays (numerical, categorical)","7.DP.1.5","L"),
 (13,"13.04+05","Bivariate data; line graphs","8.DP.1.1","L"),
 (13,"13.06","Scatter plots and association","8.DP.1.1 · 8.DP.1.2","L"),
 (13,"13.07+08","Lines of fit; outliers","8.DP.1.3 · 8.DP.1.2","L"),
 (13,"13.09","Interpreting the equation of a line of fit","8.DP.1.3 · 8.AR.3.5","L"),
 (13,"T-C1","Thread C: sample spaces of repeated experiments (17.1)","8.DP.2.1","T"),
 (13,"T-C2","Thread C: theoretical probability of repeated experiments (17.2–17.3)","8.DP.2.2","T"),
 (13,"13.X1","Unit 13 exam, day 1","","X"),
 (13,"13.X2","Unit 13 exam, day 2","","X"),
 (14,"14.01–04","Exponent laws with variable bases — consolidation of Thread A","8.AR.1.1","L"),
 (14,"14.05+06","Multiplying a monomial by a linear expression","8.AR.1.2","L"),
 (14,"14.07+08","Factoring a common monomial","8.AR.1.3","L"),
 (14,"14.X1","Unit 14 exam, day 1","","X"),
 (14,"14.X2","Unit 14 exam, day 2","","X"),
 (15,"15.01","Slides, flips, spins","8.GR.2.1","L"),
 (15,"15.02+03","Reflections, rotations, translations — identify and describe","8.GR.2.1","L"),
 (15,"15.03b","Translations on the coordinate plane","8.GR.2.3","L"),
 (15,"15.04","Reflections on the coordinate plane","8.GR.2.3","L"),
 (15,"15.05","Rotations on the coordinate plane (about the origin)","8.GR.2.3","L"),
 (15,"15.06","Describing rigid transformations; congruence","8.GR.2.1 · 8.GR.2.3","L"),
 (15,"15.07+09","Dilations and scale factor","8.GR.2.2","L"),
 (15,"15.08","Dilations on the coordinate plane (centered at the origin)","8.GR.2.3","L"),
 (16,"16.01+02","Angle relationships — consolidation of Thread B","8.GR.1.4 · 8.GR.1.5","L"),
 (16,"16.03+04","Interior angles of polygons","8.GR.1.6","L"),
 (16,"15/16.X1","Units 15–16 exam, day 1","","X"),
 (16,"15/16.X2","Units 15–16 exam, day 2","","X"),
 (17,"17.01–03","Repeated experiments — consolidation of Thread C","8.DP.2.1 · 8.DP.2.2","L"),
 (17,"17.04–06","Predictions from theoretical probability","8.DP.2.3","L"),
 (17,"17.X","Unit 17 exam (one day)","","X"),
]
# one flex day after every exam: reteach from exam evidence, or absorb a lost day
P2=[]
for r in PLAN:
    P2.append(r)
    if r[4]=="X" and r[1].endswith("X2") and r[0] in (3,4,6,9,10,11,12):   # not after 5 (Grade 7 unit), 7 (PM2 review follows), 13 (keeps Unit 14 whole before spring break); Q4's buffer is the PM3 review block
        P2.append((r[0],"flex","Flex day — reteach from exam evidence, or absorb a lost day","","F"))
PLAN=P2
assert len(PLAN)<=len(days), (len(PLAN),len(days))
rows=[]
for (u,code,title,bm,kind),dt in zip(PLAN,days):
    rows.append((dt,u,code,title,bm,kind))
# PM3 review fills every remaining period up to Apr 30; the window opens May 3
pm3=d.date(2027,5,3)
cats=["NSO and probability","algebraic reasoning (expressions, equations, systems)","linear relationships, functions, data","geometric reasoning"]
n=0
for dt in days[len(PLAN):]:
    if dt<pm3:
        n+=1
        title=f"PM3 review {n}: "+(cats[n-1] if n<=4 else "mixed FAST-shaped rounds, one category per whiteboard question")
        rows.append((dt,0,f"PM3-R{n}",title,"all","R"))
    elif dt<=d.date(2027,5,28) and not any(r[2]=="PM3" for r in rows):
        rows.append((dt,0,"PM3","May 3–28: PM3 window (school date TBD). Non-test days: Algebra 1 bridge — operations with radicals, point-slope and standard form, systems by substitution","912.NSO.1.4 · 912.AR.2.2 · 912.AR.9.1","W"))
if __name__=="__main__":
    import sys
    print(f"| Date | Day | Unit | Lesson | What is taught | Benchmark | IXL skill(s) — code | Also consider — code | Due |")
    print("|---|---|---|---|---|---|---|---|---|")
    for i,(dt,u,code,title,bm,kind) in enumerate(rows):
        wd=dt.strftime("%a")
        flag=" (43 min)" if wd=="Wed" else ""
        mark={"T":"**thread** ","X":"**exam** ","R":"**review** ","F":"*flex* ","W":""}.get(kind,"")
        main,also=ixl(code)
        nxt=[r[0] for r in rows[i+1:] if r[5] not in ("W",)]
        due=nxt[0].strftime('%b %d') if (main and nxt) else ""
        M="; ".join(f"{x} — ____" for x in main); A="; ".join(f"{x} — ____" for x in also)
        print(f"| {dt.strftime('%b %d')} | {wd}{flag} | {u if u else ''} | {code} | {mark}{title} | {bm} | {M} | {A} | {due} |")
    # student-facing due-date sheet
    with open(os.path.join(HERE,"..","a7","reference","A7 IXL DUE DATES 2026-27.md"),"w") as f:
        f.write(f"# A7 — IXL assignments and due dates, 2026–27\n\nEach class day ends with IXL. Whatever is not finished in class is that night's practice. **Done means a SmartScore of {SMARTSCORE} on every listed skill.** Due = the next class day. \"Also consider\" skills are optional extra practice on the same idea.\n\nSkill codes: fill in from IXL's printed skill plan (the ____ blanks) — see the note at the end.\n\n| Assigned | Lesson | Required skills (SmartScore {SMARTSCORE}) | Optional (also consider) | Due |\n|---|---|---|---|---|\n")
        for i,(dt,u,code,title,bm,kind) in enumerate(rows):
            main,also=ixl(code)
            if not main: continue
            nxt=[r[0] for r in rows[i+1:] if r[5] not in ("W",)]
            due=nxt[0].strftime('%a %b %d') if nxt else ""
            M="; ".join(f"{x} (____)" for x in main); A="; ".join(f"{x} (____)" for x in also)
            f.write(f"| {dt.strftime('%a %b %d')} | {code} {title} | {M} | {A} | {due} |\n")
        f.write("\n*Codes:* IXL's page shows skill names; the codes (e.g. 8th grade F.5) print on IXL's \"Print skill plan\" PDF. Send that PDF and the blanks get filled by script, or fill them once in `a7/reference/ixl_skills_by_lesson.json` (add a `code` per skill) and re-run `tools/scope_calendar.py`.\n")
    print(f"\nPlanned periods: {len(rows)} of {len(days)} available Sep 23–May 28; PM3 review days: {n}", file=sys.stderr)
    for dt,u,code,title,bm,kind in rows:
        if code.endswith("X1") or code=="17.X" or code.startswith("PM"):
            pass
    import collections
    firsts={}
    for dt,u,code,title,bm,kind in rows:
        if u and u not in firsts: firsts[u]=dt
    print("Unit starts:", {k:v.strftime('%b %d') for k,v in firsts.items()}, file=sys.stderr)
