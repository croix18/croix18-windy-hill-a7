const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
        AlignmentType, BorderStyle, LevelFormat, HeadingLevel } = require("docx");

const NAVY = "1F3864", GREY = "595959", FONT = "Arial";
const W = 12240 - 2 * 1080;                          // US Letter, 0.75" margins -> 10080 DXA of text width
const run = (text, o = {}) => new TextRun({ text, font: FONT, size: o.size || 20, bold: o.bold, italics: o.italics,
                                            color: o.color, highlight: o.highlight });
const para = (children, o = {}) => new Paragraph({ children: Array.isArray(children) ? children : [run(children, o)],
                                                   spacing: { after: o.after ?? 100, before: o.before ?? 0, line: 276 },
                                                   alignment: o.align, border: o.border, keepNext: o.keepNext });
const h2 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true,
                                     spacing: { before: 220, after: 80 },
                                     children: [new TextRun({ text, font: FONT, size: 24, bold: true, color: NAVY })] });
const bullet = (children) => new Paragraph({ numbering: { reference: "dots", level: 0 }, spacing: { after: 60, line: 264 },
                                             children: Array.isArray(children) ? children : [run(children)] });
const PH = (text) => run(text, { highlight: "yellow" });   // a blank for Croix to fill in

const cell = (text, w, o = {}) => new TableCell({
  width: { size: w, type: WidthType.DXA },
  shading: o.fill ? { type: ShadingType.CLEAR, color: "auto", fill: o.fill } : undefined,
  margins: { top: 50, bottom: 50, left: 90, right: 90 },
  children: [new Paragraph({ spacing: { after: 0, line: 252 }, alignment: o.align,
                             children: [run(text, { size: o.size || 18, bold: o.bold, color: o.color })] })] });
const border = { style: BorderStyle.SINGLE, size: 4, color: "BFBFBF" };
const borders = { top: border, bottom: border, left: border, right: border, insideHorizontal: border, insideVertical: border };

// ---- the grading scale (Florida Statute 1003.437, grades 6-12)
const scaleW = [W / 5, W / 5, W / 5, W / 5, W / 5];
const scale = new Table({
  width: { size: W, type: WidthType.DXA }, columnWidths: scaleW, borders,
  rows: [
    new TableRow({ children: ["A", "B", "C", "D", "F"].map(g => cell(g, W / 5, { bold: true, fill: "DCE3F0", align: AlignmentType.CENTER, size: 20 })) }),
    new TableRow({ children: ["90–100%", "80–89%", "70–79%", "60–69%", "0–59%"].map(g => cell(g, W / 5, { align: AlignmentType.CENTER, size: 20 })) }),
  ] });

// ---- the year at a glance (from the A7 plan; approximate)
const YEAR = [
  ["Aug – Sep", "Units 1–2: Equations and Inequalities; Real Numbers, Square Roots and Cube Roots", "Two-step equations and inequalities; rewriting rational numbers; squares, cubes and roots; rational and irrational numbers"],
  ["Late Sep – mid Oct", "Unit 3: Exponents and Scientific Notation", "Laws of exponents; very large and very small numbers in scientific notation"],
  ["Late Oct", "Unit 4: Solving Problems with Rational Numbers", "Operations in scientific notation; significant digits; order of operations with exponents and roots"],
  ["Late Oct – early Nov", "Unit 5: Multi-Step Problems with Proportional Relationships", "Scale drawings; converting units between measurement systems"],
  ["November", "Unit 6: Relationships in Triangles", "The Pythagorean Theorem and its converse; distance on the coordinate plane; similar triangles"],
  ["Early Dec", "Unit 7: Representing Proportional Relationships", "Tables, graphs and equations; the constant of proportionality"],
  ["Mid Dec", "Winter FAST (PM2) review", "Review days before the winter progress-monitoring test"],
  ["Mid Dec – early Jan", "Unit 8: Relationships in Circles", "Circumference and area of circles; circle graphs"],
  ["Mid Jan", "Unit 9: Surface Area and Volume", "Surface area and volume of cylinders"],
  ["Late Jan – early Feb", "Unit 10: Linear Relationships", "Slope, y-intercept and graphs of lines"],
  ["February", "Unit 11: Solving Equations and Systems of Equations", "Multi-step equations; systems of two linear equations"],
  ["Late Feb – early Mar", "Unit 12: Functions", "What a function is; linear and nonlinear functions; reading graphs"],
  ["March", "Unit 13: Representing Data", "Scatter plots and lines of fit; choosing a display for data"],
  ["Early Apr", "Unit 14: Equivalent Algebraic Expressions", "Laws of exponents with variables; multiplying and factoring expressions"],
  ["Mid Apr", "Unit 15: Transformations", "Translations, reflections, rotations and dilations"],
  ["Late Apr", "Unit 16: Properties and Theorems of Angles", "Angle relationships; angles of triangles and polygons"],
  ["Late Apr", "Unit 17: Probability", "Probability of single and repeated experiments; making predictions"],
  ["May", "Spring FAST (PM3)", "Review before the test, then a preview of Algebra 1"],
];
const yw = [1900, 3900, W - 1900 - 3900];
const year = new Table({
  width: { size: W, type: WidthType.DXA }, columnWidths: yw, borders,
  rows: [new TableRow({ tableHeader: true, children: ["When (approx.)", "Unit", "What students learn"].map((h, i) => cell(h, yw[i], { bold: true, fill: NAVY, color: "FFFFFF" })) }),
         ...YEAR.map((r, k) => new TableRow({ cantSplit: true, children: r.map((t, i) => cell(t, yw[i], { fill: k % 2 ? "F2F5FA" : undefined, bold: i === 1 && false })) }))] });

const doc = new Document({
  creator: "Mr. Shaffer", title: "Grade 7 Accelerated Mathematics — Course Syllabus 2026–2027",
  styles: { default: { document: { run: { font: FONT, size: 20 } } } },
  numbering: { config: [{ reference: "dots", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
                                                       style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, bottom: 1000, left: 1080, right: 1080 } } },
    children: [
      para([run("Grade 7 Accelerated Mathematics", { size: 36, bold: true, color: NAVY })], { after: 40 }),
      para([run("Course Syllabus  ·  2026–2027  ·  Windy Hill Middle School", { size: 22, color: GREY })], { after: 40 }),
      para([run("Mr. Shaffer  ·  ", { size: 20 }), PH("[school email]")],
           { after: 160, border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: NAVY, space: 6 } } }),

      h2("About this course"),
      para([run("Grade 7 Accelerated Mathematics (course 1205050) is an accelerated course. It covers all of the Grade 8 math standards in Florida’s B.E.S.T. Standards, plus several Grade 7 standards, so that students are ready for Algebra 1 in 8th grade. Florida’s course description names six areas of emphasis:")]),
      bullet("Scientific notation, and extending numbers to the real number system, including irrational numbers"),
      bullet("Equivalent numeric and algebraic expressions, including the Laws of Exponents"),
      bullet("Linear relationships, including modeling data with a linear equation"),
      bullet("Solving linear equations, inequalities and systems of linear equations"),
      bullet("The concept of a function"),
      bullet("Two-dimensional figures, especially triangles, using distance, angles and the Pythagorean Theorem"),
      para([run("Students take the Grade 8 FAST, Florida’s statewide progress-monitoring test, three times this year: fall, winter and spring.")], { before: 60 }),

      h2("Materials"),
      bullet([run("Math Nation", { bold: true }), run(" — our textbook and online platform, with instructional videos")]),
      bullet([run("IXL", { bold: true }), run(" — online practice assigned after each lesson")]),
      bullet([run("Lessons and practice sets", { bold: true }), run(" I create for this course, aligned to the B.E.S.T. standards")]),
      bullet([run("A notebook for class notes, and pencils", { bold: true })]),

      h2("How grades work"),
      para([run("These are graded in every unit:")], { keepNext: true }),
      bullet([run("Unit tests. ", { bold: true }), run("Each unit ends with a test given over two class periods (two short units sometimes share one test). A Unit Review goes home before each test for practice.")]),
      bullet([run("Vocabulary quizzes.", { bold: true })]),
      bullet([run("Notebook checks.", { bold: true })]),
      bullet([run("IXL. ", { bold: true }), run("Assigned after each lesson and due at the start of the next class. An assignment is complete when every listed skill reaches a SmartScore of 67 (IXL’s measure of mastery, out of 100). When two lessons in a row use the same skills, they count as one assignment, due after the second lesson.")]),
      para([run("Other classwork may also be graded from time to time. Grades are posted in Focus, where you can check your child’s progress at any time.")], { before: 60 }),
      para([run("Grades follow Florida’s grading scale for grades 6–12:")], { keepNext: true, after: 80 }),
      scale,

      h2("Late work, retakes and absences"),
      para([run("Late work and test retakes follow Lake County Schools’ grading policy. I handle them individually, so if your child has late or missing work, or would like to talk about a test, please reach out.")]),
      para([run("After an absence, your child should check with me about missed work. Math Nation’s videos are a good way to catch up on a lesson.")]),

      h2("The year at a glance"),
      para([run("The order of units is set; the timing is approximate and may shift to meet students’ needs. Test dates are announced in class.", { italics: true, color: GREY })], { keepNext: true, after: 80 }),
      year,

      h2("Staying in touch"),
      bullet([run("Email: ", { bold: true }), PH("[school email]")]),
      bullet([run("Grades: ", { bold: true }), run("the Focus parent portal")]),
      bullet("I’m happy to set up a phone call or a meeting."),
      para([run("I’m looking forward to a great year.  — Mr. Shaffer")], { before: 160 }),
    ] }] });

Packer.toBuffer(doc).then(b => { fs.writeFileSync("A7 Syllabus 2026-27.docx", b); console.log("wrote docx"); });
