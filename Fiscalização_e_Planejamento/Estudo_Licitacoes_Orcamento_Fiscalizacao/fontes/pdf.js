// Gera o PDF com todos os gabaritos e comentários revelados.
// Uso: node fontes/pdf.js Licitacoes_Orcamento_Fiscalizacao.html Licitacoes_Orcamento_Fiscalizacao.pdf
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await (await b.newContext({ colorScheme: 'light' })).newPage();
  await p.goto('file://' + path.resolve(process.argv[2]) + '#pdf');
  await p.waitForTimeout(1500);
  await p.evaluate(() => { document.documentElement.classList.add('modo-pdf'); document.querySelectorAll('.qbloco').forEach(el => { el.dataset.revelar = '1'; }); });
  await p.evaluate(() => { if (typeof redesenha === 'function') redesenha(); });
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, margin: { top: '14mm', bottom: '16mm', left: '14mm', right: '14mm' },
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#536158;font-family:sans-serif">Licitações, Orçamento e Fiscalização · Câmara dos Deputados 2027 · <span class="pageNumber"></span>/<span class="totalPages"></span></div>' });
  await b.close();
})();
