# Instalações prediais de água fria e água quente (NBR 5626:2020)

Material de estudo para a prova da Câmara dos Deputados (Cebraspe), feito em 07/10/2026.

## Por onde começar

| Arquivo | Para que serve |
|---|---|
| [NBR_5626-2020_Resumo_de_estudo.pdf](NBR_5626-2020_Resumo_de_estudo.pdf) | Abre direto no navegador ou no celular. É o mesmo conteúdo do Word. |
| [NBR_5626-2020_Resumo_de_estudo.docx](NBR_5626-2020_Resumo_de_estudo.docx) | Versão editável, para anotar e grifar. |
| [esquemas/](esquemas) | Os sete esquemas do resumo, em imagem, para revisão rápida. |

## O que há no resumo (26 páginas)

1. **Ficha rápida** com os números da norma: pressões, temperaturas, reservação, ensaios.
2. **Resumo por tema**, com o item da norma entre parênteses para conferência (seções 2 a 16).
3. **Onde a banca costuma inverter** (seção 17).
4. **Questões 117 a 163 do caderno comentadas** (seção 18): 117 a 158 de água fria e 159 a 163 de água quente. O enunciado está resumido; o texto integral fica no caderno, na questão de mesmo número.
5. **Treino extra** com 40 itens certo/errado inéditos sobre a edição de 2020 e gabarito comentado (seções 19 e 20).

## Como usar com o caderno

Resolva as questões no caderno e confira na seção 18 do resumo. Cada questão tem uma classificação:

- **Norma de 2020 confirma**: 118, 119, 120, 123, 127, 131, 139, 146, 147, 149 e 162.
- **Edição anterior: atenção**: 117, 125, 132, 136, 137, 150 e 154. O gabarito se apoia em critério anterior a 2020 (pesos, limite de velocidade, chumbo, 40 cm da retrossifonagem).
- **Doutrina e prática**: as demais, sobre hidráulica, materiais ou prática de projeto.

## Limites deste material

- É um resumo em linguagem própria. Não reproduz nem substitui a norma.
- A cópia da norma usada como base não tem as páginas 4, 5 e 31. Ficaram de fora as definições 3.21 a 3.42, os itens 6.15.2.5 a 6.15.2.9 e a figura de ventilação de coluna.
- O que se diz sobre a edição de 1998 e sobre a literatura não veio dos dois PDFs do repositório. Confira antes de levar para a prova.
- Nas questões 126 e 159, a justificativa da banca é inferência. As questões 143 a 145 dependem da figura do caderno.

## Arquivos de origem

- Norma: [nbr-5626-2020-emenda-sistemas-prediais-de-agua-fria-e-quente_compress.pdf](../../nbr-5626-2020-emenda-sistemas-prediais-de-agua-fria-e-quente_compress.pdf)
- Caderno de questões: [Caderno_07_Engª_Civil_Edificações_Instalações.pdf](../../Caderno_07_Eng%C2%AA_Civil_Edifica%C3%A7%C3%B5es_Instala%C3%A7%C3%B5es.pdf)

## Para alterar o resumo no futuro

A pasta [fontes/](fontes) guarda o texto e os programas que geram o Word. Assim o resumo pode ser corrigido ou ampliado sem refazer tudo.

| Arquivo | Conteúdo |
|---|---|
| `conteudo.js` | Texto das seções 1 a 17 |
| `caderno.js` | Comentários das questões 117 a 163 |
| `questoes.js` | Os 40 itens do treino extra e o gabarito |
| `esquemas.py` | Desenho dos sete esquemas |
| `build.js` | Montagem do Word |

Para gerar de novo, dentro de `fontes/`:

```
python3 esquemas.py ../esquemas
node build.js ../NBR_5626-2020_Resumo_de_estudo.docx
```

Requer Python com matplotlib e Pillow, e Node com o pacote `docx`.
