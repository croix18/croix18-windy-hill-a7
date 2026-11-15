/* A7 Unit 11 practice: the wrong answers of an all-multiple-choice paper (unit.js `choices`; the kit's ui.js mcOf prints the
   first three beside the key; Croix, 14 Nov 2026: "I'd like the retakes that I print up to be all multiple choice").
   node mc_check.js [sets=3000]   → exits 1 on any failure.
   Read here from the words a student would see, with this file's own reader: for every typed part of every set — at least three
   wrong answers; each in the key's own shape (a number with the same letter or unit; an ordered pair; weeks and an amount;
   "about" and a pair); none the answer, and for an estimate none inside its tolerance of 0.1, so a paper never has two right
   choices; no two the same; and each of the three that print is what one of the part's named mistakes gives, unless the part
   has fewer than three (then a value one away from the answer fills the place, and is counted). */
'use strict';
const U = require('./unit.js'), C = require('./coach.js'), E = require('./engine.js');
const N = +(process.argv[2] || 3000); let nfail = 0, parts = 0, named = 0, filled = 0, boxed = 0; const fails = [], byFam = {};
const fail = (s, w, m) => { nfail++; if (fails.length < 40) fails.push('set ' + s + ' ' + w + ': ' + m); };
const plain = h => String(h).replace(/<span class="fr"><span class="nu">([^<]*)<\/span><span class="de">([^<]*)<\/span><\/span>/g, '$1/$2').replace(/<[^>]+>/g, ' ').replace(/&nbsp;| /g, ' ').replace(/−/g, '-').replace(/\s+/g, ' ').trim();
const nums = t => (t.match(/-?\d+(?:\.\d+)?(?:\/\d+)?/g) || []).map(x => x.indexOf('/') > 0 ? Number(x.split('/')[0]) / Number(x.split('/')[1]) : Number(x));
const shape = t => t.replace(/-?\d+(?:\.\d+)?(?:\/\d+)?/g, '#');
for (let s = 1; s <= N; s++) U.generate(s).sections.forEach((sec, si) => sec.items.forEach((it, ii) => {
  E.partsOf(it).forEach(p => {
    if (['num', 'pair', 'story'].indexOf(p.kind) < 0) return;
    const w = (si + 1) + '.' + (ii + 1) + (p.label || '') + ' ' + p.fam, key = plain(U.view.key(p)), kv = nums(key), ch = U.choices(p).map(plain); parts++;
    const want = p.kind === 'num' ? [E.qnum(p.ans)] : p.ans.map(E.qnum);
    if (kv.length !== want.length || kv.some((v, i) => Math.abs(v - want[i]) > 1e-9)) fail(s, w, 'the key "' + key + '" does not read as the answer');
    if (ch.length < 3) fail(s, w, 'only ' + ch.length + ' wrong answers');
    /* two boxes (15 Nov 2026): the screen takes one number a box, but the key and the paper's choices stay whole (a pair, or the
       weeks and the amount) — so a box's key is that coordinate of the whole key, and every choice still has both numbers */
    const B = U.view.boxes(p), kt = U.keyText(p);
    if ((p.kind === 'num') !== !B) fail(s, w, p.kind === 'num' ? 'one number with boxes' : 'two numbers without two boxes');
    if (B) { boxed++; if (!Array.isArray(kt) || kt.length !== B.length || kt.some((t, i) => Math.abs(Number(t.indexOf('/') > 0 ? t.split('/')[0] / t.split('/')[1] : t) - want[i]) > 1e-9)) fail(s, w, 'the boxes\' keys ' + JSON.stringify(kt) + ' are not the key "' + key + '"'); }
    if (new Set(ch).size !== ch.length) fail(s, w, 'a wrong answer twice');
    const mods = (p.kind === 'num' ? C.F[p.fam].models(p).map(m => [E.qnum(m.v)]) : C.PF[p.fam].models(p).map(m => m.v.map(E.qnum)));
    ch.forEach((c, i) => { const v = nums(c);
      if (shape(c) !== shape(key)) fail(s, w, '"' + c + '" is not in the key\'s shape "' + key + '"');
      if (v.length !== kv.length) { fail(s, w, '"' + c + '" has ' + v.length + ' numbers'); return; }
      if (p.fam === 'estimate') { const ex = [E.qnum(p.ans[0]), E.qnum(p.ans[1])];      /* within 0.1 of the key, the lead's ruling of 14 Nov 2026 */ if (Math.abs(v[0] - ex[0]) <= 0.1 + 1e-9 && Math.abs(v[1] - ex[1]) <= 0.1 + 1e-9) fail(s, w, '"' + c + '" is inside the tolerance'); }
      else if (v.every((x, j) => Math.abs(x - kv[j]) < 1e-9)) fail(s, w, '"' + c + '" is the answer');
      if (p.fam === 'plans' && !(v[0] > 0)) fail(s, w, '"' + c + '" is not a count');
      if (i < 3) { const m = mods.some(mv => mv.every((x, j) => Math.abs((p.fam === 'estimate' ? Math.round(x * 10) / 10 : x) - v[j]) < 1e-9));
        if (m) named++; else { filled++; byFam[p.fam] = (byFam[p.fam] || 0) + 1;
          const off = v.map((x, j) => Math.abs(x - kv[j])); if (!(off.reduce((a, b) => a + b, 0) <= 3 + 1e-9)) fail(s, w, '"' + c + '" is neither a named mistake nor a value near the answer'); } } });
  });
}));
if (boxed !== 4 * N) fail('all', 'boxes', boxed + ' parts with two boxes, not ' + 4 * N);
console.log(N + ' sets: ' + parts + ' typed parts (' + boxed + ' of them two boxes, keyed and offered whole), three wrong answers each; ' + named + ' are a named mistake, ' + filled + ' a nearby value' + (filled ? ' (' + Object.keys(byFam).sort().map(k => k + ' ' + byFam[k]).join(', ') + ')' : ''));
if (nfail) { console.log(nfail + ' PROBLEMS'); fails.forEach(f => console.log('  ' + f)); process.exit(1); }
console.log('mc_check: ALL SOUND');
