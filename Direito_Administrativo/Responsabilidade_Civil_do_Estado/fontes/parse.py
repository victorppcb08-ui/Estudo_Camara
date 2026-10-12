"""Extrai as questões dos cadernos do TEC (texto do pdftotext -layout) para JSON."""
import json, re, sys

def limpa(linhas):
    out = []
    for l in linhas:
        l = l.replace('\f', '')
        if re.match(r'^\d\d/\d\d/\d{4}, \d\d:\d\d', l) or 'tecconcursos.com.br/questoes/cadernos' in l:
            continue
        out.append(l.rstrip())
    return out

def parse(caminho, caderno):
    linhas = limpa(open(caminho, encoding='utf-8').read().split('\n'))
    blocos, atual = [], None
    for l in linhas:
        m = re.match(r'^\s*www\.tecconcursos\.com\.br/questoes/(\d+)\s*$', l)
        if m:
            atual = {'id': m.group(1), 'linhas': []}
            blocos.append(atual)
        elif atual is not None:
            atual['linhas'].append(l)
    qs = []
    for b in blocos:
        ls = [l for l in b['linhas']]
        while ls and not ls[0].strip():
            ls.pop(0)
        def prox():
            while not ls[0].strip():
                ls.pop(0)
            return ls.pop(0).strip()
        cab = prox()
        # assunto pode quebrar em 2 linhas
        assunto = prox()
        while not ls[0].strip():
            ls.pop(0)
        if not re.match(r'^\s*\d+\)', ls[0]):
            assunto += ' ' + prox()
        while not ls[0].strip():
            ls.pop(0)
        m = re.match(r'^\s*(\d+)\)\s*(.*)$', ls[0])
        num = int(m.group(1)); ls[0] = m.group(2)
        gab = None
        corpo = []
        for l in ls:
            g = re.match(r'^\s*Gabarito:\s*(.+)$', l)
            if g:
                gab = g.group(1).strip(); break
            corpo.append(l)
        # separa enunciado / opções
        enun, opts, tipo = [], [], 'ME'
        modo = 'enun'
        for l in corpo:
            s = l.strip()
            if re.match(r'^(Certo|Errado)$', s):
                tipo = 'CE'; modo = 'fim'; continue
            mo = re.match(r'^\s{3,}([a-e])\)\s+(.*)$', l)
            if mo and modo in ('enun', 'opt'):
                opts.append([mo.group(1), mo.group(2).strip()]); modo = 'opt'; continue
            if modo == 'opt':
                if s:
                    opts[-1][1] += ' ' + s
                continue
            if modo == 'enun':
                enun.append(l)
        # parágrafos do enunciado
        pars, buf = [], []
        for l in enun:
            s = l.strip()
            if not s:
                if buf: pars.append(' '.join(buf)); buf = []
                continue
            if re.match(r'^(I|II|III|IV|V|VI)\s', s) and buf:
                pars.append(' '.join(buf)); buf = []
            buf.append(s)
        if buf: pars.append(' '.join(buf))
        m = re.match(r'CEBRASPE \(CESPE\) - (.*)/(\d{4})$', cab)
        qs.append({'id': b['id'], 'cab': cab, 'prova': m.group(1) if m else cab,
                   'ano': int(m.group(2)) if m else None,
                   'assunto': assunto.replace('Direito Administrativo (Doutrina e Leis Federais) - ', ''),
                   'caderno': caderno, 'num': num, 'tipo': tipo, 'enunciado': pars,
                   'opcoes': opts, 'gabarito': gab})
    return qs

q06 = parse(sys.argv[1], '06'); q07 = parse(sys.argv[2], '07')
por_id = {}
for q in q06 + q07:
    if q['id'] in por_id:
        por_id[q['id']]['caderno'] += '+' + q['caderno']
        por_id[q['id']].setdefault('num07', q['num'])
    else:
        q['num06' if q['caderno'] == '06' else 'num07'] = q['num']
        por_id[q['id']] = q
for q in por_id.values():
    q.pop('num', None)
json.dump(list(por_id.values()), open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(q06), len(q07), len(por_id))
