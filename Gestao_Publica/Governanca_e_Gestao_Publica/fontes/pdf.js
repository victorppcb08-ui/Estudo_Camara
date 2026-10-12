const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await (await b.newContext({ colorScheme: 'light' })).newPage();
  await p.goto('file://' + path.resolve(process.argv[2]) + '#pdf');
  await p.waitForTimeout(1200);
  await p.evaluate(() => { document.documentElement.classList.add('modo-pdf'); document.querySelectorAll('.qbloco').forEach(el => { el.dataset.revelar = '1'; }); });
  await p.evaluate(() => window.dispatchEvent(new Event('load')));
  await p.evaluate(() => { if (typeof redesenha === 'function') redesenha(); });
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, margin: { top: '14mm', bottom: '16mm', left: '14mm', right: '14mm' },
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#536158;font-family:sans-serif">Governança e Gestão Pública · Câmara dos Deputados 2027 · <span class="pageNumber"></span>/<span class="totalPages"></span></div>' });
  await b.close();
})();
