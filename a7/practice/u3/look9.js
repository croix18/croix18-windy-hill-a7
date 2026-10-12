const { chromium } = require('/home/claude/.npm-global/lib/node_modules/playwright');
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); const p = await b.newPage({ viewport: { width: 390, height: 844 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + __dirname + '/preview.html#set-77'); await p.evaluate(() => { try { localStorage.clear(); } catch (e) {} }); await p.reload(); await p.waitForTimeout(200);
  await p.evaluate(() => document.getElementById('bStart').click()); await p.waitForTimeout(1200);
  await p.evaluate(() => { Object.defineProperty(document, 'hidden', { configurable: true, get: () => true }); document.dispatchEvent(new Event('visibilitychange')); });
  await p.waitForTimeout(300);
  console.log('after hide: Resume shown', await p.evaluate(() => !document.getElementById('bStart').hidden && document.getElementById('bStart').textContent), '| time', await p.innerText('#time'));
  await p.waitForTimeout(2200); console.log('2 s later, still', await p.innerText('#time'), '| errors', errs); await b.close(); })();
