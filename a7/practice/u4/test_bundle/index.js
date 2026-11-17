/* A7 Unit 4 Test: the site's bundle (practice/kit/exam/build_exam.py; do not edit — build it again). */
'use strict';
/* the unit as bank.js makes it on the practice page, to judge a lesson test's items (they carry their keys: no bank is loaded) */
function lessonUnit() {
  const U = require('./u4/unit.js'), w = { Unit: Object.assign({}, U, { view: Object.assign({}, U.view), judge: Object.assign({}, U.judge) }),
    CADENCE_BANK: { lessons: {} }, CADENCE_MAP: { order: [], lessons: {} }, Kit: Object.assign({}, require('./kit/core.js')) };
  require('./kit/bank_node.js')(w, undefined);
  return w.Unit;
}
module.exports = { course: "a7", unit: 4, cv: 5, kit: "3f3540b015d8",
  U: require('./u4/unit.js'), server: require('./kit/exam/server.js'), pack: require('./kit/pack.js'),
  UL: lessonUnit(), lessons: [{"scope": "lesson-4.01", "code": "4.01", "title": "Add and subtract in scientific notation", "name": "Lesson 4.01 · Add and subtract in scientific notation", "day": false}, {"scope": "lesson-4.02", "code": "4.02", "title": "Multiplying Numbers Expressed in Scientific Notation", "name": "Lesson 4.02 · Multiplying Numbers Expressed in Scientific Notation", "day": false}, {"scope": "lesson-4.03", "code": "4.03", "title": "Dividing Numbers Expressed in Scientific Notation", "name": "Lesson 4.03 · Dividing Numbers Expressed in Scientific Notation", "day": false}, {"scope": "lesson-4.02+03", "code": "4.02+03", "title": "Multiply and divide in scientific notation", "name": "Lessons 4.02–03 · Multiply and divide in scientific notation", "day": true}, {"scope": "lesson-4.04", "code": "4.04", "title": "Real-world scientific notation; significant digits", "name": "Lesson 4.04 · Real-world scientific notation; significant digits", "day": false}, {"scope": "lesson-4.05", "code": "4.05", "title": "Expressions with radicals (perfect squares to 225, cubes −125 to 125)", "name": "Lesson 4.05 · Expressions with radicals (perfect squares to 225, cubes −125 to 125)", "day": false}, {"scope": "lesson-4.06", "code": "4.06", "title": "Order of operations with exponents and radicals", "name": "Lesson 4.06 · Order of operations with exponents and radicals", "day": false}] };
