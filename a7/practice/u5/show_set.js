/* Every question of one set with all its help — the rule, Show me how, the Hint, and each modelled mistake typed — for reading the page as a student meets it.   node show_set.js [set=4821] [questions, e.g. 3,6,19] */
const D = __dirname + "/";
const E = require(D + 'engine.js'), C = require(D + 'coach.js'), U = require(D + 'unit.js'), W = C.Walk;
const plain = h => String(h).replace(/(\d)<span class="fr"><span class="nu">([^<]*)<\/span><span class="de">([^<]*)<\/span><\/span>/g, '$1 $2/$3').replace(/<span class="fr"><span class="nu">([^<]*)<\/span><span class="de">([^<]*)<\/span><\/span>/g, '$1/$2').replace(/<sup>(.*?)<\/sup>/g, '^$1').replace(/<[^>]+>/g, '').replace(/&gt;/g, '>').replace(/&lt;/g, '<');
const seed = +process.argv[2] || 4821, only = (process.argv[3] || '').split(',').filter(Boolean).map(Number);
const G = E.generate(seed); let q = 0;
G.sections.forEach(sec => sec.items.forEach(it => { q++; if (only.length && only.indexOf(q) < 0) return;
  console.log('\n######## Q' + q + ': ' + plain(it.stem));
  if (it.opts) { it.opts.forEach((o, i) => console.log('   ' + 'ABCDE'[i] + ((Array.isArray(it.correct) ? it.correct.includes(i) : it.correct === i) ? '*' : ' ') + ' ' + plain(o)));
    console.log('  SHOW ME HOW:'); C.mcSolution(it).forEach(l => console.log('    - ' + plain(l.say)));
    console.log('  HINT:'); W.stepsMC(it).forEach((s, i) => console.log('    ' + (i + 1) + '. ' + plain(s.ask) + (s.opts ? ' [' + s.opts.map(o => (o.ok ? '*' : '') + plain(o.label) + (o.why ? ' {' + plain(o.why) + '}' : '')).join(' | ') + ']' : ' → ' + E.numStr(s.ans) + '  (hint: ' + plain(s.hint) + ')')));
    if (it.type === 'mc') it.opts.forEach((o, k) => { if (k !== it.correct) console.log('  WRONG ' + 'ABCD'[k] + ': ' + plain(C.mcFeedback(it, k).what[0])); });
    else console.log('  WRONG 2nd try: ' + C.selectFeedback(it, [0, 1, 2, 3].filter(i => !it.correct.includes(i)), 2).what.map(plain).join(' // '));
    return; }
  E.partsOf(it).forEach(p => {
    console.log(' -- (' + (p.label || '-') + ') ' + plain(p.stem) + '   KEY: ' + plain(E.ansHtml(p)));
    console.log('  RULE: ' + plain(C.F[p.fam].rule(p)));
    console.log('  SHOW ME HOW:'); C.solution(p).forEach(l => console.log('    - ' + plain(l.say) + (l.ex ? '   [' + plain(l.ex.h) + ']' : '')));
    console.log('  HINT:'); W.steps(p).forEach((s, i) => console.log('    ' + (i + 1) + '. ' + plain(s.ask) + (s.opts ? ' [' + s.opts.map(o => (o.ok ? '*' : '') + plain(o.label) + (o.why ? ' {' + plain(o.why) + '}' : '')).join(' | ') + ']' : ' → ' + E.numStr(s.ans) + '  (hint: ' + plain(s.hint) + ')')));
    C.F[p.fam].models(p).forEach(m => { const t = E.places(m.v) >= 0 ? E.decPlain(m.v) : E.fixed(m.v, 2); console.log('  MISTAKE ' + t + ': ' + plain(C.feedback(p, t, {}).what[0])); });
  });
}));
