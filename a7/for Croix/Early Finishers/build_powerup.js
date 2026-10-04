const fs = require("fs");
const D = JSON.parse(fs.readFileSync("data.json"));
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, AlignmentType, BorderStyle } = require("docx");
const NAVY = "1F3864", FONT = "Arial", W = 12240 - 2 * 1080;
const r = (t, o = {}) => new TextRun({ text: String(t), font: FONT, size: o.size || 24, bold: o.bold, italics: o.italics, color: o.color, superScript: o.sup });
const pow = (b, e, o = {}) => [r(b, o), r(e, { ...o, sup: true })];                  // b^e with a real superscript
const blank = (n = 6) => r("_".repeat(n));
const P = (kids, o = {}) => new Paragraph({ children: kids, spacing: { after: o.after ?? 120, before: o.before ?? 0, line: o.line || 300 }, alignment: o.align, keepNext: o.keepNext });
const LINE = () => new Paragraph({ spacing: { before: 200, after: 0 }, children: [r("_".repeat(72), { color: "808080" })] });
const H = (t) => new Paragraph({ keepNext: true, spacing: { before: 200, after: 100 }, children: [r(t, { bold: true, color: NAVY, size: 26 })] });
const bd = { style: BorderStyle.SINGLE, size: 4, color: "808080" };
const borders = { top: bd, bottom: bd, left: bd, right: bd, insideHorizontal: bd, insideVertical: bd };
const cell = (kids, w, fill) => new TableCell({ width: { size: w, type: WidthType.DXA }, margins: { top: 60, bottom: 60, left: 40, right: 40 },
  shading: fill ? { type: ShadingType.CLEAR, color: "auto", fill } : undefined,
  children: [new Paragraph({ alignment: AlignmentType.CENTER, children: kids })] });
function grid(label1, label2, pairs, key, powKids) {           // two-row table: n | value
  const w = Math.floor(W / (pairs.length + 1)), cols = Array(pairs.length + 1).fill(w);
  const tw = w * (pairs.length + 1);
  return new Table({ width: { size: tw, type: WidthType.DXA }, columnWidths: cols, borders, rows: [
    new TableRow({ children: [cell([r(label1, { bold: true, size: 22 })], w, "DCE3F0"), ...pairs.map(([n]) => cell([r(n, { size: 22 })], w, "DCE3F0"))] }),
    new TableRow({ height: { value: 480, rule: "atLeast" }, children: [cell(powKids, w, "DCE3F0"), ...pairs.map(([n, v]) => cell(key ? [r(v, { size: 22, bold: true, color: "C00000" })] : [r("")], w))] }) ] });
}
function build(key) {
  const K = (t) => r(t, { bold: true, color: "C00000" });       // key answers in red
  const ans = (v, n) => key ? K(v) : blank(n);
  const kids = [
    new Paragraph({ spacing: { after: 0 }, children: [r("Power Up", { size: 44, bold: true, color: NAVY }), ...(key ? [r("   ANSWER KEY", { size: 28, bold: true, color: "C00000" })] : [])] }),
    P([r("Early finishers  ·  Grade 7 Accelerated  ·  from Unit 2 into Unit 3", { size: 20, color: "595959" })], { after: 60 }),
    P([r("Name ", { size: 22 }), r("_".repeat(34), { size: 22 })], { after: 60 }),
    H("1.  Words for tomorrow"),
    P([r("In  "), ...pow(2, 5), r("  the 2 is the  "), ans("base", 14), r("  and the 5 is the  "), ans("exponent", 14), r(".")]),
    H("2.  Squares and cubes (from Unit 2)"),
    grid("n", "", D.squares, key, [...pow("n", 2, { size: 22, bold: true })]),
    P([], { after: 100 }),
    grid("n", "", D.cubes.concat([]), key, [...pow("n", 3, { size: 22, bold: true })]),
    H("3.  Powers of 2   (each one is double the one before)"),
    grid("n", "", D.pow2, key, [...pow(2, "n", { size: 22, bold: true })]),
    H("4.  Pattern hunt   (use your powers-of-2 table)"),
    ...(key ? [] : [P([r("Fill in each blank. Write the exponent in the small box.", { italics: true, size: 22 })], { after: 80 })]),
    ...D.pattern.map(([a, b, x, y, prod, s], i) => P([r(`${"abcd"[i]})   `), ...pow(2, a), r("  ×  "), ...pow(2, b), r("   =   "),
        key ? K(x) : blank(5), r("  ×  "), key ? K(y) : blank(5), r("   =   "), key ? K(prod) : blank(6), r("   =   2"),
        key ? r(s, { sup: true, bold: true, color: "C00000" }) : r("□", { sup: true, size: 34 })], { after: 60 })),
    P([r("What do you notice about the exponents?", { bold: true }), ...(key ? [r("  "), K("When you multiply powers of 2, you add the exponents.")] : [])], { before: 100, after: 0 }),
    ...(key ? [] : [LINE(), LINE()]),
    H("5.  Which is larger?   Circle the larger one, or write  =  if they are equal."),
    new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W / 5, W / 5, W / 5, W / 5, W / 5], borders: { top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE }, left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE }, insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE } },
      rows: [new TableRow({ children: D.compare.map(([b1, e1, v1, b2, e2, v2, w], i) => new TableCell({ width: { size: W / 5, type: WidthType.DXA },
        children: [new Paragraph({ alignment: AlignmentType.LEFT, children: [r(`${"abcde"[i]})  `), ...pow(b1, e1), r("   or   "), ...pow(b2, e2)] }),
                   ...(key ? [new Paragraph({ children: [K(w === "equal" ? `equal: both ${v1}` : `${w === "left" ? b1 : b2}^${w === "left" ? e1 : e2}`.replace(/\^(\d+)/, (m, e) => "") ), ...(w === "equal" ? [] : [r(w === "left" ? e1 : e2, { sup: true, bold: true, color: "C00000" }), K(` (${w === "left" ? v1 : v2} vs ${w === "left" ? v2 : v1})`)])] })] : [])] })) })] }),
    H("Challenge"),
    P([r("Find a power between 500 and 600, using an exponent greater than 1. There are four of them. Can you find them all?")], { after: 0 }),
    ...(key ? [] : [LINE(), LINE()]),
    ...(key ? [P([K("2"), r("9", { sup: true, bold: true, color: "C00000" }), K(" = 512,   8"), r("3", { sup: true, bold: true, color: "C00000" }), K(" = 512,   23"), r("2", { sup: true, bold: true, color: "C00000" }), K(" = 529,   24"), r("2", { sup: true, bold: true, color: "C00000" }), K(" = 576")]),
               P([r("For you: 2", { italics: true, size: 20 }), r("9", { sup: true, italics: true, size: 20 }), r(" = 8", { italics: true, size: 20 }), r("3", { sup: true, italics: true, size: 20 }), r(" because 8 = 2", { italics: true, size: 20 }), r("3", { sup: true, italics: true, size: 20 }), r(", so 8", { italics: true, size: 20 }), r("3", { sup: true, italics: true, size: 20 }), r(" = (2", { italics: true, size: 20 }), r("3", { sup: true, italics: true, size: 20 }), r(")", { italics: true, size: 20 }), r("3", { sup: true, italics: true, size: 20 }), r(" = 2", { italics: true, size: 20 }), r("9", { sup: true, italics: true, size: 20 }), r(": a preview of tomorrow's power of a power law. Part 4 previews the product of powers law.", { italics: true, size: 20 })], { before: 80 })] : []),
  ];
  return new Document({ styles: { default: { document: { run: { font: FONT, size: 24 } } } },
    sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 900, bottom: 900, left: 1080, right: 1080 } } }, children: kids }] });
}
Promise.all([Packer.toBuffer(build(false)), Packer.toBuffer(build(true))]).then(([a, b]) => {
  fs.writeFileSync("A7 Power Up.docx", a); fs.writeFileSync("A7 Power Up - Key.docx", b); console.log("built"); });
