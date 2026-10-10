const { chromium } = require('/home/claude/.npm-global/lib/node_modules/playwright');
const P = require('./engine.js');
function atomish(a) { return a.t === 'n' || a.t === 'v' || a.t === 'pow' || a.t === 'par'; }
function typed(a, o) {                      // how a student would type it
  o = o || {};
  switch (a.t) {
    case 'n': return o.commas ? P.commas(a.s) : a.s;
    case 'v': return a.s;
    case 'pow': { const b = a.b.t === 'n' || a.b.t === 'v' ? typed(a.b) : '(' + typed(a.b.t === 'par' ? a.b.x : a.b) + ')';
      const e = a.e.t === 'n' ? a.e.s : a.e.t === 'neg' && a.e.x.t === 'n' ? '-' + a.e.x.s : '(' + typed(a.e) + ')';
      return b + '^' + e; }
    case 'mul': return a.xs.map(x => x.t === 'neg' || x.t === 'frac' ? '(' + typed(x) + ')' : typed(x)).join(a.op === '' ? '' : a.op === '×' ? ' x ' : '*');
    case 'frac': { const n = atomish(a.n) || (a.n.t === 'mul' && a.n.op === '') ? typed(a.n) : '(' + typed(a.n) + ')';
      const d = atomish(a.d) ? typed(a.d) : '(' + typed(a.d) + ')'; return n + '/' + d; }
    case 'neg': return '-' + (atomish(a.x) || a.x.t === 'frac' ? typed(a.x) : '(' + typed(a.x) + ')');
    case 'par': return '(' + typed(a.x) + ')';
    case 'eq': return typed(a.l) + '=' + typed(a.r);
  }
  throw new Error('typed ' + a.t);
}

(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 390, height: 844 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  for (const seed of [11, 2024, 99999, 31337]) {
    await p.goto('file://' + __dirname + '/preview.html#set-' + seed); await p.waitForTimeout(200);
    await p.evaluate(() => { try { localStorage.clear(); } catch (e) {} }); await p.reload(); await p.waitForTimeout(200);
    const G = P.generate(seed); let qn = 0;
    for (const sec of G.sections) for (const it of sec.items) {
      qn++;
      if (it.type === 'parts' || it.type === 'solo') {
        for (const pt of (it.type === 'parts' ? it.parts : [it.part])) { const id = qn + (it.type === 'parts' ? pt.label : '');
          await p.fill('#a' + id, typed(pt.ans, { commas: pt.kind === 'std' })); await p.evaluate(id => document.querySelector('[data-check="' + id + '"]').click(), id); }
      } else {
        const ks = it.type === 'mc' ? [it.correct] : it.correct;
        for (const k of ks) await p.evaluate(([q, k]) => document.querySelector('input[name="q' + q + '"][value="' + k + '"]').click(), [qn, k]);
        await p.evaluate(q => document.querySelector('[data-check="' + q + '"]').click(), qn);
      }
    }
    const notRight = await p.evaluate(() => Array.from(document.querySelectorAll('.fb')).filter(f => !/Correct/.test(f.innerText)).map(f => f.id + ' ' + f.innerText));
    console.log('set', seed, '|', await p.innerText('#score'), '| not right:', notRight.length ? notRight : 'none');
  }
  console.log('errors', errs);
  await b.close();
})();
