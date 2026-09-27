const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, AlignmentType,
        BorderStyle, LevelFormat, PageBreak, Footer, PageNumber } = require("docx");
const NAVY = "1F3864", GREY = "595959", FONT = "Arial", W = 12240 - 2 * 1000;
const r = (t, o = {}) => new TextRun({ text: t, font: FONT, size: o.size || 19, bold: o.bold, italics: o.italics, color: o.color });
const kids = (x, o) => Array.isArray(x) ? x : [r(x, o)];
const P = (x, o = {}) => new Paragraph({ children: kids(x, o), spacing: { before: o.before ?? 0, after: o.after ?? 80, line: 264 }, alignment: o.align, keepNext: o.keepNext });
const B = (x, lvl = 0) => new Paragraph({ numbering: { reference: "b", level: lvl }, spacing: { after: 50, line: 256 }, children: kids(x) });
const H = (t, o = {}) => new Paragraph({ keepNext: true, spacing: { before: o.before ?? 200, after: 80 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: NAVY, space: 2 } }, children: [r(t, { bold: true, size: 23, color: NAVY })] });
const SUB = (t) => P([r(t, { bold: true, size: 20 })], { before: 100, after: 40, keepNext: true });
const bd = { style: BorderStyle.SINGLE, size: 4, color: "7F7F7F" };
const borders = { top: bd, bottom: bd, left: bd, right: bd, insideHorizontal: bd, insideVertical: bd };
const cell = (content, w, o = {}) => new TableCell({ width: { size: w, type: WidthType.DXA }, margins: { top: 70, bottom: 70, left: 100, right: 100 },
  shading: o.fill ? { type: ShadingType.CLEAR, color: "auto", fill: o.fill } : undefined,
  children: (Array.isArray(content) && content.length && content[0] instanceof Paragraph) ? content : [P(content, { after: 0, ...o })] });
const table = (widths, rows, head) => new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: widths, borders,
  rows: rows.map((row, i) => new TableRow({ cantSplit: true, tableHeader: head && i === 0,
    children: row.map((c, j) => cell(c, widths[j], head && i === 0 ? { fill: "DCE3F0", bold: true } : {})) })) });
const hb = (t) => r(t, { bold: true });

const doc = new Document({
  creator: "Mr. Shaffer", title: "Essential Benchmark Learning Plan — MA.7.AR.2.2",
  styles: { default: { document: { run: { font: FONT, size: 19 } } } },
  numbering: { config: [{ reference: "b", levels: [
    { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 340, hanging: 220 } } } },
    { level: 1, format: LevelFormat.BULLET, text: "–", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 680, hanging: 220 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 900, bottom: 900, left: 1000, right: 1000 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [r("Essential Benchmark Learning Plan · MA.7.AR.2.2 · page ", { size: 16, color: GREY }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: GREY })] })] }) },
    children: [
      P([r("Essential Benchmark Learning Plan", { bold: true, size: 34, color: NAVY })], { align: AlignmentType.CENTER, after: 40 }),
      P([hb("Grade Level/Content Area:  "), r("Grade 7 Mathematics (M/J Grade 7 Mathematics, course 1205040)")], { align: AlignmentType.CENTER, after: 120 }),
      table([W / 3, W / 3, W / 3], [[[hb("Number of Days:  "), r("11")], [hb("Start Date:  "), r("Tue, Oct 13, 2026")], [hb("End Date:  "), r("Tue, Oct 27, 2026")]]]),

      H("Essential Grade Level Benchmark", { before: 160 }),
      P([hb("MA.7.AR.2.2 "), r("— Write and solve two-step equations in one variable within a mathematical or real-world context, where all terms are rational numbers.")]),
      B([hb("Clarification 1: "), r("Instruction focuses the application of the properties of equality. Refer to Properties of Operations, Equality and Inequality (Appendix D).")]),
      B([hb("Clarification 2: "), r("Instruction includes equations in the forms px ± q = r and p(x ± q) = r, where p, q and r are specific rational numbers.")]),
      B([hb("Clarification 3: "), r("Problems include linear equations where the variable may be on either side of the equal sign.")]),
      P([r("District placement: Quarter 2 essential benchmark; supporting benchmark MA.7.AR.2.1 (district Scope & Sequence Guidance).", { italics: true, color: GREY, size: 18 })], { before: 40 }),

      H("Previous and Next Grade Level Benchmarks (most closely aligned)"),
      table([W / 2, W / 2], [
        [[hb("Previous Grade Level Benchmark most closely aligned")], [hb("Next Grade Level Benchmark most closely aligned")]],
        [[P([hb("MA.6.AR.2.2 "), r("— Write and solve one-step equations in one variable within a mathematical or real-world context using addition and subtraction, where all terms and solutions are integers.")]),
          P([hb("MA.6.AR.2.3 "), r("— Write and solve one-step equations in one variable within a mathematical or real-world context using multiplication and division, where all terms and solutions are integers.")]),
          P([r("Both are listed as previous benchmarks in the B1G-M. A two-step equation joins them: one addition/subtraction step and one multiplication/division step, now with rational (not just integer) terms and solutions.", { italics: true, size: 18 })], { after: 0 })],
         [P([hb("MA.8.AR.2.1 "), r("— Solve multi-step linear equations in one variable, with rational number coefficients. Include equations with variables on both sides.")]),
          P([r("Clarification: problem types include one-variable linear equations that generate one solution, infinitely many solutions or no solution.", { size: 18 })]),
          P([r("The B1G-M also lists MA.8.AR.2.3 (x² = p and x³ = q) as a next benchmark; MA.8.AR.2.1 is the direct continuation: two steps become multi-step, and variables appear on both sides.", { italics: true, size: 18 })], { after: 0 })]],
      ]),

      H("Common Understanding About the Essential Benchmark"),
      SUB("Key verbs"),
      B([hb("Write: "), r("translate a mathematical or real-world situation into a two-step equation in one variable: define the variable and identify the coefficient and the constant.")]),
      B([hb("Solve: "), r("find the value of the variable that makes the equation true by applying the properties of equality (Clarification 1). Students verbalize or write the Property of Operations or Property of Equality used at each step (B1G-M).")]),
      SUB("Key concepts and vocabulary"),
      B("Terms from the K-12 Glossary named in the B1G-M: equation, rational number."),
      B("Also: variable, coefficient, constant, term, solution, inverse operations, Addition/Subtraction/Multiplication/Division Properties of Equality, Distributive Property (Appendix D)."),
      B("The two forms (Clarification 2): px ± q = r and p(x ± q) = r, where p, q and r are specific rational numbers: integers, fractions and decimals, positive or negative. The variable may be on either side of the equal sign (Clarification 3), e.g. r = px + q."),
      B("A “two-step” equation needs two inverse operations to isolate the variable. For p(x ± q) = r the order is not fixed: in 4(x + 7) = 12, students may divide both sides by 4 or use the Distributive Property first. Both are correct (B1G-M, MTR.3.1)."),
      SUB("What proficiency looks like"),
      P("A proficient student, in or out of context, writes a two-step equation for a situation, solves it using the properties of equality, justifies each step, and checks the solution. This works in both forms, with rational numbers, with the variable on either side. The student can also explain what the solution means in the situation."),
      SUB("Notes from the FAST Item Specifications (Grade 7 Mathematics, FLDOE draft, August 2023)"),
      B([hb("Assessment limits: "), r("items will require the student to write an equation, solve an equation, or write and solve an equation. Equations are represented in the form px ± q = r or p(x ± q) = r.")]),
      B([hb("Context: "), r("both (items appear with and without a context).  "), hb("Calculator: "), r("available.")]),
      B([hb("Reporting category: "), r("Number Sense and Operations and Algebraic Reasoning, 25–31% of the Grade 7 FAST (36–40 items). It is shared with MA.7.NSO.1.1, 1.2, 2.1, 2.2, 2.3, MA.7.AR.1.2 (which also assesses MA.7.AR.1.1) and MA.7.AR.2.1 (FAST Test Design Summary and Blueprint, updated Feb. 5, 2025).")]),
      SUB("Notes from the Performance Level Descriptors (FLDOE Reporting Category Statements, May 2024, built from the Achievement Level Descriptions)"),
      B([hb("Below expectations: "), r("“Solve one-step inequalities and two-step equations with all positive integers or one rational number.”")]),
      B([hb("At/near expectations: "), r("“Write and solve one-step inequalities and two-step equations with rational numbers in the same form.”")]),
      B([hb("Above expectations: "), r("“Write and solve one-step inequalities and two-step equations and interpret the solution in context of the situation presented.”")]),
      P([r("What moves a student up: from integers to rational numbers, and from solving to writing and interpreting in context.", { italics: true, size: 18 })]),
      SUB("Common misconceptions or errors (B1G-M)"),
      B("Using the addition or subtraction property of equality on the same side of the equal sign. Address with balances, algebra tiles or bar diagrams that show the two sides staying balanced (MTR.2.1)."),
      B("Misidentifying the constants and the coefficients within a real-world context."),
      B([r("Team note (classroom experience, not from the B1G-M): distributing to only the first term, e.g. rewriting 4(x + 7) as 4x + 7.", { italics: true })]),
      SUB("Supporting standards that could also be taught during this plan"),
      B([hb("MA.7.AR.2.1 "), r("(district-listed supporting benchmark) — Write and solve one-step inequalities in one variable within a mathematical context and represent solutions algebraically or graphically.")]),
      B([hb("MA.7.NSO.2 "), r("— operations with rational numbers (B1G-M horizontal alignment): the arithmetic every step depends on.")]),
      B([hb("MA.7.AR.1.1 "), r("— properties of operations with linear expressions (the Distributive Property behind p(x ± q) = r); district Q1 essential benchmark.")]),
      B([hb("Contexts named in the B1G-M: "), r("MA.7.AR.3 (percent problems), MA.7.AR.4.5 (proportional relationships), MA.7.GR.2.2 and MA.7.GR.2.3 (surface area and volume of cylinders).")]),
      B([hb("MTRs (B1G-M): "), r("MTR.2.1 (represent problems in multiple ways: tiles, bar diagrams, balances), MTR.3.1 (fluency; choose efficient steps), MTR.5.1 (patterns and structure), MTR.7.1 (real-world contexts), plus MTR.1.1 and MTR.6.1 in the instructional tasks.")]),

      H("Learning Targets"),
      P([r("Progression from least to most complex; LT6 is the benchmark in its entirety. Vetted with an educator lens against the benchmark, the clarifications, the item specifications and the B1G-M.", { italics: true, size: 18 })]),
      table([Math.round(W * 0.44), Math.round(W * 0.34), W - Math.round(W * 0.44) - Math.round(W * 0.34)], [
        ["Learning Targets in Progression of Learning", "Assessment", "Timeline"],
        [[hb("LT1: "), r("I can identify the variable, the coefficient and the constant in a two-step equation or a real-world situation, and model the equation with algebra tiles, a bar diagram or a balance.")], "Exit ticket (informal check)", "1 day: Day 1, Tue Oct 13"],
        [[hb("LT2: "), r("I can solve two-step equations in the form px ± q = r with integers by using the properties of equality, name the property I use at each step, and check my answer.")], "Exit ticket", "1 day: Day 2, Wed Oct 14 (43-min period)"],
        [[hb("LT3: "), r("I can solve two-step equations in the form px ± q = r when the numbers are fractions, decimals or negatives, including when the variable is on the right side of the equal sign.")],
         [P([hb("CFA 1 "), r("(end of Day 4), covering LT1–LT3. Five items: identify the coefficient and constant in a context; three solve items (integers; fractions or decimals; variable on the right); one error analysis on the “same side of the equal sign” misconception. Scored on the proficiency scale below.")], { after: 40 }), P([r("Link CFA 1: ________________", { italics: true, color: GREY })], { after: 0 })],
         "2 days: Days 3–4, Thu Oct 15 – Fri Oct 16 (CFA 1 on Fri)"],
        [[hb("LT4: "), r("I can solve two-step equations in the form p(x ± q) = r by dividing first or by using the Distributive Property first, and explain which way is more efficient.")], "Exit ticket",
         "1 day: Day 5, Mon Oct 19. Team meets on CFA 1 data; response day is Day 6, Tue Oct 20."],
        [[hb("LT5: "), r("I can write a two-step equation for a real-world or mathematical situation and tell what my variable stands for.")], "Exit ticket", "1 day: Day 7, Wed Oct 21 (43-min period)"],
        [[hb("LT6 (full benchmark): "), r("I can write and solve two-step equations in one variable within a mathematical or real-world context, where all terms are rational numbers, and explain what my solution means.")],
         [P([hb("CSA "), r("(Day 10), covering LT1–LT6 and built to the FAST item specifications: write, solve, and write-and-solve items; both forms; with and without context; variable on either side; rational terms; calculator available. Scored on the proficiency scale.")], { after: 40 }), P([r("Link CSA: ________________", { italics: true, color: GREY })], { after: 0 })],
         "1 day + review + CSA + response: Day 8 Thu Oct 22 (LT6), Day 9 Fri Oct 23 (review), Day 10 Mon Oct 26 (CSA), Day 11 Tue Oct 27 (response day after the team meets on CSA data)"],
      ], true),
      SUB("Proficiency scale (for CFA 1 and the CSA)"),
      table([Math.round(W * 0.16), W - Math.round(W * 0.16)], [
        ["Level", "The student can…"],
        [[hb("4  Exceeds")], "Everything in Level 3, and interprets the solution in the context of the situation (FLDOE “above”). Justifies each step with a property, and compares solution strategies for p(x ± q) = r (MTR.3.1)."],
        [[hb("3  Proficient")], "Write and solve two-step equations in one variable in the forms px ± q = r and p(x ± q) = r, where all terms are rational numbers, with or without a context and with the variable on either side (the benchmark; FLDOE “at/near”: rational numbers in the same form)."],
        [[hb("2  Developing")], "Solve two-step equations with all positive integers or with one rational number (FLDOE “below”); writes an equation for a context with support."],
        [[hb("1  Beginning")], "With support, identify the parts of an equation and solve one-step equations (MA.6.AR.2.2 and MA.6.AR.2.3)."],
      ], true),

      H("Proficiency Calendar"),
      table([900, 2300, W - 900 - 2300 - 2300, 2300], [
        ["Day", "Date", "Learning target / focus", "Assessment"],
        ["1", "Tue Oct 13", "LT1: parts of an equation; model with algebra tiles, bar diagrams, balances", "Exit ticket"],
        ["2", "Wed Oct 14 (43 min)", "LT2: solve px ± q = r with integers; name each property; check", "Exit ticket"],
        ["3", "Thu Oct 15", "LT3: rational coefficients and constants; variable on either side", "Exit ticket"],
        ["4", "Fri Oct 16", "LT3 practice", "CFA 1 (LT1–LT3)"],
        ["5", "Mon Oct 19", "LT4: p(x ± q) = r, divide first or distribute first. Team meets on CFA 1 data.", "Exit ticket"],
        ["6", "Tue Oct 20", "Response day (CFA 1): regroup to reteach LT2–LT3 or extend", "Re-check on missed LT"],
        ["7", "Wed Oct 21 (43 min)", "LT5: write two-step equations from situations (three-read strategy)", "Exit ticket"],
        ["8", "Thu Oct 22", "LT6: write and solve in context; explain what the solution means", "Exit ticket"],
        ["9", "Fri Oct 23", "Review: mixed practice in the FAST shape (write / solve / both; both forms; with and without context)", "Practice, not graded"],
        ["10", "Mon Oct 26", "Common summative assessment. Team meets on CSA data.", "CSA (LT1–LT6)"],
        ["11", "Tue Oct 27", "Response day (CSA): targeted reteach and reassessment below Level 3; extension at Level 3–4", "Reassessment"],
      ], true),

      H("SMART Goal for the Essential Benchmark Learning"),
      P("By Tuesday, October 27, 2026, at least 80% of our Grade 7 Mathematics students will score Level 3 (proficient) or higher on the MA.7.AR.2.2 common summative assessment, as measured by our common proficiency scale. Students scoring below Level 3 will get targeted support on the response day and through Tier 2 intervention, and will be reassessed, so that 100% of students show proficiency on MA.7.AR.2.2 by the end of the school year."),
      P([r("Checkpoint: CFA 1 on Oct 16 shows who needs support before the CSA. The 80% figure is a proposal for the team to confirm.", { italics: true, size: 18 })]),

      H("List of Potential Resources & Activities"),
      table([Math.round(W * 0.2), W - Math.round(W * 0.2)], [
        ["Purpose", "Resource / activity"],
        [[hb("Core instruction")], [B("Math Nation Grade 7, Unit 10, Sections 5–10 (the district Scope & Sequence Guidance maps MA.7.AR.2.2 here): videos, workbook and Test Yourself practice."),
          B("B1G-M Grade 7 (FLDOE), MA.7.AR.2.2, pp. 37–40: the algebra-tile model 2x − 3 = −11, the bar diagram 2x − 10 = −26 and the balance 3x + 4 = −11 (solutions −4, −8, −5); the “avoid a particular order” comparison 4(x + 7) = 12 (x = −4)."),
          B("Students state the property of equality used at each step (Appendix D).")]],
        [[hb("Formative (state)")], [B("CPALMS MA.7.AR.2.2 formative assessments (MFAS): Solve Equations; Write and Solve an Equation; Squares; Algebra or Arithmetic? — cpalms.org/PreviewStandard/Preview/15463"),
          B("CPALMS Original Student Tutorials: Professor E. Qual, Parts 1 and 2 (two-step equations and rational numbers).")]],
        [[hb("Practice")], [B("IXL: Solve two-step equations: complete the solution (X2L); Which x satisfies an equation? (DJS); Solve two-step equations using algebra tiles (R9E); Solve two-step equations without parentheses (CMX); Solve equations of the form px + q = r with fractions (Y6Q); Solve two-step equations with parentheses (NSH); Solve equations of the form p(x + q) = r with fractions (A8D); Solve two-step equations with integers (QEB); Choose two-step equations: word problems (8NH); Solve two-step equations: word problems (D2Y)."),
          B("FAST Grade 7 Mathematics Sample Test Materials (FLDOE) for item format: flfast.org")]],
        [[hb("Intervention (Tier 2/3)")], [B("B1G-M tiered-instruction strategies: an interactive equation balance and manipulatives; co-solving with algebra tiles before writing the equation; co-writing an equation without solving it; the three-read strategy; laminated question cards (What do you know? What is the problem asking? Can you draw a model?)."),
          B("Reteach prerequisites: one-step equations (MA.6.AR.2.2, MA.6.AR.2.3) and rational-number operations (MA.7.NSO.2)."),
          B("Access points (students on access courses): MA.7.AR.2.AP.2a, set up two-step equations in one variable based on real-world problems; MA.7.AR.2.AP.2b, solve two-step equations in one variable based on real-world problems where all terms have positive integer coefficients.")]],
        [[hb("Extension")], [B("B1G-M Instructional Task 1 (plumber: materials $341.25, total $424.09, $20.71 per hour; answer: 4 hours) and Task 2 (rectangle whose length is twice its width, perimeter 45 ft; width 7.5 ft)."),
          B("B1G-M Instructional Items: 7/9 = (2/3)x − 7 (x = 35/3) and 5.6(3z − 2) = 11 (z = 37/28 ≈ 1.32)."),
          B("Interpret solutions in context and compare strategies for p(x ± q) = r (Level 4).")]],
        [[hb("Multilingual learners")], [B("Word bank with visuals: equation, variable, coefficient, constant, term, solution, property of equality, Distributive Property (tile and balance pictures)."),
          B("Sentence frames: “First I ___ both sides by ___ because ___.”  “The coefficient is ___; it means ___.”  “My solution means ___.”"),
          B("Three-read strategy with partner talk; bar diagrams and algebra tiles as non-verbal ways to show thinking (B1G-M); pre-teach context words (total, per, fee, each); bilingual word-to-word dictionary during instruction as permitted.")]],
      ], true),

      H("Notes from Team Discussion"),
      P([r("Discussion points and decisions to confirm at the meeting:", { italics: true })]),
      B("Common language: the property names students write at each step (Addition, Subtraction, Multiplication, Division Property of Equality; Distributive Property), and one agreed layout for showing work."),
      B("Calculator use on CFA 1 and the CSA. FAST makes a calculator available for this benchmark; decide whether CFA 1 is calculator-free to see rational-number fluency."),
      B("Proficiency: agree on how each CFA and CSA item maps to the scale (Level 3 = proficient) and score 2–3 papers together before splitting the stack."),
      B("CFA 1 data meeting by Mon Oct 19 and CSA data meeting by Tue Oct 27. Plan the response-day groups: reteach with balances and tiles (LT2), rational-number practice (LT3), extension tasks (Level 3–4)."),
      B("Which intervention students get Tier 2 time, and when reassessment happens."),
      P([r("Notes: ", { bold: true }), r("______________________________________________________________________________")], { before: 80 }),

      H("Reflection on Implementation / Notes for Next Year"),
      P([r("Complete after the CSA (Oct 27):", { italics: true })]),
      B("Percent at Level 3 or higher on CFA 1 ____ % and on the CSA ____ % (goal: 80%). Did we meet the SMART goal?"),
      B("Which learning target had the lowest mastery? Which misconception persisted (same-side properties, coefficient versus constant, distributing)?"),
      B("Did the 11-day timeline hold? Where did we need more or less time, and did the two 43-minute Wednesdays matter?"),
      B("Which models (tiles, bar diagrams, balances) and resources worked best, and what would we change next year? The district map will be built around next year's textbook."),
      P([r("Notes: ", { bold: true }), r("______________________________________________________________________________")], { before: 80 }),

      H("State documents used"),
      B("Florida’s B.E.S.T. Standards for Mathematics (FLDOE): MA.7.AR.2.2, MA.7.AR.2.1, MA.6.AR.2.2, MA.6.AR.2.3, MA.8.AR.2.1, with clarifications."),
      B("B.E.S.T. Instructional Guide for Mathematics (B1G-M), Grade 7, MA.7.AR.2.2, pp. 37–40."),
      B("FAST Grade 7 Mathematics Test Item Specifications (draft, August 2023)."),
      B("Test Design Summary and Blueprint: FAST Mathematics and B.E.S.T. EOCs (updated Feb. 5, 2025)."),
      B("Reporting Category Statements, B.E.S.T. Standards: Mathematics (May 2024), built from the Achievement Level Descriptions."),
      B("CPALMS, MA.7.AR.2.2 (access points and resources); Grade 7 Mathematics course description (1205040); Lake County Schools Scope & Sequence Guidance, M/J Grade 7 Mathematics."),
    ] }] });
Packer.toBuffer(doc).then(b => { fs.writeFileSync("Essential Benchmark Learning Plan - MA.7.AR.2.2.docx", b); console.log("built"); });
