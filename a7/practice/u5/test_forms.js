/* The numbers of every question on Form A and Form B of the A7 Unit 5 test (a7/build/u5/unit.py), as the page's keys —
   the practice page's exclusion list. CHECK-TIME ONLY: u5_check.js and verify.py load this file; the kit never ships it
   (build.py refuses a page that holds its name or a line of its data — the kit's rule of 24 Oct 2026). The page holds these
   only as hashes (engine.js FORMS_H); u5_check.js proves the hashes are these, and verify.py proves these are the forms'.
   A key is the slot's numbers as the engine writes them: "4>10" a side of 4 that is 10 in the copy; a room "r|p,q" at
   r feet to the inch (¼ in : 1 ft is 4), its sides smaller first; a conversion "from>to|amount"; a recipe's cups as a
   fraction (3/2); a mixture as its sorted parts | the known part's share | the amount (so a reordering is the same question); a rectangle's sides alone (rectWH) keep the test's rectangles off
   the page at any scale factor; a recipe's k and cups (recK) keep its computation off at any yields. The transfer items' numbers are here too (Q8, a room; Q19, two
   speeds): the page's practice room and speed questions never use them. And a form's number that another of the page's
   questions could print (the readers of 30 Oct 2026): `amount`, an amount with its pair of units, whatever the direction
   (Form A Q10's 70 cm, Q11's 4 yd = 144 in, Q8's 100 ft²); `range` and `tripD`, Q16's miles on a tank and its trip; `speedM`,
   the transfer item's mi/h speed, whose conversion the page's Q19 would print. */
const TEST_FORMS = {
  A: { sf: ['4>10', '15>6'], sel3: ['3'], rect: ['3,4|3'], rectWH: ['3,4'], areaK: ['8>72'], room: ['4|3,3.5', '5|2,2'], wall: ['4|3'], plan: ['4|18'],
       conv: ['in>cm|9', 'cm>in|70', 'kg>lb|20', 'gal>L|5'], chain: ['yd>cm|4'], sqconv: ['ft2>m2|20'], curA: ['0.92|60'], curB: ['0.92|23'],
       tank: ['26|15'], trip: ['26|15|1000'], range: ['390'], tripD: ['1000'], recA: ['4|3/2|10'], recB: ['4|3/2|6'], recK: ['2.5|3/2'], mix: ['2:3:4|3|9'], speed: ['60|40'], speedM: ['40'],
       amount: ['in/cm|9', 'in/cm|70', 'in/cm|144', 'lb/kg|20', 'gal/L|5', 'ft2|20', 'ft2|100'] },
  B: { sf: ['6>9', '20>5'], sel3: ['4'], rect: ['2,5|4'], rectWH: ['2,5'], areaK: ['5>80'], room: ['2|3,5', '4|1.5,2'], wall: ['2|3'], plan: ['4|22'],
       conv: ['in>cm|11', 'cm>in|90', 'lb>kg|60', 'gal>L|9'], chain: ['yd>cm|5'], sqconv: ['m2>ft2|5'], curA: ['1.35|70'], curB: ['1.35|54'],
       tank: ['22|20'], trip: ['22|20|1500'], range: ['440'], tripD: ['1500'], recA: ['6|2|9'], recB: ['6|2|8'], recK: ['1.5|2'], mix: ['1:3:4|3|12'], speed: ['90|55'], speedM: ['55'],
       amount: ['in/cm|11', 'in/cm|90', 'in/cm|180', 'lb/kg|60', 'gal/L|9', 'm2|5', 'ft2|48'] }
};
if (typeof module !== 'undefined') module.exports = TEST_FORMS;
if (typeof globalThis !== 'undefined') globalThis.TEST_FORMS = TEST_FORMS;
