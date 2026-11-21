#!/usr/bin/env python3
"""Gera a página de estudo (interativa) e a versão de impressão usada para o PDF.
Uso: python3 build.py   (dentro de fontes/)"""
import json, html, datetime, os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import simulados_blocos as SB, simulados_bloco2 as S2, plano

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.dirname(AQUI)
banco = json.load(open(os.path.join(AQUI, 'banco_itens.json'), encoding='utf-8'))

items, sims = [], []
for s in S2.SIMULADOS_B2:
    ids = []
    for k, (top, org, txt, gab, com) in enumerate(s['itens'], 1):
        iid = f"{s['id']}-{k:02d}"
        items.append(dict(id=iid, sim=s['id'], bloco=2, top=top, org=org, ctx="", txt=txt, gab=gab, com=com))
        ids.append(iid)
    sims.append(dict(id=s['id'], titulo=s['titulo'], bloco=2, itens=ids))

for s in SB.SIMULADOS:
    ids = []
    for k, (idx, com) in enumerate(s['itens'], 1):
        b = banco[idx]
        iid = f"{s['id']}-{k:02d}"
        txt = SB.TEXTO_FIX.get(idx, b['text']).strip()
        ctx = SB.CTX_FIX.get(idx, b['ctx']).strip()
        # limpa restos de cabeçalho de caderno no comando
        for lixo in ['-- CONHECIMENTO', 'OS ESPECÍFICOS --', 'OS ESPECÍFICOS', 'CONHECIMENTO']:
            ctx = ctx.replace(lixo, '').strip(' -–')
        ctx = re.sub(r'\(cid:\d+\)', '', ctx)
        ctx = re.sub(r'^\s*\d+\s*[–-]\s*', '', ctx)
        ctx = re.sub(r'julgue os itens de \d+ a \d+', 'julgue o item', ctx)
        ctx = ctx.replace('Jugue', 'Julgue').strip()
        if 'Controle Externo' in ctx and 'Considerando' in ctx: ctx = ctx[ctx.index('Considerando'):]
        if len(ctx) > 420: ctx = ''
        org = f"Real · {b['exam']}, item {b['n']} (gabarito oficial definitivo)"
        items.append(dict(id=iid, sim=s['id'], bloco=s['bloco'], top=None, org=org, ctx=ctx, txt=txt, gab=b['gab'], com=com))
        ids.append(iid)
    sims.append(dict(id=s['id'], titulo=s['titulo'], bloco=s['bloco'], itens=ids))

topicos = [
    dict(id='banca', curto='Como a banca pensa', nome='Como o examinador pensa'),
    dict(id='ele', curto='2.1 Elétricas', nome=S2.TOPICOS['ele']),
    dict(id='inc', curto='2.5 Incêndio', nome=S2.TOPICOS['inc']),
    dict(id='arq', curto='2.7 Arquitetônicos', nome=S2.TOPICOS['arq']),
    dict(id='ar', curto='2.4 Ar-condicionado', nome=S2.TOPICOS['ar']),
    dict(id='vent', curto='2.3 Ventilação', nome=S2.TOPICOS['vent']),
    dict(id='elev', curto='2.2 Elevadores', nome=S2.TOPICOS['elev']),
    dict(id='tel', curto='2.6 Telefonia', nome=S2.TOPICOS['tel']),
    dict(id='numeros', curto='Tabela-relâmpago', nome='Tabela-relâmpago'),
]

teoria = open(os.path.join(AQUI, 'teoria.html'), encoding='utf-8').read()
for top, lst in S2.EXTRAS.items():
    blocos = []
    for org, txt, gab, com in lst:
        g = {'C': 'C', 'E': 'E', 'X': 'X'}.get(gab, '–')
        lbl = {'C': 'C', 'E': 'E', 'X': 'anulado'}.get(gab, 'ver')
        blocos.append(f'<details><summary>{html.escape(txt)} <span class="g {g}">{lbl}</span></summary>'
                      f'<p class="note">{html.escape(org)}</p>{"<p>"+html.escape(com)+"</p>" if com else ""}</details>')
    bloco_html = f'<div class="extras"><h3>Itens reais comentados ({len(lst)})</h3>{"".join(blocos)}</div>'
    teoria = teoria.replace(f'<!--EXTRAS:{top}-->', bloco_html)

data = dict(items=items, sims=sims, topicos=topicos, plano=plano.plano_json())
tpl = open(os.path.join(AQUI, 'template.html'), encoding='utf-8').read()
rev = datetime.date.today().strftime('%d/%m/%Y')
out = (tpl.replace('__TEORIA__', teoria)
          .replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
          .replace('__REV__', rev)
          .replace('__NSIM__', str(len(sims)))
          .replace('__NITENS__', str(len(items))))
pag = os.path.join(AQUI, '_artifact.html')  # versão publicada como Artifact (sem doctype)
open(pag, 'w', encoding='utf-8').write(out)
# versão de impressão: documento completo + flag
imp = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">' \
      '<script>window.PRINT_MODE=true</script></head><body>' + out + '</body></html>'
open(os.path.join(AQUI, '_impressao.html'), 'w', encoding='utf-8').write(imp)
# versão autônoma para abrir direto do computador (com doctype)
std = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"></head><body>' + out + '</body></html>'
open(os.path.join(SAIDA, 'Camara_2027_Engenharia.html'), 'w', encoding='utf-8').write(std)
print(len(items), 'itens;', len(sims), 'simulados;', round(len(out)/1024), 'KB')
