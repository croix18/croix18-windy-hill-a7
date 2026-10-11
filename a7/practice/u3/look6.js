const { chromium } = require('/home/claude/.npm-global/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + __dirname + '/preview.html#set-4821'); await p.waitForTimeout(200);
  await p.evaluate(() => { try { localStorage.clear(); } catch (e) {} }); await p.reload(); await p.waitForTimeout(200);
  const click = async s => { await p.evaluate(s => document.querySelector(s).click(), s); await p.waitForTimeout(50); };
  await click('[data-walk="1a"]');
  await click('[data-wopt="1a|0|1"]');                    // Multiply (wrong)
  console.log('after wrong tap:', (await p.innerText('#wl1a')).replace(/\s+/g, ' ').slice(0, 260));
  await click('[data-wopt="1a|0|0"]');                    // Add
  await p.fill('#wn1a', '16'); await click('[data-wnum="1a"]');
  console.log('after 16:', (await p.innerText('#wl1a .cur')).replace(/\s+/g, ' '));
  await p.fill('#wn1a', '17'); await p.press('#wn1a', 'Enter'); await p.waitForTimeout(50);
  console.log('finished:', (await p.innerText('#wl1a .wfin')).replace(/\s+/g, ' '));
  await (await p.$('.prt[data-id="1a"]')).screenshot({ path: 'w_walk1a.png' });
  // now the student answers: counts as help
  await p.fill('#a1a', '3^17'); await click('[data-check="1a"]');
  console.log('1a feedback:', (await p.innerText('#fb1a')).replace(/\s+/g, ' '), '| score:', await p.innerText('#score'));
  // select-all walk
  await click('[data-walk="8"]');
  const n8 = await p.evaluate(() => document.querySelectorAll('#wl8 .wopt').length);
  console.log('Q8 walk first step options:', n8);
  // toSci walk
  await click('[data-walk="12a"]'); await click('[data-wopt="12a|0|1"]');
  console.log('12a wrong tap:', (await p.innerText('#wl12a .wwhy')).replace(/\s+/g, ' '));
  await p.reload(); await p.waitForTimeout(200);
  console.log('after reload 1a walk still finished:', await p.evaluate(() => !!document.querySelector('#wl1a .wfin')), '| 12a open:', await p.evaluate(() => !document.getElementById('wl12a').hidden));
  console.log('errors', errs);
  await b.close();
})();
