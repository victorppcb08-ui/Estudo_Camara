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
        ls = list(b['linhas'])
        def pula():
            while ls and not ls[0].strip(): ls.pop(0)
        def prox():
            pula(); return ls.pop(0).strip()
        cab = prox()
        while not re.search(r'/\d{4}$', cab):
            cab += ' ' + prox()
        assunto = prox()
        pula()
        while not re.match(r'^\s*\d+\)', ls[0]):
            assunto += ' ' + prox(); pula()
        m = re.match(r'^\s*(\d+)\)\s*(.*)$', ls[0])
        num = int(m.group(1)); ls[0] = m.group(2)
        gab, corpo = None, []
        for l in ls:
            g = re.match(r'^\s*Gabarito:\s*(.+)$', l)
            if g: gab = g.group(1).strip(); break
            corpo.append(l)
        enun, opts, tipo, modo = [], [], 'ME', 'enun'
        for l in corpo:
            s = l.strip()
            if re.match(r'^(Certo|Errado)$', s):
                tipo = 'CE'; modo = 'fim'; continue
            mo = re.match(r'^\s{3,}([a-e])\)\s+(.*)$', l)
            if mo and modo in ('enun', 'opt'):
                opts.append([mo.group(1), mo.group(2).strip()]); modo = 'opt'; continue
            if modo == 'opt':
                if s: opts[-1][1] += ' ' + s
                continue
            if modo == 'enun': enun.append(l)
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
        assunto = re.sub(r'^(Direito Administrativo \(Doutrina e Leis Federais\)|Engenharia Civil e Auditoria de Obras) - ', '', assunto)
        qs.append({'id': b['id'], 'cab': cab, 'prova': m.group(1) if m else cab,
                   'ano': int(m.group(2)) if m else None, 'assunto': assunto,
                   'caderno': caderno, 'num': num, 'tipo': tipo, 'enunciado': pars,
                   'opcoes': opts, 'gabarito': gab})
    return qs

if __name__ == '__main__':
    todas = []
    for arq, cad in zip(sys.argv[1:-1:2], sys.argv[2:-1:2]):
        q = parse(arq, cad); print(cad, len(q)); todas += q
    json.dump(todas, open(sys.argv[-1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
