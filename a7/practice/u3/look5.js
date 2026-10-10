const { chromium } = require('/home/claude/.npm-global/lib/node_modules/playwright');
const P = require('./engine.js'), C = require('./coach.js');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + __dirname + '/preview.html#set-4821'); await p.waitForTimeout(200);
  await p.evaluate(() => { try { localStorage.clear(); } catch (e) {} }); await p.reload(); await p.waitForTimeout(200);
  const clickSel = async s => { await p.evaluate(s => document.querySelector(s).click(), s); await p.waitForTimeout(60); };
  // 1. wrong, then try another twice
  await p.fill('#a1a', '3^72'); await clickSel('[data-check="1a"]');
  await clickSel('[data-another="1a"]');
  for (let r = 0; r < 2; r++) {
    const xid = await p.evaluate(() => { const q = document.querySelector('#ag1a .xq'); return q.dataset.q; });
    const ans = await p.evaluate(xid => { const S = JSON.parse(localStorage.getItem('a7u3prac.v3.set.4821.all')); const m = S.more['1a']; const G = Practice.generate(m.seed); const pt = G.sections[0].items[0].parts[0]; return pt.prm.b + '^' + (pt.prm.m + pt.prm.n); }, xid);
    await p.fill('#a' + xid, ans); await clickSel('[data-check="' + xid + '"]');
    console.log('extra', r + 1, xid, ans, '→', (await p.innerText('#fb' + xid)).replace(/\s+/g, ' '), '|', await p.innerText('#ag1a .xhead'));
    if (r === 0) await clickSel('#ag1a [data-another="1a"]');
  }
  await (await p.$('.q[data-q="1"]')).screenshot({ path: 'v_another.png' });
  // 2. help me solve on 2c
  await clickSel('[data-work="2c"]');
  await p.fill('#wt2c', '10^9/10^7\n10^2\n100'); await clickSel('[data-wcheck="2c"]');
  console.log('work 2c:', (await p.innerText('#wr2c')).replace(/\s+/g, ' '));
  await clickSel('[data-wuse="2c"]'); console.log('answer box now:', await p.inputValue('#a2c'));
  await p.fill('#wt2c', '10^6/10^7'); await clickSel('[data-wcheck="2c"]');
  console.log('work 2c wrong:', (await p.innerText('#wr2c')).replace(/\s+/g, ' '));
  await (await p.$('.prt[data-id="2c"]')).screenshot({ path: 'v_work.png' });
  // 3. pictures
  for (const [id, wrong] of [['1b', '3^9'], ['6a', '-512'], ['6b', '1/8'], ['9c', '3m^10'], ['12a', '9.1 x 10^6'], ['13b', '0.000075'], ['1c', '10^17'], ['2a', '4/49']]) {
    await p.fill('#a' + id, wrong); await clickSel('[data-check="' + id + '"]'); await clickSel('[data-all="' + id + '"]');
    const el = await p.$('#st' + id); await el.screenshot({ path: 'v_pic_' + id + '.png' });
  }
  // 4. finish, misses, scopes
  await clickSel('#bFinish'); await clickSel('#cy');
  const nm = await p.evaluate(() => Object.keys(JSON.parse(localStorage.getItem('a7u3prac.v3.misses'))).length);
  console.log('misses saved:', nm, '| result buttons:', (await p.innerText('#result .btns')).replace(/\s+/g, ' | '));
  await p.selectOption('#scope', 'miss'); await p.waitForTimeout(200);
  console.log('miss scope: items', await p.evaluate(() => document.querySelectorAll('#paper .prt, #paper .choices').length), '| total', await p.innerText('#total'), '| hash', await p.evaluate(() => location.hash));
  await p.selectOption('#scope', 'p2'); await p.waitForTimeout(200);
  console.log('p2 scope: total', await p.innerText('#total'), '| headings', (await p.evaluate(() => Array.from(document.querySelectorAll('.sechead h2')).map(h => h.textContent))).join(' / '));
  await p.screenshot({ path: 'v_p2.png' });
  console.log('wider than screen:', await p.evaluate(() => document.documentElement.scrollWidth > innerWidth));
  console.log('errors', errs);
  await b.close();
})();
