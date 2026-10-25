# A7 Unit 5 — Multi-Step Proportional Relationships: Reference Sheet, Unit
# Review (home Tue 3 Nov, key Wed; ruling 27a — A7 has no review day), Unit Assessment as Form A,
# Form B and the practice test (ruling 33). Every conversion ratio is the FAST Grade 7 reference
# sheet's and no other (outline decision 1), and every item prints the ratio it needs. Currency
# rates are printed and dated on the item and never real (decision 2). Two transfer items on both
# test forms at the same positions, never on the practice test or the review (ruling 18): question
# 8 (a plan's real area reported in square meters — GR.1.5 with AR.3.3 inside; its type was 5.10
# board 8) and question 19 (a rate comparison across systems ending in a decision — AR.4.5; its type
# was 5.10 board 9). DOK 3 at about 8% (ruling 17): questions 8 and 19, each a decision or a chain the unit rehearsed but never practised; every answer on the paper is a number, a letter or a set of letters (7 Oct: "I don't want to read explanations"). Every value is
# re-derived at build time; no keyed value is shared across forms at the same position (ruling 33).


def pick(form, a, b, p):
    """One value per form: A, B, practice."""
    return {"A": a, "B": b, "practice": p}[form]


def _gr15(form):
    P = lambda a, b, p: pick(form, a, b, p)
    q1 = dict(stem=P("A 4 cm side of a figure is 10 cm in its scale copy. Find the scale factor.",
                     "A 6 cm side of a figure is 9 cm in its scale copy. Find the scale factor.",
                     "A 4 cm side of a figure is 12 cm in its scale copy. Find the scale factor."),
              answer=P("k = 2.5", "k = 1.5", "k = 3"), why="copy ÷ original",
              check=P(("eq", "F(10,4)", "F(5,2)"), ("eq", "F(9,6)", "F(3,2)"), ("eq", "F(12,4)", "3")), space=0.6)
    q2 = dict(stem=P("A 15 cm side of a figure is 6 cm in its scale copy. Find the scale factor.",
                     "A 20 cm side of a figure is 5 cm in its scale copy. Find the scale factor.",
                     "A 12 cm side of a figure is 6 cm in its scale copy. Find the scale factor."),
              answer=P("k = 0.4", "k = 0.25", "k = 0.5"), why=P("copy ÷ original; the copy is smaller, so k is under 1 — 2.5 is the proportion backwards", "copy ÷ original; the copy is smaller, so k is under 1 — 4 is the proportion backwards", "copy ÷ original; the copy is smaller, so k is under 1 — 2 is the proportion backwards"),
              check=P(("eq", "F(6,15)", "F(2,5)"), ("eq", "F(5,20)", "F(1,4)"), ("eq", "F(6,12)", "F(1,2)")), space=0.6)
    # question 3 — FAST's multiselect shape: the B1G-M's "scaling area like length" and Math
    # Nation's "angles scale too" are both choices the student has to leave alone
    k3 = P(3, 4, 2)
    q3 = dict(stem=f"A figure is scaled by a scale factor of {k3}. Select ALL of the statements that are true about the copy.",
              choices=P([f"Each side is {k3} times as long.", f"Each angle is {k3} times as large.", f"The perimeter is {k3} times as long.", f"The area is {k3} times as large.", f"The area is {k3 * k3} times as large."],
                        [f"Each angle is {k3} times as large.", f"The area is {k3 * k3} times as large.", f"Each side is {k3} times as long.", f"The area is {k3} times as large.", f"The perimeter is {k3} times as long."],
                        [f"The area is {k3} times as large.", f"Each side is {k3} times as long.", f"The perimeter is {k3} times as long.", f"The area is {k3 * k3} times as large.", f"Each angle is {k3} times as large."]),
              correct=P([0, 2, 4], [1, 2, 4], [1, 2, 3]), answer=P("A, C and E", "B, C and E", "B, C and D"),
              errors=P({"B": "angles are not lengths and do not scale [7.GR.1.5: Math Nation's named misconception]", "D": "area × k: scaling area like length [B1G-M 7.GR.1.5]"},
                       {"A": "angles are not lengths and do not scale [7.GR.1.5: Math Nation's named misconception]", "D": "area × k: scaling area like length [B1G-M 7.GR.1.5]"},
                       {"A": "area × k: scaling area like length [B1G-M 7.GR.1.5]", "E": "angles are not lengths and do not scale [7.GR.1.5: Math Nation's named misconception]"}),
              why="All three and nothing else for the point: sides and perimeter × k, area × k², angles unchanged.",
              check=P(("many", ("eq", "3**2", "9"), ("true", "3 != 9"), ("true", "35*3 != 35")), ("many", ("eq", "4**2", "16"), ("true", "4 != 16"), ("true", "35*4 != 35")), ("many", ("eq", "2**2", "4"), ("true", "2 != 4"), ("true", "35*2 != 35"))))
    q4 = dict(stem=P("A 3 cm by 4 cm rectangle is scaled by $k = 3$.", "A 2 cm by 5 cm rectangle is scaled by $k = 4$.", "A 3 cm by 5 cm rectangle is scaled by $k = 2$."),
              parts=[dict(label="a", stem="Find the copy's perimeter.", answer=P("42 cm", "56 cm", "32 cm"), why="perimeter × k",
                          check=P(("eq", "2*(3+4)*3", "42"), ("eq", "2*(2+5)*4", "56"), ("eq", "2*(3+5)*2", "32")), space=0.6),
                     dict(label="b", stem="Find the copy's area.", answer=P("108 cm²", "160 cm²", "60 cm²"), why=P("area × k² — 36 multiplied the area by k once", "area × k² — 40 multiplied the area by k once", "area × k² — 30 multiplied the area by k once"),
                          check=P(("eq", "3*4*9", "108"), ("eq", "2*5*16", "160"), ("eq", "3*5*4", "60")), space=0.6)])
    q5 = dict(stem=P("A figure has area $8\\,\\text{cm}^{2}$. Its scale copy has area $72\\,\\text{cm}^{2}$. What is the scale factor?",
                     "A figure has area $5\\,\\text{cm}^{2}$. Its scale copy has area $80\\,\\text{cm}^{2}$. What is the scale factor?",
                     "A figure has area $6\\,\\text{cm}^{2}$. Its scale copy has area $150\\,\\text{cm}^{2}$. What is the scale factor?"),
              answer=P("k = 3", "k = 4", "k = 5"),
              why=P("72 ÷ 8 = 9 is k², so k = √9. A board with 9 handed in the area ratio as k.", "80 ÷ 5 = 16 is k², so k = √16. A board with 16 handed in the area ratio as k.", "150 ÷ 6 = 25 is k², so k = √25. A board with 25 handed in the area ratio as k."),
              check=P(("eq", "sqrt(F(72,8))", "3"), ("eq", "sqrt(F(80,5))", "4"), ("eq", "sqrt(F(150,6))", "5")), space=1.0)
    q6 = dict(stem=P("A floor plan is drawn at $\\frac{1}{4}\\,\\text{in} : 1\\,\\text{ft}$. A room is 3 in by 3.5 in on the plan.",
                     "A floor plan is drawn at $\\frac{1}{2}\\,\\text{in} : 1\\,\\text{ft}$. A room is 3 in by 5 in on the plan.",
                     "A floor plan is drawn at $1\\,\\text{in} : 5\\,\\text{ft}$. A room is 2 in by 3 in on the plan."),
              parts=[dict(label="a", stem=P("Find the real length of the wall drawn 3 in long.", "Find the real length of the wall drawn 3 in long.", "Find the real length of the wall drawn 2 in long."),
                          answer=P("12 ft", "6 ft", "10 ft"), why=P("the scale per 1 inch, then ×: 1 in : 4 ft", "the scale per 1 inch, then ×: 1 in : 2 ft", "the scale per 1 inch, then ×: 1 in : 5 ft"),
                          check=P(("eq", "3*4", "12"), ("eq", "3*2", "6"), ("eq", "2*5", "10")), space=0.6),
                     dict(label="b", stem="Find the room's real area.", answer=P("168 ft²", "60 ft²", "150 ft²"), why=P("real dimensions first: 12 by 14 — 10.5 in² × 4 = 42 is the named error", "real dimensions first: 6 by 10 — 15 in² × 2 = 30 is the named error", "real dimensions first: 10 by 15 — 6 in² × 5 = 30 is the named error"),
                          check=P(("eq", "12*14", "168"), ("eq", "6*10", "60"), ("eq", "10*15", "150")), space=0.6)])
    q7 = dict(stem=P("A plan is drawn at $1\\,\\text{in} : 4\\,\\text{ft}$. A real wall is 18 ft long. How long is it on the plan?",
                     "A plan is drawn at $\\frac{1}{4}\\,\\text{in} : 1\\,\\text{ft}$. A real wall is 22 ft long. How long is it on the plan?",
                     "A plan is drawn at $1\\,\\text{in} : 3\\,\\text{ft}$. A real wall is 15 ft long. How long is it on the plan?"),
              answer=P("4.5 in", "5.5 in", "5 in"), why="real ÷ rate",
              check=P(("eq", "F(18,4)", "F(9,2)"), ("eq", "F(22,4)", "F(11,2)"), ("eq", "F(15,3)", "5")), space=0.6)
    # question 8 — transfer item 1 on both test forms (a plan's real area reported in square
    # meters: GR.1.5 with AR.3.3 inside; its type was 5.10 board 8); the practice test carries a
    # plan's area in square feet instead
    if form == "practice":
        q8 = dict(stem="A plan is drawn at $1\\,\\text{in} : 6\\,\\text{ft}$. A room is 1.5 in by 2.5 in on the plan. Find the room's real area.",
                  answer="135 ft²", why="9 ft by 15 ft.", check=("eq", "9*15", "135"), space=0.8)
    else:
        q8 = dict(transfer=True,
                  stem=P("A plan is drawn at $1\\,\\text{in} : 5\\,\\text{ft}$. A room is 2 in by 2 in on the plan. $1\\,\\text{ft} = 0.305\\,\\text{m}$. Find the room's real area in square meters.",
                         "A plan is drawn at $1\\,\\text{in} : 4\\,\\text{ft}$. A room is 1.5 in by 2 in on the plan. $1\\,\\text{ft} = 0.305\\,\\text{m}$. Find the room's real area in square meters.", ""),
                  answer=P("About 9.30 m² (3.05 m by 3.05 m); 9.29 by the sheet's other ratio", "About 4.47 m² (1.83 m by 2.44 m); 4.46 by the sheet's other ratio", ""),
                  why=P("10 ft by 10 ft; 3.05 × 3.05 = 9.3025. The same number by the other route: 100 ft² × 0.305² = 9.3025; by the sheet's 1 m = 3.28 ft, 100 ÷ 3.28² = 9.29 — full credit. 30.5 (100 × 0.305) used the ratio once on an area. A plan's area asked in metric appears on no review and in no question bank; its type was 5.10 board 8.",
                        "6 ft by 8 ft; 1.83 × 2.44 = 4.4652. The same number by the other route: 48 ft² × 0.305² = 4.4652; by the sheet's 1 m = 3.28 ft, 48 ÷ 3.28² = 4.46 — full credit. 14.64 (48 × 0.305) used the ratio once on an area. A plan's area asked in metric appears on no review and in no question bank; its type was 5.10 board 8.", ""),
                  check=P(("many", ("eq", "2*5", "10"), ("eq", "10*F(305,1000)*10*F(305,1000)", "F(93025,10000)")),
                          ("many", ("eq", "F(3,2)*4", "6"), ("eq", "2*4", "8"), ("eq", "6*F(305,1000)*8*F(305,1000)", "F(44652,10000)")), None), space=1.0)
    return [q1, q2, q3, q4, q5, q6, q7, q8]


def _ar33(form):
    P = lambda a, b, p: pick(form, a, b, p)
    q9 = dict(stem=P("$1\\,\\text{in} = 2.54\\,\\text{cm}$. How many centimeters is 9 in?", "$1\\,\\text{in} = 2.54\\,\\text{cm}$. How many centimeters is 11 in?", "$1\\,\\text{in} = 2.54\\,\\text{cm}$. How many centimeters is 7 in?"),
              answer=P("22.86 cm (23.1 by ÷ 0.39)", "27.94 cm (28.2 by ÷ 0.39)", "17.78 cm (17.9 by ÷ 0.39)"), why="× the ratio whose 1 is inches; the sheet's other ratio, ÷ 0.39, earns the point too when the work shows it",
              check=P(("eq", "9*F(254,100)", "F(2286,100)"), ("eq", "11*F(254,100)", "F(2794,100)"), ("eq", "7*F(254,100)", "F(1778,100)")), space=0.6)
    # question 10 — FAST's multiselect shape, and the "both sheet directions" decision in front of
    # the student: the B1G-M's inverted ratio is a choice to leave alone
    n10 = P(70, 90, 110)
    q10 = dict(stem=f"1 in = 2.54 cm and 1 cm = 0.39 in. Select ALL of the expressions that give the number of inches in {n10} cm.",
               choices=P([f"${n10} \\times 0.39$", f"${n10} \\times 2.54$", f"${n10} \\div 2.54$", f"${n10} \\div 0.39$"],
                         [f"${n10} \\div 0.39$", f"${n10} \\div 2.54$", f"${n10} \\times 2.54$", f"${n10} \\times 0.39$"],
                         [f"${n10} \\times 2.54$", f"${n10} \\times 0.39$", f"${n10} \\div 0.39$", f"${n10} \\div 2.54$"]),
               correct=P([0, 2], [1, 3], [1, 3]), answer=P("A and C", "B and D", "B and D"),
               errors=P({"B": "× 2.54: the inverted ratio — centimeters are smaller, so fewer inches [B1G-M 7.AR.3.3]", "D": "÷ 0.39: the inverted ratio [B1G-M 7.AR.3.3]"},
                        {"A": "÷ 0.39: the inverted ratio [B1G-M 7.AR.3.3]", "C": "× 2.54: the inverted ratio — centimeters are smaller, so fewer inches [B1G-M 7.AR.3.3]"},
                        {"A": "× 2.54: the inverted ratio — centimeters are smaller, so fewer inches [B1G-M 7.AR.3.3]", "C": "÷ 0.39: the inverted ratio [B1G-M 7.AR.3.3]"}),
               why=P("Both sheet routes (27.3 and 27.6) and nothing else for the point.", "Both sheet routes (35.1 and 35.4) and nothing else for the point.", "Both sheet routes (42.9 and 43.3) and nothing else for the point."),
               check=P(("many", ("eq", "70*F(39,100)", "F(273,10)"), ("true", "70*F(254,100) != 70*F(39,100)"), ("true", "70/F(39,100) != 70*F(39,100)")),
                       ("many", ("eq", "90*F(39,100)", "F(351,10)"), ("true", "90*F(254,100) != 90*F(39,100)"), ("true", "90/F(39,100) != 90*F(39,100)")),
                       ("many", ("eq", "110*F(39,100)", "F(429,10)"), ("true", "110*F(254,100) != 110*F(39,100)"), ("true", "110/F(39,100) != 110*F(39,100)"))))
    q11 = dict(stem=P("$1\\,\\text{yd} = 3\\,\\text{ft}$, $1\\,\\text{ft} = 12\\,\\text{in}$, $1\\,\\text{in} = 2.54\\,\\text{cm}$. How many centimeters is 4 yd?",
                      "$1\\,\\text{yd} = 3\\,\\text{ft}$, $1\\,\\text{ft} = 12\\,\\text{in}$, $1\\,\\text{in} = 2.54\\,\\text{cm}$. How many centimeters is 5 yd?",
                      "$1\\,\\text{yd} = 3\\,\\text{ft}$, $1\\,\\text{ft} = 12\\,\\text{in}$, $1\\,\\text{in} = 2.54\\,\\text{cm}$. How many centimeters is 1.5 yd?"),
               answer=P("365.76 cm", "457.2 cm", "137.16 cm"), why=P("a chain: 144 in, then × 2.54 (144 ÷ 0.39 = 369.2 by the other ratio — full credit). The estimate (a yard is nearly a meter) catches 10.16.", "a chain: 180 in, then × 2.54 (180 ÷ 0.39 = 461.5 by the other ratio — full credit). The estimate catches 12.7.", "a chain: 54 in, then × 2.54 (54 ÷ 0.39 = 138.5 by the other ratio — full credit). The estimate catches 3.81."),
               check=P(("eq", "4*36*F(254,100)", "F(36576,100)"), ("eq", "5*36*F(254,100)", "F(4572,10)"), ("eq", "F(3,2)*36*F(254,100)", "F(13716,100)")), space=0.7)
    q12 = dict(stem=P("$1\\,\\text{kg} = 2.204\\,\\text{lb}$. How many pounds is 20 kg?", "$1\\,\\text{lb} = 0.454\\,\\text{kg}$. How many kilograms is 60 lb?", "$1\\,\\text{kg} = 2.204\\,\\text{lb}$. How many pounds is 35 kg?"),
               answer=P("44.08 lb (44.05 by ÷ 0.454)", "27.24 kg (27.22 by ÷ 2.204)", "77.14 lb (77.09 by ÷ 0.454)"), why="× the ratio whose 1 is the unit you have; the sheet's other ratio earns the point too when the work shows it",
               check=P(("eq", "20*F(2204,1000)", "F(4408,100)"), ("eq", "60*F(454,1000)", "F(2724,100)"), ("eq", "35*F(2204,1000)", "F(7714,100)")), space=0.6)
    q13 = dict(stem=P("$1\\,\\text{gal} = 3.785\\,\\text{L}$. How many liters is 5 gal?", "$1\\,\\text{gal} = 3.785\\,\\text{L}$. How many liters is 9 gal?", "$1\\,\\text{gal} = 3.785\\,\\text{L}$. How many liters is 3 gal?"),
               answer=P("18.925 L (18.94 by ÷ 0.264)", "34.065 L (34.09 by ÷ 0.264)", "11.355 L (11.36 by ÷ 0.264)"), why="more liters than gallons; the sheet's other ratio earns the point too when the work shows it",
               check=P(("eq", "5*F(3785,1000)", "F(18925,1000)"), ("eq", "9*F(3785,1000)", "F(34065,1000)"), ("eq", "3*F(3785,1000)", "F(11355,1000)")), space=0.6)
    # question 14 — a square unit ACROSS systems (7.AR.3.3 is across systems; yd² → ft² is grade 6)
    q14 = dict(stem=P("$1\\,\\text{ft} = 0.305\\,\\text{m}$. A patio is $20\\,\\text{ft}^{2}$ in area. Which is closest to its area in square meters?",
                      "$1\\,\\text{m} = 3.28\\,\\text{ft}$. A floor is $5\\,\\text{m}^{2}$ in area. Which is closest to its area in square feet?",
                      "$1\\,\\text{in} = 2.54\\,\\text{cm}$. A tile is $10\\,\\text{in}^{2}$ in area. Which is closest to its area in square centimeters?"),
               choices=P(["$6.1\\,\\text{m}^{2}$", "$0.093\\,\\text{m}^{2}$", "$1.86\\,\\text{m}^{2}$", "$12.2\\,\\text{m}^{2}$"], ["$53.8\\,\\text{ft}^{2}$", "$16.4\\,\\text{ft}^{2}$", "$10.8\\,\\text{ft}^{2}$", "$32.8\\,\\text{ft}^{2}$"], ["$25.4\\,\\text{cm}^{2}$", "$64.5\\,\\text{cm}^{2}$", "$6.45\\,\\text{cm}^{2}$", "$50.8\\,\\text{cm}^{2}$"]), correct=P(2, 0, 1), answer=P("C", "A", "B"),
               errors=P({"A": "20 × 0.305: the ratio once on a square unit [7.AR.3.3: square units square the ratio — the unit's own]", "B": "0.305² alone: the 20 ft² forgotten [4.06: finish the computation]", "D": "20 × 2 × 0.305: the ratio doubled [5.02–03 Notes II: k × k, not 2k]"},
                        {"B": "5 × 3.28: the ratio once on a square unit [7.AR.3.3: square units square the ratio — the unit's own]", "C": "3.28² alone: the 5 m² forgotten [4.06: finish the computation]", "D": "5 × 2 × 3.28: the ratio doubled [5.02–03 Notes II: k × k, not 2k]"},
                        {"A": "10 × 2.54: the ratio once on a square unit [7.AR.3.3: square units square the ratio — the unit's own]", "C": "2.54² alone: the 10 in² forgotten [4.06: finish the computation]", "D": "10 × 2 × 2.54: the ratio doubled [5.02–03 Notes II: k × k, not 2k]"}),
               why=P("20 × 0.305² = 1.8605 (or 20 ÷ 3.28² = 1.86).", "5 × 3.28² = 53.79 (or 5 ÷ 0.305² = 53.75).", "10 × 2.54² = 64.52 (or 10 ÷ 0.39² = 65.7 — the sheet's two routes differ here; either picks B)."),
               check=P(("eq", "20*F(305,1000)**2", "F(18605,10000)"), ("eq", "5*F(328,100)**2", "F(53792,1000)"), ("eq", "10*F(254,100)**2", "F(64516,1000)")))
    q15 = dict(stem=P("Rate on Nov 5: $1\\,\\text{US dollar} = 0.92\\,\\text{euros}$.", "Rate on Nov 5: $1\\,\\text{US dollar} = 1.35\\,\\text{Canadian dollars}$.", "Rate on Nov 5: $1\\,\\text{US dollar} = 1.32\\,\\text{Canadian dollars}$."),
               parts=[dict(label="a", stem=P("How many euros is \\$60?", "How many Canadian dollars is \\$70?", "How many Canadian dollars is \\$90?"),
                           answer=P("55.20 euros", "94.50 Canadian dollars", "118.80 Canadian dollars"), why="× the rate",
                           check=P(("eq", "60*F(92,100)", "F(552,10)"), ("eq", "70*F(135,100)", "F(945,10)"), ("eq", "90*F(132,100)", "F(1188,10)")), space=0.6),
                      dict(label="b", stem=P("How many US dollars is 23 euros?", "How many US dollars is 54 Canadian dollars?", "How many US dollars is 66 Canadian dollars?"),
                           answer=P("\\$25", "\\$40", "\\$50"), why=P("÷ the rate; 21.16 multiplied both ways", "÷ the rate; 72.90 multiplied both ways", "÷ the rate; 87.12 multiplied both ways"),
                           check=P(("eq", "23/F(92,100)", "25"), ("eq", "54/F(135,100)", "40"), ("eq", "66/F(132,100)", "50")), space=0.6)])
    return [q9, q10, q11, q12, q13, q14, q15]


def _ar45(form):
    P = lambda a, b, p: pick(form, a, b, p)
    q16 = dict(stem=P("A car gets 26 miles per gallon and its tank holds 15 gal.", "A car gets 22 miles per gallon and its tank holds 20 gal.", "A car gets 27 miles per gallon and its tank holds 10 gal."),
               parts=[dict(label="a", stem="How far does it go on a full tank?", answer=P("390 mi", "440 mi", "270 mi"), why="the rate × the gallons",
                           check=P(("eq", "26*15", "390"), ("eq", "22*20", "440"), ("eq", "27*10", "270")), space=0.6),
                      dict(label="b", stem=P("It makes a 1,000-mi trip. How many tanks of gas does the trip use? (Part of a tank counts as a whole tank.)",
                                             "It makes a 1,500-mi trip. How many tanks of gas does the trip use? (Part of a tank counts as a whole tank.)",
                                             "It makes a 1,200-mi trip. How many tanks of gas does the trip use? (Part of a tank counts as a whole tank.)"),
                           answer=P("3 tanks (1,000 ÷ 390 ≈ 2.56)", "4 tanks (1,500 ÷ 440 ≈ 3.41)", "5 tanks (1,200 ÷ 270 ≈ 4.44)"),
                           why="the bracket on the paper settles the rounding; follow-through on part (a)",
                           check=P(("eq", "sp.ceiling(F(1000,390))", "3"), ("eq", "sp.ceiling(F(1500,440))", "4"), ("eq", "sp.ceiling(F(1200,270))", "5")), space=0.7)])
    q17 = dict(stem=P("A recipe for 4 servings uses $1\\frac{1}{2}$ cups of rice.", "A recipe for 6 servings uses 2 cups of rice.", "A recipe for 5 servings uses 2 cups of rice."),
               parts=[dict(label="a", stem=P("How much rice for 10 servings?", "How much rice for 9 servings?", "How much rice for 15 servings?"),
                           answer=P("3¾ cups", "3 cups", "6 cups"), why=P("k = 2.5 from the yields, then the ingredient", "k = 1.5 from the yields, then the ingredient", "k = 3 from the yields, then the ingredient"),
                           check=P(("eq", "F(10,4)*F(3,2)", "F(15,4)"), ("eq", "F(9,6)*2", "3"), ("eq", "F(15,5)*2", "6")), space=0.6),
                      dict(label="b", stem=P("With 6 cups on hand, how many servings can be made?", "With 8 cups on hand, how many servings can be made?", "With 10 cups on hand, how many servings can be made?"),
                           answer=P("16 servings", "24 servings", "25 servings"), why=P("4 recipes × the yield; 24 scaled the yield by the cups", "4 recipes × the yield; 48 scaled the yield by the cups", "5 recipes × the yield; 50 scaled the yield by the cups"),
                           check=P(("eq", "6/F(3,2)*4", "16"), ("eq", "F(8,2)*6", "24"), ("eq", "F(10,2)*5", "25")), space=0.6)])
    q18 = dict(stem=P("Juice is mixed orange : mango : water = $3 : 2 : 4$. A batch uses 9 cups of orange. How many cups is the whole batch?",
                      "Paint is mixed $1 : 3 : 4$. A batch uses 12 gal of the second color. How many gallons is the whole batch?",
                      "Paint is mixed $3 : 1 : 2$. A batch uses 4 gal of the second color. How many gallons is the whole batch?"),
               answer=P("27 cups", "32 gal", "24 gal"), why=P("k = 3 from the orange, then the whole, 9 parts; 6 found the mango and stopped", "k = 4 from the second color, then the whole, 8 parts; 16 found the third color and stopped", "k = 4 from the second color, then the whole, 6 parts; 12 found the first color and stopped"),
               check=P(("eq", "9*F(9,3)", "27"), ("eq", "8*F(12,3)", "32"), ("eq", "6*F(4,1)", "24")), space=0.7)
    # question 19 — transfer item 2 on both test forms (a rate comparison across systems that ends in
    # a decision; its type was 5.10 board 9); the practice test carries a bare comparison instead
    if form == "practice":
        q19 = dict(stem="$1\\,\\text{mi} = 1.61\\,\\text{km}$. A train does 80 km/h; a bus does 45 mi/h. Which is faster? Show both speeds in one unit.",
                   answer="The train: 45 mi/h = 72.45 km/h, and 80 > 72.45.", why="Same unit first; 80 > 45 compared two units.",
                   check=("eq", "45*F(161,100)", "F(7245,100)"), space=0.9)
    else:
        q19 = dict(transfer=True,
                   stem=P("$1\\,\\text{mi} = 1.61\\,\\text{km}$. A drive is 200 km long. Car A averages 40 mi/h; car B averages 60 km/h. Which car gets there first, and by about how many minutes? Show both speeds in one unit.",
                          "$1\\,\\text{mi} = 1.61\\,\\text{km}$. A drive is 450 km long. Truck A averages 55 mi/h; truck B averages 90 km/h. Which truck gets there first, and by about how many minutes? Show both speeds in one unit.", ""),
                   answer=P("Car A, by about 14 minutes: 40 mi/h = 64.4 km/h, so 200 ÷ 64.4 ≈ 3.11 h against 200 ÷ 60 ≈ 3.33 h.",
                            "Truck B, by about 5 minutes: 55 mi/h = 88.55 km/h, so 450 ÷ 90 = 5 h against 450 ÷ 88.55 ≈ 5.08 h.", ""),
                   why=P("The point needs the speeds in one unit and the choice with its gap: 0.227 h is 13.7 min — 13 or 14 both earn it (by the sheet's 0.62 route, 124 mi: 3.1 h against 3.33 h, 14 min). 'Car B, 60 > 40' compared two units. A decision from two rates in different units appears on no review and in no question bank; its type was 5.10 board 9.",
                         "The point needs the speeds in one unit and the choice with its gap: 0.082 h is 4.9 min — 5 earns it (by the 0.62 route, 279 mi: 5 h against 5.07 h, 4 min; accept 4–5). 'Truck B, 90 > 55' is right by accident — no credit without the conversion. The surface appears on no review and in no question bank; its type was 5.10 board 9.", ""),
                   check=P(("many", ("eq", "40*F(161,100)", "F(644,10)"), ("eq", "F(200,60)", "F(10,3)"), ("true", "F(200,F(644,10)) < F(200,60)")),
                           ("many", ("eq", "55*F(161,100)", "F(8855,100)"), ("eq", "F(450,90)", "5"), ("true", "F(450,90) < F(450,F(8855,100))")), None), space=1.2)
    return [q16, q17, q18, q19]


def _sections(f):
    return [dict(title="Scale Drawings and Scale Factors", benchmark="MA.7.GR.1.5", items=_gr15(f)),
            dict(title="Converting Across Systems", benchmark="MA.7.AR.3.3", items=_ar33(f)),
            dict(title="Multi-Step Proportion Problems", benchmark="MA.7.AR.4.5", items=_ar45(f))]


U = dict(
    unit=5, title="Multi-Step Proportional Relationships",
    reference_intro="The conversion ratios on this page are printed exactly as the FAST reference sheet prints them (the grade 7 and grade 8 sheets carry the same lines), and the FAST gives you that sheet. On this unit's test you will not have it — every conversion item prints the ratio it needs. The rules around the ratios are the unit's own, and they are tested from memory.",

    reference=[
        dict(title="1.   Scale Drawings and Scale Factors", right="Lessons 1–4 · k is one number, and every length gets it",
             blocks=["**The scale factor k is copy ÷ original.**  Every corresponding length is multiplied by the same k. A copy that is smaller has k less than 1: a 10 cm side that becomes 4 cm has k = 0.4, not 2.5. Angles are not lengths and do not change.",
                     dict(table=([2600, 2200, 4560], [
                         ["What", "Multiply by", "Why"],
                         ["a length", "k", "that is what k is"],
                         ["the perimeter", "k", "a sum of lengths"],
                         ["the area", "k²", "two lengths multiplied, so k is used twice"],
                         ["an angle", "nothing", "an angle is not a length"]])),
                     "**From two areas back to k: a square root.**  Areas 20 and 180 give 180 ÷ 20 = 9 = k², so k = 3. Every area ratio on this test is a perfect square.",
                     "**A scale with two units is a rate — write it per 1 unit of drawing first.**  ¼ in : 1 ft is 1 in : 4 ft. Then drawing × rate = real, and real ÷ rate = drawing.",
                     "**Area from a plan: real dimensions first.**  A room 1.5 in by 2 in at 1 in : 6 ft is 9 ft by 12 ft, 108 ft² — never 3 in² × 6. The rate is used twice for an area, which is k² again. (With one unit, 1 in : 6 ft is 1 : 72, and 72 is the scale factor.)"]),
        dict(title="2.   The Conversion Ratios (the FAST reference sheet's)", right="Lessons 6–9 · never memorized, always printed",
             blocks=[dict(table=([3080, 3080, 3100], [
                         ["Customary → Metric", "Metric → Customary", "Inside one system"],
                         ["1 in = 2.54 cm", "1 cm = 0.39 in", "1 ft = 12 in · 1 yd = 3 ft"],
                         ["1 ft = 0.305 m", "1 m = 3.28 ft", "1 mi = 5,280 ft · 1 mi = 1,760 yd"],
                         ["1 mi = 1.61 km", "1 km = 0.62 mi", "1 c = 8 fl oz · 1 pt = 2 c"],
                         ["1 c = 0.24 L", "1 L = 4.23 c", "1 qt = 2 pt · 1 gal = 4 qt"],
                         ["1 gal = 3.785 L", "1 L = 0.264 gal", "1 lb = 16 oz · 1 ton = 2,000 lb"],
                         ["1 oz = 28.35 g", "1 g = 0.0352 oz", "1 m = 100 cm · 1 m = 1,000 mm · 1 km = 1,000 m"],
                         ["1 lb = 0.454 kg", "1 kg = 2.204 lb", "1 L = 1,000 mL · 1 kg = 1,000 g · 1 g = 1,000 mg"]]), size=10),
                     "**A conversion ratio is a form of 1.**  2.54 cm over 1 in equals 1 — the same length in two units — so multiplying by it changes the unit and not the amount. Pick the ratio whose 1 is the unit you HAVE, so that unit cancels.",
                     "**Estimate first.**  A centimeter is shorter than an inch, so 50 cm is fewer than 50 inches: 19.5, never 127. The estimate is what catches the ratio the wrong way round.",
                     "**Both directions are on the sheet, and both are accepted.**  50 cm × 0.39 = 19.5 in and 50 ÷ 2.54 = 19.7 in are both the sheet's answer. Show which ratio you used.",
                     "**Some paths take two steps.**  Yards to centimeters goes through feet and inches. Fluid ounces to liters go through cups (8 fl oz = 1 c, 1 c = 0.24 L) — there is no fluid-ounce-to-milliliter line on the sheet. An ounce (weight) and a fluid ounce (volume) are two different units."]),
        dict(title="3.   Square Units, Cubic Units, Money", right="Lessons 7 and 9 · the ratio once, twice, three times",
             blocks=[dict(table=([2200, 3300, 3760], [
                         ["Unit", "The length ratio is used", "Example"],
                         ["length (ft → in)", "once", "3 ft = 36 in"],
                         ["area (ft² → in²)", "twice: 12² = 144", "3 ft² = 432 in²"],
                         ["volume (ft³ → in³)", "three times: 12³ = 1,728", "2 ft³ = 3,456 in³"],
                         ["area (m² → cm²)", "twice: 100² = 10,000", "1 m² = 10,000 cm², not 100"],
                         ["area (ft² → m²)", "twice: 0.305² = 0.093", "20 ft² = 1.86 m² — the sheet's length ratio, squared"]])),
                     "**Money converts like length, but the rate is on the problem, not the sheet.**  An exchange rate changes daily, so it is printed and dated on the item. Dollars to euros at 0.92: multiply. Euros back to dollars: divide."]),
        dict(title="4.   Multi-Step Problems", right="Lessons 10–11 · one rate, used again; same unit first",
             blocks=["**A multi-step problem is one unit rate used more than once — name what each step finds.**  23 mi per gallon × 17.5 gal = 402.5 mi per tank; 1,207 mi ÷ 402.5 = 2.998, so 3 tanks. A part of a tank is still a tank the trip uses — the paper says so when it asks.",
                     "**Two rates in different units cannot be compared until they are in one unit.**  100 km/h × 0.62 = 62 mi/h, so 65 mi/h is faster even though 100 is the bigger number. Convert first; the answer is a sentence with both speeds in the same unit.",
                     "**A recipe scales by k = new yield ÷ old yield, and k multiplies every ingredient.**  Then answer the question that was asked: what is on hand ÷ the recipe's amount gives how many recipes, and that × the yield gives servings.",
                     "**A part-to-whole mixture: k from the part you know, then the whole.**  Paint 2 : 4 : 5 with 8 gal of white has k = 4 and 11 parts, so 44 gal."]),
        dict(title="5.   Vocabulary",
             blocks=[dict(vocab=[
                 # a term prints underlined, where math does not render: "($k$)" printed its dollar signs (25 Oct 2026); plain k, as this sheet writes it above
                 ("scale factor (k)", "the one number every length of a figure is multiplied by to make its scale copy; copy ÷ original"),
                 ("scale drawing", "a drawing whose lengths are all the real lengths × one scale factor"),
                 ("corresponding sides", "a side of the original and the side of the copy that matches it"),
                 ("scale (two units)", "a ratio such as $\\frac{1}{4}\\,\\text{in} : 1\\,\\text{ft}$ — a drawing length and the real length it stands for; read it per 1 unit of drawing"),
                 ("conversion ratio", "a pair of equal measures, such as $1\\,\\text{in} = 2.54\\,\\text{cm}$, written as a fraction that equals 1"),
                 ("customary / metric", "the inch–mile–pound–gallon system; the centimeter–kilometer–kilogram–liter system"),
                 ("exchange rate", "how much of one currency one unit of another buys; set by someone, printed on the problem"),
                 ("fluid ounce", "a volume ($8\\,\\text{fl oz} = 1\\,\\text{c}$); the ounce on a scale is a weight ($16\\,\\text{oz} = 1\\,\\text{lb}$) — two units that share a word"),
                 ("square units / cubic units", "an area, which uses the length ratio twice; a volume, which uses it three times"),
                 ("unit rate", "how much of one quantity per 1 of the other — 23 miles per gallon"),
                 ("proportional", "two quantities whose ratio stays the same: double one and the other doubles")])]),
    ],

    # ------------------------------------------------------------------ unit review (unscored; home Tue 3 Nov, key Wed)
    review=[
        dict(letter="A", title="Scale Drawings", lessons="Lesson 1", benchmark="MA.7.GR.1.5", items=[
            dict(stem="A 5 cm side of a figure is 8 cm in its scale copy. Find the scale factor.", answer="k = 1.6", why="copy ÷ original", check=("eq", "F(8,5)", "F(8,5)"), space=0.6),
            dict(stem="A 16 cm side of a figure is 4 cm in its scale copy. Find the scale factor.", answer="k = 0.25", why="the copy is smaller, so k is under 1", check=("eq", "F(4,16)", "F(1,4)"), space=0.6),
            dict(stem="A scale copy is made at $k = 1.5$. A side of the original is 6 cm. Find the matching side of the copy.", answer="9 cm", why="", check=("eq", "6*F(3,2)", "9"), space=0.6),
            dict(stem="A drawing has a 65° angle. Its scale copy is made at $k = 2$. What is the matching angle in the copy?",
                 choices=["32.5°", "67°", "130°", "65°"], correct=3, answer="D",
                 errors={"A": "the angle divided by k [7.GR.1.5]", "B": "k added to the angle [7.GR.1.5: the additive error — Math Nation's named misconception]", "C": "the angle multiplied by k [7.GR.1.5: lengths scale, angles do not]"},
                 why="", check=("eq", "65", "65")),
            dict(stem="A map is drawn at $1\\,\\text{cm} : 30\\,\\text{km}$. Two towns are 4.5 cm apart on it. How far apart are they?", answer="135 km", why="drawing × rate", check=("eq", "F(9,2)*30", "135"), space=0.6),
        ]),
        dict(letter="B", title="Scale Factor: Perimeter and Area", lessons="Lessons 2–3", benchmark="MA.7.GR.1.5", items=[
            dict(stem="A figure with perimeter 16 cm is scaled by $k = 2.5$. Find the copy's perimeter.", answer="40 cm", why="perimeter × k", check=("eq", "16*F(5,2)", "40"), space=0.6),
            dict(stem="A figure with area $9\\,\\text{cm}^{2}$ is scaled by $k = 2.5$. Find the copy's area.", answer="56.25 cm²", why="area × k² = 9 × 6.25", check=("eq", "9*F(25,4)", "F(225,4)"), space=0.6),
            dict(stem="A 4 cm by 6 cm rectangle is scaled by $k = \\frac{1}{2}$.", parts=[
                dict(label="a", stem="Find the copy's perimeter.", answer="10 cm", why="20 × ½", check=("eq", "2*(4+6)*F(1,2)", "10"), space=0.5),
                dict(label="b", stem="Find the copy's area.", answer="6 cm²", why="24 × ¼", check=("eq", "4*6*F(1,4)", "6"), space=0.5)]),
            dict(stem="A figure has area $10\\,\\text{cm}^{2}$ and its scale copy has area $160\\,\\text{cm}^{2}$. Find $k$.", answer="k = 4", why="160 ÷ 10 = 16 = k²", check=("eq", "sqrt(F(160,10))", "4"), space=0.6),
            dict(stem="A figure's perimeter is 12 cm and its copy's perimeter is 36 cm. What is the area ratio, copy to original?", answer="9", why="k = 3 from the perimeters; the area ratio is k²", check=("eq", "(F(36,12))**2", "9"), space=0.6),
            dict(stem="Sam says tripling every side of a rectangle triples its area. Explain why not, with a counterexample.",
                 answer="A 2 by 5 (area 10) tripled is 6 by 15 (area 90): nine times, because area is two lengths and each is tripled.", why="the reason and the numbers", check=("eq", "F(6*15, 2*5)", "9"), space=1.0),
        ]),
        dict(letter="C", title="Real-World Scale Drawings", lessons="Lesson 4", benchmark="MA.7.GR.1.5", items=[
            dict(stem="A plan is drawn at $\\frac{1}{2}\\,\\text{in} : 1\\,\\text{ft}$. A wall is 7.5 in long on it. Find the real length.", answer="15 ft", why="1 in : 2 ft; 7.5 × 2", check=("eq", "F(15,2)*2", "15"), space=0.6),
            dict(stem="A plan is drawn at $1\\,\\text{in} : 6\\,\\text{ft}$. A real wall is 21 ft long. Find its length on the plan.", answer="3.5 in", why="real ÷ rate", check=("eq", "F(21,6)", "F(7,2)"), space=0.6),
            dict(stem="A model boat is built at $1 : 25$ and is 32 cm long. Find the real boat's length in meters.", answer="8 m", why="32 × 25 = 800 cm", check=("eq", "F(32*25,100)", "8"), space=0.6),
            dict(stem="Every part below is about one floor plan drawn at $\\frac{1}{4}\\,\\text{in} : 1\\,\\text{ft}$, on which a room is 3 in by 4 in. $1\\,\\text{ft} = 0.305\\,\\text{m}$.",
                 key_stem="**SSDD.**   Every part below is about one floor plan drawn at ¼ in : 1 ft, on which a room is 3 in by 4 in. 1 ft = 0.305 m.  Same surface, four different questions: a length, an area with the rate used twice, the scale factor as one number, and a length conversion — the four moves of the unit on one room, so that a student learns to read the question and not the picture.",
                 parts=[
                     dict(label="a", stem="Find the real length of the wall drawn 3 in long.", answer="12 ft", why="1 in : 4 ft; 3 × 4", check=("eq", "3*4", "12"), space=0.5),
                     dict(label="b", stem="Find the room's real area.", answer="192 ft²", why="12 by 16; the rate used twice", check=("eq", "12*16", "192"), space=0.5),
                     dict(label="c", stem="Write the scale factor from the drawing to the room as a single number.", answer="48", why="1 in : 4 ft is 1 in : 48 in", check=("eq", "4*12", "48"), space=0.5),
                     dict(label="d", stem="Find the room's real perimeter in meters.", answer="17.08 m", why="2(12 + 16) = 56 ft; 56 × 0.305 (56 ÷ 3.28 = 17.07 by the other ratio). The area in square meters is the test's transfer item and is not rehearsed here (ruling 18).", check=("eq", "2*(12+16)*F(305,1000)", "F(1708,100)"), space=0.7)]),
        ]),
        dict(letter="D", title="Converting Length Across Systems; Currency", lessons="Lessons 6–7", benchmark="MA.7.AR.3.3", items=[
            dict(stem="$1\\,\\text{in} = 2.54\\,\\text{cm}$. How many centimeters is 14 in?", answer="35.56 cm", why="", check=("eq", "14*F(254,100)", "F(3556,100)"), space=0.6),
            dict(stem="$1\\,\\text{cm} = 0.39\\,\\text{in}$. How many inches is 120 cm?", answer="46.8 in (47.2 by ÷ 2.54)", why="fewer inches than centimeters", check=("eq", "120*F(39,100)", "F(468,10)"), space=0.6),
            dict(stem="$1\\,\\text{km} = 0.62\\,\\text{mi}$. How many miles is 30 km?", answer="18.6 mi", why="", check=("eq", "30*F(62,100)", "F(186,10)"), space=0.6),
            dict(stem="$1\\,\\text{yd} = 3\\,\\text{ft}$, $1\\,\\text{ft} = 12\\,\\text{in}$, $1\\,\\text{in} = 2.54\\,\\text{cm}$. How many centimeters is 6 yd? Estimate first.", answer="About 540; exactly 548.64 cm", why="216 in × 2.54", check=("eq", "216*F(254,100)", "F(54864,100)"), space=0.8),
            dict(stem="Rate on Nov 3: $1\\,\\text{US dollar} = 0.92\\,\\text{euros}$.", parts=[
                dict(label="a", stem="How many euros is \\$150?", answer="138 euros", why="× the rate", check=("eq", "150*F(92,100)", "138"), space=0.5),
                dict(label="b", stem="How many US dollars is 69 euros?", answer="\\$75", why="÷ the rate", check=("eq", "69/F(92,100)", "75"), space=0.5)]),
            dict(stem="$1\\,\\text{in} = 2.54\\,\\text{cm}$; $1\\,\\text{cm} = 0.39\\,\\text{in}$. Lee converts 40 cm to inches by multiplying by 2.54 and gets 101.6 in. Name the error and fix it.",
                 answer="Lee used the ratio whose 1 is inches on centimeters. Inches are bigger, so there are fewer: 40 × 0.39 = 15.6 in (or 40 ÷ 2.54 = 15.7).", why="the error named and the estimate", check=("eq", "40*F(39,100)", "F(156,10)"), space=1.0),
        ]),
        dict(letter="E", title="Converting Mass, Area and Volume", lessons="Lessons 8–9", benchmark="MA.7.AR.3.3", items=[
            dict(stem="$1\\,\\text{lb} = 0.454\\,\\text{kg}$. How many kilograms is 80 lb?", answer="36.32 kg", why="(80 ÷ 2.204 = 36.30 by the other ratio)", check=("eq", "80*F(454,1000)", "F(3632,100)"), space=0.6),
            dict(stem="$1\\,\\text{L} = 0.264\\,\\text{gal}$. How many gallons is 40 L?", answer="10.56 gal", why="", check=("eq", "40*F(264,1000)", "F(1056,100)"), space=0.6),
            dict(stem="$1\\,\\text{ft} = 0.305\\,\\text{m}$. How many square meters is $8\\,\\text{ft}^{2}$? (Round to two places.)", answer="About 0.74 m²", why="8 × 0.305² = 0.7442: the sheet's length ratio, squared", check=("eq", "8*F(305,1000)**2", "F(7442,10000)"), space=0.7),
            dict(stem="$1\\,\\text{c} = 8\\,\\text{fl oz}$ and $1\\,\\text{c} = 0.24\\,\\text{L}$. How many liters is 48 fl oz?", answer="1.44 L", why="6 c × 0.24", check=("eq", "6*F(24,100)", "F(144,100)"), space=0.6),
            dict(stem="$1\\,\\text{m} = 3.28\\,\\text{ft}$. A desk is $1.5\\,\\text{m}^{2}$ in area. Which is closest to its area in square feet?",
                 choices=["$4.9\\,\\text{ft}^{2}$", "$9.8\\,\\text{ft}^{2}$", "$16.1\\,\\text{ft}^{2}$", "$10.8\\,\\text{ft}^{2}$"], correct=2, answer="C",
                 errors={"A": "1.5 × 3.28: the ratio once [7.AR.3.3: square units square the ratio — the unit's own]", "B": "1.5 × 2 × 3.28: the ratio doubled [5.02–03 Notes II]", "D": "3.28² alone: the 1.5 m² forgotten [4.06: finish the computation]"},
                 why="1.5 × 3.28² = 16.1376.", check=("eq", "F(3,2)*F(328,100)**2", "F(161376,10000)")),
        ]),
        dict(letter="F", title="Multi-Step Proportion Problems", lessons="Lessons 10–11", benchmark="MA.7.AR.4.5", items=[
            dict(stem="A car gets 29 miles per gallon and its tank holds 12 gal.", parts=[
                dict(label="a", stem="How far does it go on a full tank?", answer="348 mi", why="", check=("eq", "29*12", "348"), space=0.5),
                dict(label="b", stem="It starts an 800-mi trip with a full tank. How many tanks of gas does the trip take?", answer="3 tanks (800 ÷ 348 ≈ 2.3)", why="a part of a tank is still a tank", check=("eq", "sp.ceiling(F(800,348))", "3"), space=0.6)]),
            dict(stem="A recipe for 3 servings uses $1\\frac{1}{4}$ cups of rice.", parts=[
                dict(label="a", stem="How much rice for 12 servings?", answer="5 cups", why="k = 4", check=("eq", "F(12,3)*F(5,4)", "5"), space=0.5),
                dict(label="b", stem="With 10 cups on hand, how many servings can be made?", answer="24 servings", why="8 recipes × 3", check=("eq", "10/F(5,4)*3", "24"), space=0.5)]),
            dict(stem="$1\\,\\text{km} = 0.62\\,\\text{mi}$. A train does 110 km/h; a bus does 65 mi/h. Which is faster? Show both speeds in one unit.", answer="The train: 110 km/h = 68.2 mi/h > 65 mi/h", why="same unit first", check=("eq", "110*F(62,100)", "F(682,10)"), space=0.8),
            dict(stem="Paint is mixed $1 : 2 : 5$. A batch uses 10 gal of the third color. How many gallons is the whole batch?", answer="16 gal", why="k = 2; 8 parts × 2", check=("eq", "8*F(10,5)", "16"), space=0.6),
        ]),
    ],

    # ------------------------------------------------------------------ unit assessment (Form A, Form B, practice)
    assessment=dict(
        total=24,
        tracker_order=["MA.7.GR.1.5", "MA.7.AR.3.3", "MA.7.AR.4.5"],
        tracker={"MA.7.GR.1.5": 10, "MA.7.AR.3.3": 8, "MA.7.AR.4.5": 6},
        follow_through="Follow-through (ruling 19).  A later part is correct when the right operation is applied to the student's own earlier value: question 16(b) from their own 16(a), question 6(b) from their own 6(a). Look at what they wrote for the earlier part, do this part's operation to it, and tick if that is what they wrote.",
        forms={"A": _sections("A"), "B": _sections("B"), "practice": _sections("practice")},
    ),
)
