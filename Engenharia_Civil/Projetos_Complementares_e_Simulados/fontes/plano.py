# Cronograma de 21/11/2026 a 17/01/2027, com férias de 09/12 a 27/12.
# fase: base | blocos | ferias | reta | prova
import datetime as dt

D = dt.date
PLANO = [
 # Fase 1: Bloco 2 a fundo
 (D(2026,11,21), "base", "Ler 'Como o examinador pensa'. Elétrica: teoria completa + itens reais do tópico.", ["banca", "ele"]),
 (D(2026,11,22), "base", "Elétrica: SPDA e revisão dos números. Incêndio: teoria (classes, sistemas, SDAI).", ["ele", "inc"]),
 (D(2026,11,23), "base", "Incêndio: saídas de emergência e sprinklers. Simulado B2-1.", ["inc", "B2-1"]),
 (D(2026,11,24), "base", "Arquitetônicos: etapas, representação, NBR 9050 e NBR 15575. Simulado B2-2.", ["arq", "B2-2"]),
 (D(2026,11,25), "base", "Ar-condicionado e ventilação/exaustão (incluindo gás). Simulado B2-3.", ["ar", "vent", "B2-3"]),
 (D(2026,11,26), "base", "Elevadores e telefonia. Simulado B2-4.", ["elev", "tel", "B2-4"]),
 (D(2026,11,27), "base", "Simulado B2-5. Caderno de erros do Bloco 2: refazer tudo que errou ou deixou em branco.", ["B2-5", "erros"]),
 (D(2026,11,28), "blocos", "Tabela-relâmpago do Bloco 2. Bloco 1: simulado B1-1 + Caderno de Estruturas (repositório).", ["numeros", "B1-1"]),
 (D(2026,11,29), "blocos", "Bloco 1: simulados B1-2 e B1-3 + resumo NBR 5626 e guia NBR 6118 (repositório).", ["B1-2", "B1-3"]),
 # Fase 2: demais blocos
 (D(2026,11,30), "blocos", "Bloco 3: simulado B3-1 + estudo SINAPI (repositório).", ["B3-1"]),
 (D(2026,12,1), "blocos", "Bloco 3: simulado B3-2 + exercícios de PERT-CPM (folgas e caminho crítico à mão).", ["B3-2"]),
 (D(2026,12,2), "blocos", "Bloco 4: simulado B4-1 (sondagem, canteiro, NR-18, NR-35, fundações na obra).", ["B4-1"]),
 (D(2026,12,3), "blocos", "Bloco 4: simulado B4-2 (concreto, alvenaria, revestimentos, coberturas, esquadrias).", ["B4-2"]),
 (D(2026,12,4), "blocos", "Bloco 5: simulado B5-1 (manutenção, NBR 5674, NBR 14037, patologia).", ["B5-1"]),
 (D(2026,12,5), "blocos", "Bloco 5: simulado B5-2. Bloco 6: simulado B6-1.", ["B5-2", "B6-1"]),
 (D(2026,12,6), "blocos", "Bloco 6: simulado B6-2. Modo prova com 45 itens (todos os blocos).", ["B6-2", "prova"]),
 (D(2026,12,7), "blocos", "Caderno de erros completo: refazer só os itens errados ou em branco.", ["erros"]),
 (D(2026,12,8), "blocos", "Modo prova com 90 itens, cronometrado (2h15). Linha de base antes da viagem. Baixar o PDF no celular.", ["prova"]),
 # Fase 3: férias (modo manutenção, 30 a 40 min)
 (D(2026,12,9), "ferias", "Viagem. Só a tabela-relâmpago (10 min).", ["numeros"]),
 (D(2026,12,10), "ferias", "Simulado B2-1 refeito (sem consultar). 30 min.", ["B2-1"]),
 (D(2026,12,11), "ferias", "Folga.", []),
 (D(2026,12,12), "ferias", "Simulado B1-1. 30 min.", ["B1-1"]),
 (D(2026,12,13), "ferias", "Tabela-relâmpago + 'Onde a banca inverte' de elétrica e incêndio.", ["numeros"]),
 (D(2026,12,14), "ferias", "Simulado B3-1. 30 min.", ["B3-1"]),
 (D(2026,12,15), "ferias", "Folga.", []),
 (D(2026,12,16), "ferias", "Simulado B2-3 refeito.", ["B2-3"]),
 (D(2026,12,17), "ferias", "Simulado B4-1.", ["B4-1"]),
 (D(2026,12,18), "ferias", "Folga.", []),
 (D(2026,12,19), "ferias", "Simulado B5-1.", ["B5-1"]),
 (D(2026,12,20), "ferias", "Tabela-relâmpago + 'Como o examinador pensa' (releitura).", ["numeros", "banca"]),
 (D(2026,12,21), "ferias", "Simulado B6-1.", ["B6-1"]),
 (D(2026,12,22), "ferias", "Simulado B2-5 refeito.", ["B2-5"]),
 (D(2026,12,23), "ferias", "Folga.", []),
 (D(2026,12,24), "ferias", "Folga (Natal).", []),
 (D(2026,12,25), "ferias", "Folga (Natal).", []),
 (D(2026,12,26), "ferias", "Simulado B1-2.", ["B1-2"]),
 (D(2026,12,27), "ferias", "Retorno. Só a tabela-relâmpago.", ["numeros"]),
 # Fase 4: reta final
 (D(2026,12,28), "reta", "Refazer B2-1, B2-2 e B2-3. Meta: 100% no Bloco 2.", ["B2-1", "B2-2", "B2-3"]),
 (D(2026,12,29), "reta", "Refazer B2-4 e B2-5. Reler os comentários de todo item que errou.", ["B2-4", "B2-5"]),
 (D(2026,12,30), "reta", "Bloco 1: refazer B1-1 a B1-3 só nos erros + guia NBR 6118.", ["B1-1", "B1-2", "B1-3"]),
 (D(2026,12,31), "reta", "Blocos 3 e 4: refazer só os erros. Tarde livre.", ["B3-1", "B3-2", "B4-1", "B4-2"]),
 (D(2027,1,1), "reta", "Folga (Ano-Novo).", []),
 (D(2027,1,2), "reta", "Blocos 5 e 6: refazer só os erros.", ["B5-1", "B5-2", "B6-1", "B6-2"]),
 (D(2027,1,3), "reta", "Modo prova 90 itens, cronometrado.", ["prova"]),
 (D(2027,1,4), "reta", "Análise dos erros do modo prova: para cada erro, qual dos dez padrões a banca usou?", ["erros", "banca"]),
 (D(2027,1,5), "reta", "Modo prova 90 itens.", ["prova"]),
 (D(2027,1,6), "reta", "Caderno de erros + tabela-relâmpago.", ["erros", "numeros"]),
 (D(2027,1,7), "reta", "Modo prova 90 itens.", ["prova"]),
 (D(2027,1,8), "reta", "Caderno de erros + 'Onde a banca inverte' de todos os tópicos.", ["erros"]),
 (D(2027,1,9), "reta", "Modo prova 90 itens (último completo).", ["prova"]),
 (D(2027,1,10), "reta", "Revisão leve dos materiais do repositório (Estruturas, SINAPI, NBR 5626).", []),
 (D(2027,1,11), "reta", "Modo prova 45 itens + caderno de erros.", ["prova", "erros"]),
 (D(2027,1,12), "reta", "Modo prova 45 itens + caderno de erros.", ["prova", "erros"]),
 (D(2027,1,13), "reta", "Modo prova 45 itens + caderno de erros.", ["prova", "erros"]),
 (D(2027,1,14), "reta", "Tabela-relâmpago + 'Como o examinador pensa'.", ["numeros", "banca"]),
 (D(2027,1,15), "reta", "Só caderno de erros e tabela-relâmpago. Nada novo.", ["erros", "numeros"]),
 (D(2027,1,16), "reta", "Descanso. Conferir local, documento e caneta preta transparente.", []),
 (D(2027,1,17), "prova", "PROVA. Manhã: objetivas (5 h). Tarde: discursiva (3 h).", []),
]

DIAS_SEMANA = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]

def plano_json():
    out = []
    for d, fase, txt, links in PLANO:
        out.append({"data": d.isoformat(), "dia": f"{d.day:02d}/{d.month:02d}", "sem": DIAS_SEMANA[d.weekday()],
                    "fase": fase, "txt": txt, "links": links})
    return out
