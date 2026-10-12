"""Monta a página de Governança e Gestão Pública: estilo do estudo anterior + corpo + itens + script."""
import json, os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from itens import ITENS

estilo_base = open(sys.argv[1], encoding='utf-8').read()   # template.html do estudo de responsabilidade civil
estilo = re.search(r'<style>.*?</style>', estilo_base, re.S).group(0)
fontes = re.search(r'<link rel="preconnect".*?display=swap">', estilo_base, re.S).group(0)
corpo = open(os.path.join(AQUI, 'corpo.html'), encoding='utf-8').read()
script = open(os.path.join(AQUI, 'script.js'), encoding='utf-8').read()

dados = []
cont = {}
for i, t, e, g, c, a in ITENS:
    assert g in ('Certo', 'Errado'), i
    cont[t] = cont.get(t, 0) + 1
    dados.append({'id': i, 't': t, 'n': '%s.%d' % (t, cont[t]), 'e': e, 'gab': g, 'c': c, 'a': a})
js = json.dumps(dados, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
cab = ('<title>Governança e Gestão Pública</title>\n'
       '<meta name="description" content="Estudo dos tópicos 8 e 9 do edital da Câmara dos Deputados (Cebraspe): modelos de gestão, Nova Governança Pública, valor público e Decreto 9.203/2017.">\n')
html = (cab + fontes + '\n' + estilo + '\n<style>html.modo-pdf #relampago { display: none !important; }</style>\n' + corpo.replace('__NTOTAL__', str(len(dados))) +
        '\n<script>\n' + script.replace('/*__DADOS__*/[]', js) + '</script>\n')
open(sys.argv[2], 'w', encoding='utf-8').write(html)
from collections import Counter
print(len(dados), dict(Counter(d['t'] for d in dados)), Counter(d['gab'] for d in dados))
