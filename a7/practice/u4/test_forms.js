/* The numbers of every question on Form A, Form B (19 Oct 2026) and the review of the A7 Unit 4 test — the practice's
   exclusion list. CHECK-TIME ONLY: u4_check.js loads this file before the engine; the kit never ships it (24 Oct 2026,
   P0 of the ChatGPT review: the student page carried these numbers, labelled, where any student could read them in the
   page source). The shipped page has no exclusion list, so a practice question can be a test question on rare sets; the
   check reports how many sets that is. Ruling 49 makes the test a random set of this page from now on. */
const TEST_FORMS = {
  addSame: [['3.6', 5, '2.1', 5], ['4.3', 6, '2.4', 6]], subSame: [['8.4', -6, '5.9', -6], ['9.1', -5, '3.6', -5]], addCarry: [['7.5', 8, '6.8', 8], ['6.4', 7, '8.2', 7]], addGap: [['4.2', 4, '3.7', 3], ['5.3', 5, '2.6', 4]],
  mulInt: [[3, 4, 2, 6], [4, 3, 2, 5]], divDec: [['9.6', 9, '1.2', 4], ['8.4', 8, '2.1', 3]], mulAdj: [[5, -3, 4, 7], [6, -4, 5, 6]], divAdj: [['1.8', 2, 6, 5], ['1.5', 2, 5, 6]],
  mcGap: [['1.4', 3, '2.9', 5], ['2.3', 3, '4.1', 5]], selSci: [[3, 6], [4, 6]],
  kendra: [['2.3', 4, '6.1', 6], ['3.4', 4, '5.2', 6]],   /* Form B's Devon: 3.4 × 10⁴ since 21 Oct (it was 10³, a gap of 3) */
  rate: [['6.5', 14, '4', 2], ['4', 3, '2', -1], ['5', 4, '3', -2]],   /* the review's laser, and the two forms' transfer item */
  rwArea: [['2.4', '1.35'], ['3.5', '1.25'], ['3.2', '1.45']], rwSpeed: [['5.6', 8], ['7.2', 8], ['4.8', 6]],
  rwSum: [['6.25', '4.1'], ['7.35', '5.2'], ['5.4', '2.8']], rwDiff: [['9.3', '4.72'], ['8.4', '3.61'], ['7.6', '3.42']],
  ooA: [[15, 2, 3], [20, 3, 2], [24, 3, 5]], ooB: [[5, 7, 2], [4, 9, 5], [6, 9, 3]], ooC: [[36, 4, 3], [45, 9, 3], [48, 6, 2]], ooD: [[4, 4], [3, 3], [6, 6]],
  radA: [[6, 13], [8, 17], [7, -24]], radB: [[5, 2], [4, 3]], radC: [[3, 2, 3], [2, 3, 4], [2, 1, 3]],
  patio: [[14, '2.40', 85], [12, '2.60', 75], [15, '2.20', 60], [18, '3.50', 140]], mcOrder: [[2, 5, 3], [3, 4, 3], [2, 4, 5]], selVal: [6, 8],
  nadia: [[5, 12], [6, 8]], negSub: [[5, 3]]
};
if (typeof module !== 'undefined') module.exports = TEST_FORMS;
if (typeof globalThis !== 'undefined') globalThis.TEST_FORMS = TEST_FORMS;
