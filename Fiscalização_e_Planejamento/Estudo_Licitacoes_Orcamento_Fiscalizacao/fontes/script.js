<script>
const DADOS = /*__DADOS__*/[];
const CHAVE = 'licit-orc-fisc-v1';
const ROTULOS = {
  'CAM': 'Câmara 2026', 'L-PRIN': '1.1 Princípios', 'L-MOD': '1.2 Modalidades', 'L-DIR': '1.3 Contr. direta',
  'L-PLAN': '1.4 Planejamento', 'L-CONT': '1.5 Contratos', 'L-FISC': '1.6 Fiscalização', 'EX1': 'Examinador B1',
  'O-DEC': '2.2 Dec. 7.983', 'O-BDI': '2.3 BDI', 'O-CPU': '2.4 Composições', 'O-CRON': '2.5 Cronograma', 'O-PERT': '2.6 PERT-CPM', 'EX2': 'Examinador B2',
  'F-MED': '3.1 Medições', 'F-DOC': '3.3 Execução', 'F-MAN': '3.4 Normas', 'EX3': 'Examinador B3', 'SIMP1': 'Simulado P1'
};
const ORDEM = Object.keys(ROTULOS);
let resp = {};
try { resp = JSON.parse(localStorage.getItem(CHAVE) || '{}') || {}; } catch (e) { resp = {}; }
function salvar() { try { localStorage.setItem(CHAVE, JSON.stringify(resp)); } catch (e) {} }

const porId = {}; DADOS.forEach(q => porId[q.id] = q);
const filtro = {};

function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }
function gabLetra(q) { return q.tipo === 'CE' ? (q.gab === 'Certo' ? 'C' : q.gab === 'Errado' ? 'E' : null) : (q.gab.length === 1 ? q.gab.toLowerCase() : null); }
function situacao(q) {
  const r = resp[q.id]; if (!r) return 'nova';
  return r === gabLetra(q) ? 'acertou' : 'errou';
}

function htmlQuestao(q, revelar) {
  const r = resp[q.id];
  const mostra = revelar || !!r;
  const certa = gabLetra(q);
  const chips = [];
  if (q.camara) chips.push('<span class="chip cam">Câmara</span>');
  if (q.origem === 'autoral') chips.push('<span class="chip aut">Inédita</span>');
  const meta = q.origem === 'autoral' ? (q.t === 'SIMP1' ? 'Simulado P1 · item ' + q.n : 'Examinador · item ' + q.n) : esc(q.fonte);
  const enun = q.enunciado.map(p => '<p' + (/^(I|II|III|IV|V)\s/.test(p) ? ' class="it"' : '') + '>' + esc(p) + '</p>').join('');
  let opts;
  if (q.tipo === 'CE') {
    opts = '<div class="opts ce">' + [['C', 'Certo'], ['E', 'Errado']].map(([l, t]) => {
      let cls = 'opt';
      if (mostra && certa === l) cls += ' certa';
      if (r === l && certa && r !== certa) cls += ' marcada-errada';
      return '<button type="button" class="' + cls + '" data-q="' + q.id + '" data-op="' + l + '"' + (r ? ' disabled' : '') + ' aria-pressed="' + (r === l) + '">' + t + '</button>';
    }).join('') + '</div>';
  } else {
    opts = '<div class="opts">' + q.opcoes.map(([l, t]) => {
      let cls = 'opt';
      if (mostra && certa === l) cls += ' certa';
      if (r === l && certa && r !== certa) cls += ' marcada-errada';
      return '<button type="button" class="' + cls + '" data-q="' + q.id + '" data-op="' + l + '"' + (r ? ' disabled' : '') + ' aria-pressed="' + (r === l) + '"><span class="l">' + l + ')</span><span>' + esc(t) + '</span></button>';
    }).join('') + '</div>';
  }
  let corpo = '';
  if (mostra) {
    let ver, vcls;
    if (!r) { ver = 'Gabarito: ' + q.gab; vcls = 'neu'; }
    else if (situacao(q) === 'acertou') { ver = 'Acertou · gabarito ' + q.gab; vcls = 'ok'; }
    else { ver = 'Errou · gabarito ' + q.gab; vcls = 'bad'; }
    corpo = '<div class="resp"><div class="veredito ' + vcls + '">' + ver + '</div><p>' + esc(q.c) + '</p>' +
      (q.a ? '<div class="alerta"><b>Pegadinha:</b> ' + esc(q.a) + '</div>' : '') + '</div>';
  }
  const cls = 'q' + (r ? (situacao(q) === 'acertou' ? ' acertou' : ' errou') : '');
  return '<article class="' + cls + '" id="q-' + q.id + '"><div class="meta">' + chips.join('') + '<span>' + meta + '</span></div><div class="enun">' + enun + '</div>' + opts + corpo + '</article>';
}

function contaTexto(lista) {
  const feitas = lista.filter(q => resp[q.id]);
  return lista.length + ' questões · ' + feitas.length + ' respondidas · ' + feitas.filter(q => situacao(q) === 'acertou').length + ' acertos';
}

function desenhaBloco(el) {
  const t = el.dataset.t;
  const lista = DADOS.filter(q => q.t === t);
  const f = filtro[t] || 'todas';
  const revelar = document.documentElement.classList.contains('modo-pdf') || el.dataset.revelar === '1';
  const vis = lista.filter(q => f === 'todas' || (f === 'novas' && !resp[q.id]) || (f === 'erradas' && situacao(q) === 'errou'));
  el.innerHTML = '<div class="qbar"><span class="conta">' + contaTexto(lista) + '</span><div class="ctrl">' +
    [['todas', 'Todas'], ['novas', 'Não respondidas'], ['erradas', 'Erradas']].map(([k, v]) => '<button type="button" data-filtro="' + k + '" aria-pressed="' + (f === k) + '">' + v + '</button>').join('') +
    '<button type="button" data-revelar aria-pressed="' + (el.dataset.revelar === '1') + '">Mostrar gabaritos</button></div></div>' +
    '<div class="qlist">' + (vis.length ? vis.map(q => htmlQuestao(q, revelar)).join('') : '<p class="vazio">Nenhuma questão neste filtro.</p>') + '</div>';
}

function desenhaPlacar() {
  let totF = 0, totA = 0, totQ = 0;
  document.getElementById('placar').innerHTML = ORDEM.map(t => {
    const lista = DADOS.filter(q => q.t === t);
    const f = lista.filter(q => resp[q.id]); const a = f.filter(q => situacao(q) === 'acertou').length;
    totF += f.length; totA += a; totQ += lista.length;
    const pa = lista.length ? a / lista.length * 100 : 0, pe = lista.length ? (f.length - a) / lista.length * 100 : 0;
    return '<div class="barra"><a class="rot" href="#t-' + t + '">' + ROTULOS[t] + '</a><span class="trilho" role="img" aria-label="' + a + ' acertos e ' + (f.length - a) + ' erros em ' + lista.length + '"><i class="ok" style="width:' + pa + '%"></i><i class="bad" style="width:' + pe + '%"></i></span><span class="val">' + f.length + '/' + lista.length + '</span></div>';
  }).join('');
  const pct = totF ? Math.round(totA / totF * 100) : 0;
  document.getElementById('placar-total').innerHTML = '<span><b>' + totF + '</b> de ' + totQ + ' respondidas</span><span><b>' + pct + '%</b> de acerto</span><span><b>' + (totA - (totF - totA)) + '</b> pontos líquidos (acertos − erros)</span>';
}

function redesenha(t) {
  document.querySelectorAll('.qbloco').forEach(el => { if (!t || el.dataset.t === t) desenhaBloco(el); });
  desenhaPlacar();
}

document.addEventListener('click', ev => {
  const op = ev.target.closest('.opt');
  if (op && !op.disabled) {
    const q = porId[op.dataset.q]; resp[q.id] = op.dataset.op; salvar();
    const art = document.getElementById('q-' + q.id);
    const bloco = art.closest('.qbloco');
    art.outerHTML = htmlQuestao(q, bloco.dataset.revelar === '1');
    desenhaPlacar();
    bloco.querySelector('.conta').textContent = contaTexto(DADOS.filter(x => x.t === bloco.dataset.t));
    return;
  }
  const fb = ev.target.closest('[data-filtro]');
  if (fb) { const bl = fb.closest('.qbloco'); filtro[bl.dataset.t] = fb.dataset.filtro; desenhaBloco(bl); return; }
  const rv = ev.target.closest('[data-revelar]');
  if (rv) { const bl = rv.closest('.qbloco'); bl.dataset.revelar = bl.dataset.revelar === '1' ? '0' : '1'; desenhaBloco(bl); return; }
});

const bReset = document.getElementById('btn-reset'), bOk = document.getElementById('btn-reset-ok'), aviso = document.getElementById('aviso-reset');
bReset.addEventListener('click', () => { const abre = bOk.hidden; bOk.hidden = !abre; aviso.hidden = !abre; bReset.textContent = abre ? 'Cancelar' : 'Zerar respostas'; });
bOk.addEventListener('click', () => { resp = {}; salvar(); bOk.hidden = true; aviso.hidden = true; bReset.textContent = 'Zerar respostas'; redesenha(); });

// âncoras dos blocos de questões e contagens da tabela do mapa
document.querySelectorAll('.qbloco').forEach(el => { el.id = 't-' + el.dataset.t; });
document.querySelectorAll('[data-cnt]').forEach(el => {
  const ts = el.dataset.cnt.split(' ');
  el.textContent = DADOS.filter(q => q.origem !== 'autoral' && ts.includes(q.t)).length;
});

// contagem regressiva
(function () {
  const prova = new Date(2027, 0, 17), hoje = new Date(); hoje.setHours(0, 0, 0, 0);
  const d = Math.round((prova - hoje) / 864e5);
  const el = document.getElementById('contagem');
  if (d > 1) el.innerHTML = 'Faltam <b>' + d + ' dias</b>';
  else if (d === 1) el.innerHTML = '<b>A prova é amanhã</b>';
  else if (d === 0) el.innerHTML = '<b>A prova é hoje</b>';
  else el.innerHTML = 'Prova realizada';
})();

if (location.hash === '#pdf') document.documentElement.classList.add('modo-pdf');
redesenha();
</script>
