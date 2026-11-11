"""Monta a página: questoes.json + comentarios.py + extras.py + estilo + corpo*.html + script.js.

Uso: python3 fontes/build.py pagina.html
"""
import json, os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from comentarios import C
from extras import CAMARA_2026, SIM_P1, EXAMINADOR

def topico(q):
    a, cad = q['assunto'], q['caderno']
    if cad == 'DEC':
        if '7.983' in a: return 'O-DEC'
        if '11.246' in a: return 'L-FISC'
        if 'IN SEGES' in a: return 'L-MOD'
        return 'L-PRIN'
    if cad == 'LIC':
        regras = [('L-DIR', 'Contratação Direta'), ('L-MOD', 'Modalidades|Critérios|Instrumentos Auxiliares|Alienações'),
                  ('L-PLAN', 'Definições|Instrução|Disposições Setoriais|Fases da Licitação'),
                  ('L-FISC', 'Execução dos Contratos|Recebimento'),
                  ('L-CONT', 'Contratos Administrativos|Garantias|Riscos|Duração|Alteração|Extinção|Pagamentos|Meios Alternativos|Infrações')]
        for t, rx in regras:
            if re.search(rx, a): return t
        return 'L-PRIN'
    regras = [('O-PERT', 'PERT'), ('O-BDI', 'BDI'), ('O-CPU', 'SINAPI|Composições|Levantamento|Curva ABC'),
              ('O-CRON', 'Cronograma|Curva S|Gantt|Histograma|GVA|Fases de Planejamento|Apropriação'),
              ('F-MED', 'Acompanhamento da Aplicação'), ('F-DOC', 'Documentação|Recebimento|Fiscal e Gestor'),
              ('F-MAN', 'NBR 5674|Locação')]
    for t, rx in regras:
        if re.search(rx, a): return t
    raise ValueError(a)

NOMES = {'LIC': 'Caderno Licitação e Contratos', 'DEC': 'Caderno Dec. 7.983 e 11.246', 'C03': 'Caderno 03', 'C04': 'Caderno 04'}
qs = json.load(open(os.path.join(AQUI, 'questoes.json'), encoding='utf-8'))
dados, vistos = [], {}
for i, q in enumerate(qs):
    ref = '%s, nº %d' % (NOMES[q['caderno']], q['num'])
    if q['id'] in vistos:
        vistos[q['id']]['fonte'] += ' · ' + ref
        continue
    c, a = C[q['id']]
    d = {'id': q['id'], 't': topico(q), 'tipo': q['tipo'], 'enunciado': q['enunciado'], 'opcoes': q['opcoes'],
         'gab': q['gabarito'], 'ano': q['ano'], 'fonte': 'Cebraspe · %s · %d · %s' % (q['prova'], q['ano'], ref),
         'camara': False, 'origem': 'tec', 'ord': i, 'c': c, 'a': a}
    vistos[q['id']] = d
    dados.append(d)
for j, (i, n, enun, gab, c, a) in enumerate(CAMARA_2026):
    dados.append({'id': i, 't': 'CAM', 'tipo': 'CE', 'enunciado': [enun], 'opcoes': [], 'gab': gab, 'ano': 2026,
                  'fonte': 'Cebraspe · Câmara dos Deputados · Policial Legislativo · 2026 · Conhecimentos Gerais, item %d · gabarito definitivo' % n,
                  'camara': True, 'origem': 'camara2026', 'ord': 1000 + j, 'c': c, 'a': a})
for n, (enun, gab, c, a) in enumerate(SIM_P1, 1):
    dados.append({'id': 'simp1-%02d' % n, 't': 'SIMP1', 'n': n, 'tipo': 'CE', 'enunciado': [enun], 'opcoes': [], 'gab': gab,
                  'ano': 2027, 'fonte': '', 'camara': False, 'origem': 'autoral', 'ord': 2000 + n, 'c': c, 'a': a})
cont = {}
for k, (t, enun, gab, c, a) in enumerate(EXAMINADOR):
    cont[t] = cont.get(t, 0) + 1
    dados.append({'id': '%s-%02d' % (t.lower(), cont[t]), 't': t, 'n': cont[t], 'tipo': 'CE', 'enunciado': [enun], 'opcoes': [],
                  'gab': gab, 'ano': 2027, 'fonte': '', 'camara': False, 'origem': 'autoral', 'ord': 3000 + k, 'c': c, 'a': a})

# mais recentes primeiro dentro de cada tópico; itens inéditos na ordem
dados.sort(key=lambda d: (d['origem'] == 'autoral', -d['ano'] if d['origem'] != 'autoral' else 0, d['ord']))
for d in dados: d.pop('ord')

ceb = [d for d in dados if d['origem'] in ('tec', 'camara2026')]
ler = lambda n: open(os.path.join(AQUI, n), encoding='utf-8').read()
cabeca = ('<title>Licitações, Orçamento e Fiscalização</title>\n'
          '<meta name="description" content="Estudo para a Câmara dos Deputados (Cebraspe, 17/01/2027), Analista Legislativo – Engenharia Civil: '
          'Lei 14.133/2021, Decretos 7.983/2013 e 11.246/2022, orçamento e fiscalização de obras, ' + str(len(dados)) + ' questões comentadas, simulado e discursivas.">\n'
          '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
          '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,500;7..72,600;7..72,700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">\n')
extra_css = ('<style>.barra{grid-template-columns:8.5rem 1fr 4.5rem}.barra .rot{color:var(--ink);text-decoration:none}.barra .rot:hover{color:var(--accent)}'
             'ol.tight{padding-left:1.3rem}ol.tight li{margin:.3rem 0}.box p:last-child{margin-bottom:0}'
             '@media (max-width:30rem){.barra{grid-template-columns:6.5rem 1fr 3.5rem}}</style>\n')
corpo = ''.join(ler('corpo%d.html' % k) for k in range(1, 7))
js = json.dumps(dados, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html = cabeca + ler('estilo.css.html') + extra_css + corpo + ler('script.js').replace('/*__DADOS__*/[]', js)
html = html.replace('__NTOTAL__', str(len(dados))).replace('__NCEB__', str(len(ceb)))
open(sys.argv[1], 'w', encoding='utf-8').write(html)
por_t = {}
for d in dados: por_t[d['t']] = por_t.get(d['t'], 0) + 1
print('questões:', len(dados), 'cebraspe:', len(ceb), 'bytes:', len(html.encode()))
print(por_t)
