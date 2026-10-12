"""Monta a página de estudo: questoes.json + comentarios.py + extras.py + template.html."""
import json, os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from comentarios import C
from extras import CAMARA_2012, SIMULADO

qs = json.load(open(os.path.join(AQUI, 'questoes.json'), encoding='utf-8'))
dados = []
for i, q in enumerate(qs):
    cad = []
    if 'num06' in q: cad.append('Caderno 06, nº %d' % q['num06'])
    if 'num07' in q: cad.append('Caderno 07, nº %d' % q['num07'])
    com = C[q['id']]
    dados.append({'id': q['id'], 't': com['t'], 'tipo': q['tipo'], 'enunciado': q['enunciado'],
                  'opcoes': q['opcoes'], 'gab': q['gabarito'], 'ano': q['ano'],
                  'fonte': 'Cebraspe · %s · %d · %s' % (q['prova'], q['ano'], ' · '.join(cad)),
                  'camara': 'CAM DEP' in q['prova'], 'origem': 'tec', 'ord': i,
                  'c': com['c'], 'a': com['a']})
for j, q in enumerate(CAMARA_2012):
    com = C[q['id']]
    dados.append({'id': q['id'], 't': com['t'], 'tipo': 'CE', 'enunciado': q['enunciado'], 'opcoes': [],
                  'gab': q['gabarito'], 'ano': 2012, 'fonte': 'Cebraspe · %s · 2012 · gabarito definitivo' % q['prova'],
                  'camara': True, 'origem': 'camara2012', 'ord': 1000 + j, 'c': com['c'], 'a': com['a']})
for n, (i, t, enun, gab, com, alerta) in enumerate(SIMULADO, 1):
    dados.append({'id': i, 't': 'SIM', 'tema': t, 'n': n, 'tipo': 'CE', 'enunciado': [enun], 'opcoes': [],
                  'gab': gab, 'ano': 2027, 'fonte': '', 'camara': False, 'origem': 'autoral', 'ord': 2000 + n,
                  'c': 'Item do edital: %s. %s' % (t.replace('A', ' (A)').replace('B', ' (B)').replace('C', ' (C)').replace('D', ' (D)'), com), 'a': alerta})

# mais recentes primeiro dentro de cada item; simulado na ordem
dados.sort(key=lambda d: (d['origem'] == 'autoral', -d['ano'] if d['origem'] != 'autoral' else 0, d['ord']))
for d in dados: d.pop('ord')

ceb = [d for d in dados if d['origem'] == 'tec']
tpl = open(os.path.join(AQUI, 'template.html'), encoding='utf-8').read()
js = json.dumps(dados, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html = (tpl.replace('/*__DADOS__*/[]', js)
           .replace('__NTOTAL__', str(len(dados)))
           .replace('__NCEB__', str(len(ceb))))
saida = sys.argv[1]
open(saida, 'w', encoding='utf-8').write(html)
print('questões:', len(dados), 'cebraspe:', len(ceb), 'bytes:', len(html.encode()))
# conferência: números de palavras-chave
chave = re.compile(r'risco administrativo|risco integral|nexo|concorrente|exclusiva|regresso|dolo ou culpa', re.I)
n = sum(1 for d in ceb if chave.search(' '.join(d['enunciado']) + ' ' + ' '.join(o[1] for o in d['opcoes'])))
print('itens com o núcleo (risco/nexo/culpa da vítima/regresso):', n)
