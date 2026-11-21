# Câmara 2027 · Engenharia Civil: projetos complementares e simulados

Material de estudo para a P2 do concurso de Analista Legislativo, Engenheiro (Engenharia Civil), da Câmara dos Deputados (Cebraspe, prova em 17/01/2027). Feito em 21/11/2026.

| Arquivo | Para que serve |
|---|---|
| [Camara_2027_Engenharia.pdf](Camara_2027_Engenharia.pdf) | Tudo em um PDF de 112 páginas, para ler offline (celular, viagem). Cada simulado traz o gabarito comentado logo depois. |
| [Camara_2027_Engenharia.html](Camara_2027_Engenharia.html) | Página interativa. Baixe e abra no navegador: responde C, E ou em branco, corrige com +1/−1/0, guarda o caderno de erros e sorteia o modo prova. |

## O que há no material

1. **Como o examinador pensa:** os dez padrões de alteração que o Cebraspe usa nos itens (troca de número, inversão, troca de nome técnico, condição inventada, justificativa falsa etc.), cada um com exemplos reais, e a regra para decidir entre marcar e deixar em branco.
2. **Bloco 2 do edital, os 7 tópicos:** instalações elétricas (com SPDA), incêndio, arquitetônicos (com NBR 9050 e NBR 15575), ar-condicionado, ventilação e exaustão (com gás), elevadores e telefonia. Cada tópico traz normas com a situação atual, conceitos, números que caem, "onde a banca inverte" e itens reais comentados (42 no total).
3. **Tabela-relâmpago:** os números do Bloco 2 numa página.
4. **16 simulados de 20 itens (320 itens):**
   - Bloco 2: 5 simulados com 55 itens reais (Caderno 07 e provas do banco) e 45 inéditos, todos comentados.
   - Blocos 1, 3, 4, 5 e 6: 11 simulados só com itens reais e gabarito oficial definitivo das provas da pasta [Provas_Engenharia](../../Provas_Engenharia) e da raiz do repositório, com comentário curto.
5. **Modo prova:** sorteia 20, 45 ou 90 itens dos blocos escolhidos, com cronômetro.
6. **Cronograma:** dia a dia de 21/11/2026 a 17/01/2027, com as férias de 09/12 a 27/12 em modo manutenção.

## Atenção às normas que mudaram

Várias normas do Bloco 2 têm edição nova ou estão em revisão. O material marca cada caso:

- **NBR 5419:2026** (SPDA): publicada em março de 2026, substitui a de 2015. Os valores de esfera rolante, malha e descidas citados são os da edição de 2015; confira na nova.
- **NBR 9077:2025** (saídas de emergência): substitui a de 2001 e reorganizou o cálculo de largura.
- **NBR 16858-1** (elevadores): substituiu a NBR NM 207, citada em muitos itens antigos.
- **NBR 16401-1:2024** (ar-condicionado): nova edição; a parte 3 tem situação confusa no catálogo.
- **NBR 10898:2023** (iluminação de emergência): nova edição.
- **NBR 5410:2004**: segue vigente; a revisão ainda está em consulta pública.

Os itens reais de 2007 a 2011 se apoiam às vezes em normas canceladas (NBR 6401, NBR NM 207, NBR 5413). Os comentários avisam quando isso acontece.

## Correção encontrada no material antigo

No [Guia de estudo por provas](../Guia_Geral_por_Provas_Cebraspe), o item 51 do STJ 2024 (sprinklers alimentados por reservatório elevado "desde que de uso exclusivo") aparece como **C**. O gabarito oficial definitivo é **E**.

## Limites

- O texto de cada norma foi resumido em linguagem própria; não substitui a norma.
- Os itens inéditos foram escritos no estilo da banca a partir das normas e da doutrina; não são questões oficiais.
- Nos itens reais, o comentário explica o gabarito oficial. Em poucos casos a justificativa da banca é inferência, e o comentário diz isso.
- O livro do Yazigi não estava entre os arquivos; as referências a ele vêm do uso que a própria banca faz do texto (ver o material de estruturas metálicas).

## Para alterar ou ampliar

A pasta [fontes/](fontes) guarda o conteúdo e o gerador.

| Arquivo | Conteúdo |
|---|---|
| `teoria.html` | Texto dos 7 tópicos, "Como o examinador pensa" e tabela-relâmpago |
| `simulados_bloco2.py` | Os 100 itens dos simulados do Bloco 2 e os 42 itens extras |
| `simulados_blocos.py` | Seleção e comentários dos itens reais dos Blocos 1, 3, 4, 5 e 6 |
| `banco_itens.json` | 1.117 itens extraídos de 16 provas do Cebraspe, com gabarito oficial |
| `plano.py` | Cronograma |
| `template.html` · `build.py` | Modelo da página e montagem |

Para gerar de novo, dentro de `fontes/`: `python3 build.py`. O PDF sai do arquivo `_impressao.html` impresso pelo navegador (Chromium/Playwright).

## Versão original

Página interativa no claude.ai (abre só na sua conta): [Câmara 2027 · Engenharia Civil](https://claude.ai/artifact/5Nxgiq4CkLFDRgasgrap8K)
