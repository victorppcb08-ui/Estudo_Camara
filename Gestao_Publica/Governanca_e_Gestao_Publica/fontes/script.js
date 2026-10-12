const DADOS = /*__DADOS__*/[];
const CHAVE = 'governanca-gestao-publica-v1';
const ORDEM = ['8', '8.1', '8.2', '8.3', '8.4', '9.1', '9.2', '9.3', '9.4'];
const ROTULOS = { '8': '8 Modelos', '8.1': '8.1 NPG', '8.2': '8.2 Redes', '8.3': '8.3 Coprodução', '8.4': '8.4 Valor', '9.1': '9.1 Conceito', '9.2': '9.2 Mecanismos', '9.3': '9.3 Resultados', '9.4': '9.4 Decreto' };
let resp = {};
try { resp = JSON.parse(localStorage.getItem(CHAVE) || '{}') || {}; } catch (e) { resp = {}; }
function salvar() { try { localStorage.setItem(CHAVE, JSON.stringify(resp)); } catch (e) {} }
const porId = {}; DADOS.forEach(q => porId[q.id] = q);
const filtro = {};
let sorteio = [];

function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }
function certa(q) { return q.gab === 'Certo' ? 'C' : 'E'; }
function situacao(q) { const r = resp[q.id]; if (!r) return 'nova'; return r === certa(q) ? 'acertou' : 'errou'; }
function listaDe(t) { return t === 'REL' ? sorteio.map(i => porId[i]) : DADOS.filter(q => q.t === t); }

function htmlQuestao(q, revelar, bloco) {
  const r = resp[q.id], mostra = revelar || !!r, ok = certa(q);
  const opts = '<div class="opts ce">' + [['C', 'Certo'], ['E', 'Errado']].map(([l, t]) => {
    let cls = 'opt';
    if (mostra && ok === l) cls += ' certa';
    if (r === l && r !== ok) cls += ' marcada-errada';
    return '<button type="button" class="' + cls + '" data-q="' + q.id + '" data-op="' + l + '"' + (r ? ' disabled' : '') + ' aria-pressed="' + (r === l) + '">' + t + '</button>';
  }).join('') + '</div>';
  let corpo = '';
  if (mostra) {
    const s = situacao(q);
    const ver = !r ? 'Gabarito: ' + q.gab : (s === 'acertou' ? 'Acertou · gabarito ' : 'Errou · gabarito ') + q.gab;
    const vcls = !r ? 'neu' : (s === 'acertou' ? 'ok' : 'bad');
    corpo = '<div class="resp"><div class="veredito ' + vcls + '">' + ver + '</div><p>' + esc(q.c) + '</p>' + (q.a ? '<div class="alerta"><b>Pegadinha:</b> ' + esc(q.a) + '</div>' : '') + '</div>';
  }
  const cls = 'q' + (r ? (situacao(q) === 'acertou' ? ' acertou' : ' errou') : '');
  return '<article class="' + cls + '" data-id="' + q.id + '" id="q-' + bloco + '-' + q.id + '"><div class="meta"><span class="chip aut">Item ' + esc(q.n) + '</span><span>Subitem ' + esc(q.t) + ' do edital · inédito, padrão Cebraspe</span></div><div class="enun"><p>' + esc(q.e) + '</p></div>' + opts + corpo + '</article>';
}

function contagem(t) {
  const lista = listaDe(t), f = lista.filter(q => resp[q.id]);
  return lista.length + ' itens · ' + f.length + ' respondidos · ' + f.filter(q => situacao(q) === 'acertou').length + ' acertos';
}

function desenhaBloco(el) {
  const t = el.dataset.t, chave = t.replace('.', '_');
  const lista = listaDe(t);
  if (t === 'REL' && !lista.length) { el.innerHTML = '<p class="vazio">Toque em "Sortear 20 itens" para montar uma prova.</p>'; return; }
  const f = filtro[t] || 'todas';
  const revelar = document.documentElement.classList.contains('modo-pdf') || el.dataset.revelar === '1';
  const vis = lista.filter(q => f === 'todas' || (f === 'novas' && !resp[q.id]) || (f === 'erradas' && situacao(q) === 'errou'));
  el.innerHTML = '<div class="qbar"><span class="conta">' + contagem(t) + '</span><div class="ctrl">' +
    [['todas', 'Todos'], ['novas', 'Não respondidos'], ['erradas', 'Errados']].map(([k, v]) => '<button type="button" data-filtro="' + k + '" aria-pressed="' + (f === k) + '">' + v + '</button>').join('') +
    '<button type="button" data-revelar aria-pressed="' + (el.dataset.revelar === '1') + '">Mostrar gabaritos</button></div></div>' +
    '<div class="qlist">' + (vis.length ? vis.map(q => htmlQuestao(q, revelar, chave)).join('') : '<p class="vazio">Nenhum item neste filtro.</p>') + '</div>';
}

function desenhaPlacar() {
  let totF = 0, totA = 0, totQ = 0;
  document.getElementById('placar').innerHTML = ORDEM.map(t => {
    const lista = DADOS.filter(q => q.t === t), f = lista.filter(q => resp[q.id]), a = f.filter(q => situacao(q) === 'acertou').length;
    totF += f.length; totA += a; totQ += lista.length;
    const pa = a / lista.length * 100, pe = (f.length - a) / lista.length * 100;
    return '<div class="barra"><span class="rot">' + ROTULOS[t] + '</span><span class="trilho" role="img" aria-label="' + a + ' acertos e ' + (f.length - a) + ' erros em ' + lista.length + '"><i class="ok" style="width:' + pa + '%"></i><i class="bad" style="width:' + pe + '%"></i></span><span class="val">' + f.length + '/' + lista.length + '</span></div>';
  }).join('');
  const pct = totF ? Math.round(totA / totF * 100) : 0;
  document.getElementById('placar-total').innerHTML = '<span><b>' + totF + '</b> de ' + totQ + ' respondidos</span><span><b>' + pct + '%</b> de acerto</span>';
}

function redesenha() { document.querySelectorAll('.qbloco').forEach(desenhaBloco); desenhaPlacar(); }

document.addEventListener('click', ev => {
  const op = ev.target.closest('.opt');
  if (op && !op.disabled) {
    const q = porId[op.dataset.q]; resp[q.id] = op.dataset.op; salvar();
    document.querySelectorAll('.qbloco').forEach(bl => {
      const art = bl.querySelector('article[data-id="' + q.id + '"]');
      if (art) { art.outerHTML = htmlQuestao(q, bl.dataset.revelar === '1', bl.dataset.t.replace('.', '_')); const c = bl.querySelector('.conta'); if (c) c.textContent = contagem(bl.dataset.t); }
    });
    desenhaPlacar(); return;
  }
  const fb = ev.target.closest('[data-filtro]');
  if (fb) { const bl = fb.closest('.qbloco'); filtro[bl.dataset.t] = fb.dataset.filtro; desenhaBloco(bl); return; }
  const rv = ev.target.closest('[data-revelar]');
  if (rv) { const bl = rv.closest('.qbloco'); bl.dataset.revelar = bl.dataset.revelar === '1' ? '0' : '1'; desenhaBloco(bl); return; }
});

document.getElementById('btn-sorteio').addEventListener('click', () => {
  const ids = DADOS.map(q => q.id);
  for (let i = ids.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [ids[i], ids[j]] = [ids[j], ids[i]]; }
  sorteio = ids.slice(0, 20);
  const bl = document.querySelector('.qbloco[data-t="REL"]'); bl.dataset.revelar = '0'; filtro.REL = 'todas'; desenhaBloco(bl);
});

const bReset = document.getElementById('btn-reset'), bOk = document.getElementById('btn-reset-ok'), aviso = document.getElementById('aviso-reset');
bReset.addEventListener('click', () => { const abre = bOk.hidden; bOk.hidden = !abre; aviso.hidden = !abre; bReset.textContent = abre ? 'Cancelar' : 'Zerar respostas'; });
bOk.addEventListener('click', () => { resp = {}; salvar(); bOk.hidden = true; aviso.hidden = true; bReset.textContent = 'Zerar respostas'; redesenha(); });

(function () {
  const prova = new Date(2027, 0, 17), hoje = new Date(); hoje.setHours(0, 0, 0, 0);
  const d = Math.round((prova - hoje) / 864e5), el = document.getElementById('contagem');
  if (d > 1) el.innerHTML = 'Faltam <b>' + d + ' dias</b>';
  else if (d === 1) el.innerHTML = '<b>A prova é amanhã</b>';
  else if (d === 0) el.innerHTML = '<b>A prova é hoje</b>';
  else el.innerHTML = 'Prova realizada';
})();

if (location.hash === '#pdf') document.documentElement.classList.add('modo-pdf');
redesenha();
