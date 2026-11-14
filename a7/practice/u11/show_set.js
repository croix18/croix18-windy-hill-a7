/* Every question of one set with all its help — the rule, the worked solution, the Hint's steps, each modelled mistake typed and
   what the coach says, each wrong choice's reason, and the all-multiple-choice paper's wrong answers — for reading the page as a
   student meets it.   node show_set.js [set=4821] [questions, e.g. 3,6,14] */
const D = __dirname + '/';
const E = require(D + 'engine.js'), C = require(D + 'coach.js'), U = require(D + 'unit.js'), W = C.Walk;
const plain = h => String(h == null ? '' : typeof h === 'object' ? E.eqT(h) : h).replace(/<span class="fr"><span class="nu">([^<]*)<\/span><span class="de">([^<]*)<\/span><\/span>/g, '$1/$2').replace(/<svg[\s\S]*?<\/svg>/g, '[graph]').replace(/<table[\s\S]*?<\/table>/g, '[table]').replace(/<[^>]+>/g, '').replace(/&nbsp;/g, ' ').replace(/&gt;/g, '>').replace(/&lt;/g, '<').replace(/ /g, ' ');
const seed = +process.argv[2] || 4821, only = (process.argv[3] || '').split(',').filter(Boolean).map(Number);
const walkOut = st => (st || []).forEach((s, i) => console.log('    ' + (i + 1) + '. ' + plain(s.ask) + (s.opts ? ' [' + s.opts.map(o => (o.ok ? '*' : '') + plain(o.label) + (o.why ? ' {' + plain(o.why) + '}' : '')).join(' | ') + ']' : ' → ' + E.numStr(s.ans) + '  (hint: ' + plain(s.hint) + ')') + (s.then ? '   then: ' + plain(s.then) : '')));
const G = E.generate(seed); let q = 0;
G.sections.forEach(sec => sec.items.forEach(it => { q++; if (only.length && only.indexOf(q) < 0) return;
  console.log('\n######## Q' + q + ': ' + plain(it.stem) + (it.fig ? '  ' + plain(U.view.figure(it)) : ''));
  if (it.type === 'mc' || it.type === 'multi') {
    it.opts.forEach((o, i) => console.log('   ' + 'ABCDE'[i] + ((Array.isArray(it.correct) ? it.correct.includes(i) : it.correct === i) ? '*' : ' ') + ' ' + plain(o)));
    console.log('  RULE: ' + plain((it.type === 'mc' ? C.mcFeedback(it, (it.correct + 1) % 4) : C.selectFeedback(it, [], 1)).rule || ''));
    console.log('  SHOW ME HOW:'); C.mcSolution(it).forEach(l => console.log('    - ' + plain(l.say)));
    console.log('  HINT:'); walkOut(U.walk(it, 'mc'));
    if (it.type === 'mc') it.opts.forEach((o, k) => { if (k !== it.correct) console.log('  WRONG ' + 'ABCD'[k] + ': ' + plain(C.mcFeedback(it, k).what[0])); });
    else it.opts.forEach((o, k) => { if (!it.correct.includes(k)) console.log('  WRONG ' + 'ABCDE'[k] + ': ' + plain(U.view.why(it, k))); });
    return; }
  E.partsOf(it).forEach(p => {
    if (p.kind === 'mc') { console.log(' -- (' + p.label + ') ' + plain(p.stem) + '   KEY: ' + p.opts[p.correct]);
      console.log('  SHOW ME HOW:'); C.mcSolution(p).forEach(l => console.log('    - ' + plain(l.say) + (l.ex ? '   [' + plain(l.ex) + ']' : '')));
      console.log('  HINT:'); walkOut(U.walk(p, 'mc'));
      p.opts.forEach((o, k) => { if (k !== p.correct) console.log('  WRONG ' + o + ': ' + plain(C.mcFeedback(p, k).what[0])); }); return; }
    console.log(' -- (' + (p.label || '-') + ') ' + plain(U.view.line(p)) + '   KEY: ' + plain(U.view.key(p)) + '   typed: ' + U.keyText(p));
    console.log('  RULE: ' + plain((C.F[p.fam] || C.PF[p.fam]).rule(p)));
    console.log('  SHOW ME HOW:'); C.solution(p).forEach(l => console.log('    - ' + plain(l.say) + (l.ex ? '   [' + plain(l.ex) + ']' : '')));
    console.log('  HINT:'); walkOut(U.walk(p, 'text'));
    ((C.F[p.fam] || C.PF[p.fam]).models(p)).forEach(m => { const t = Array.isArray(m.v) ? '(' + m.v.map(E.kstr).join(', ') + ')' : E.places(m.v) >= 0 ? E.kstr(m.v) : E.kstr(m.v); console.log('  MISTAKE ' + t + ': ' + plain(C.feedback(p, t).what[0])); });
    console.log('  ALL-MC WRONG: ' + U.choices(p).map(plain).join(' | '));
  });
}));
