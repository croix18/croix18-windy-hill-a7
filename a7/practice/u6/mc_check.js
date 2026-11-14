/* A7 Unit 6 practice: the wrong answers of an all-multiple-choice paper (unit.js `choices`; the kit's ui.js mcOf prints the
   first three beside the key; Croix, 14 Nov 2026: "I'd like the retakes that I print up to be all multiple choice").
   node mc_check.js [sets=3000]   → exits 1 on any failure.
   Read here from the words a student would see, with this file's own reader (not the coach's numbers): for every typed part
   of every set — at least three wrong answers; each a positive length in the part's own unit; none the answer, and none
   within its rounding (0.05) of it, so a paper never has two right choices; no two the same; and the three that print are
   each what one of the part's named mistakes gives, unless the part has fewer than three mistakes to give (then a length
   one or two units from the answer fills the place, and is counted). */
'use strict';
const U = require('./unit.js'), C = require('./coach.js'), E = require('./engine.js');
const N = +(process.argv[2] || 3000); let nfail = 0, parts = 0, named = 0, filled = 0; const fails = [], byFam = {};
const fail = (s, w, m) => { nfail++; if (fails.length < 40) fails.push('set ' + s + ' ' + w + ': ' + m); };
const read = h => { const t = String(h).replace(/<[^>]+>/g, ' ').replace(/&nbsp;| /g, ' ').replace(/−/g, '-').replace(/\s+/g, ' ').trim(), m = /^(-?[\d,]+(?:\.\d+)?)(?: (.+))?$/.exec(t);
  return m ? { v: Number(m[1].replace(/,/g, '')), unit: m[2] || '' } : null; };
for (let s = 1; s <= N; s++) U.generate(s).sections.forEach((sec, si) => sec.items.forEach((it, ii) => {
  (it.type === 'parts' ? it.parts : it.type === 'solo' ? [it.part] : []).forEach(p => {
    if (p.kind === 'mc') return;
    const w = (si + 1) + '.' + (ii + 1) + (p.label || '') + ' ' + p.fam, key = read(U.view.key(p)), ch = U.choices(p), got = ch.map(read); parts++;
    if (!key) { fail(s, w, 'the key "' + U.view.key(p) + '" is not a number'); return; }
    if (Math.abs(key.v - E.qnum(p.ans)) > 1e-9) fail(s, w, 'the key reads ' + key.v);
    if (ch.length < 3) fail(s, w, 'only ' + ch.length + ' wrong answers');
    got.forEach((g, i) => {
      if (!g) { fail(s, w, 'choice "' + ch[i] + '" is not a number'); return; }
      if (g.unit !== key.unit) fail(s, w, 'choice "' + ch[i] + '" is not in ' + (key.unit || 'no unit'));
      if (!(g.v > 0)) fail(s, w, 'choice ' + g.v + ' is not a length');
      if (Math.abs(g.v - key.v) < 0.05) fail(s, w, 'choice ' + g.v + ' is the answer ' + key.v + ', or its rounding');
      got.forEach((h, j) => { if (j < i && h && Math.abs(h.v - g.v) < 1e-9) fail(s, w, 'choice ' + g.v + ' twice'); });
    });
    /* the three that print: a named mistake's value (to the tenth when it ends on a root), else a counted filler */
    const mods = (C.F[p.fam].models(p) || []).map(m => m.f != null ? m.f : E.qnum(m.v));
    got.slice(0, 3).forEach(g => { if (!g) return; if (mods.some(f => Math.abs(f - g.v) < 0.0501)) named++; else { filled++; byFam[p.fam] = (byFam[p.fam] || 0) + 1;
      if (!(Math.abs(g.v - key.v) >= 1 - 1e-9 && Math.abs(g.v - key.v) <= 4 + 1e-9)) fail(s, w, 'choice ' + g.v + ' is neither a named mistake nor a length near the answer'); } });
  });
}));
console.log(N + ' sets: ' + parts + ' typed parts, three wrong answers each; ' + named + ' are a named mistake, ' + filled + ' a nearby length' + (filled ? ' (' + Object.keys(byFam).sort().map(k => k + ' ' + byFam[k]).join(', ') + ')' : ''));
if (nfail) { console.log(nfail + ' PROBLEMS'); fails.forEach(f => console.log('  ' + f)); process.exit(1); }
console.log('mc_check: ALL SOUND');
