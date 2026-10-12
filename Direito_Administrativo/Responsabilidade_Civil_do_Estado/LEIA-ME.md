# Responsabilidade Civil do Estado

Estudo estratégico para o item 6 do edital da Câmara dos Deputados (Cebraspe, prova em 17/01/2027).

| Arquivo | Para que serve |
|---|---|
| [Responsabilidade_Civil_do_Estado.pdf](Responsabilidade_Civil_do_Estado.pdf) | Abre direto no GitHub, com todos os gabaritos e comentários revelados (88 páginas). |
| [Responsabilidade_Civil_do_Estado.html](Responsabilidade_Civil_do_Estado.html) | Página interativa: responda Certo/Errado ou a–e, veja o comentário na hora e acompanhe o placar por item do edital. |

## O que há no estudo

- **Mapa do edital:** como os subitens 6.1 a 6.5 se encadeiam num roteiro de análise de caso, e onde cada um está no Cap. 15 de Maria Sylvia Zanella Di Pietro (*Responsabilidade Extracontratual do Estado*).
- **Perfil da banca:** o que o Cebraspe repete, por que as 7 questões anuladas estão todas em pontos de divergência, e uma tabela de onde a autora e o STF divergem (omissão, caso fortuito, ação contra o agente, denunciação da lide, danos nucleares, atos jurisdicionais).
- **Módulos 6.1 a 6.5:** teoria do Cap. 15, jurisprudência do STF que a banca cobra (Temas 130, 362, 365, 366, 512, 592, 666, 777, 897, 940, 1055 e 1237) e um quadro de pegadinhas em cada módulo.
- **185 questões comentadas:** as 158 questões únicas dos Cadernos 06 e 07 (146 + 12 exclusivas do Caderno 07), os 3 itens da prova da Câmara de 2012 e 24 itens inéditos do "simulado do examinador".
- **As 20 pegadinhas**, técnica de leitura de itens do Cebraspe, plano de revisões até a prova e checklist da véspera.

## Como abrir

- **PDF:** clique no arquivo aqui no GitHub.
- **Página interativa:** o GitHub mostra o código, não a página. Baixe o `.html` e abra no navegador. As respostas ficam salvas no próprio navegador.
- **Versão original** (abre só na sua conta do Claude): [Responsabilidade Civil do Estado](https://claude.ai/artifact/H9th35dFvw3zwuoDTe8qtz)

## Fontes

- Maria Sylvia Zanella Di Pietro, [*Direito Administrativo*](../../Direito_Administrativo_Maria_Sylvia_Zane.pdf), Cap. 15.
- [Caderno 06](../../06_Caderno%2006_Dir_Adm_Resp_Civil_Estado.pdf) (146 questões) e [Caderno 07](../../07_Caderno%20Dir.%20Administrativo%20-%20RESPONSABILIDADE%20CIVIL.pdf) (71 questões) do TEC Concursos, Cebraspe, 2020 a 2026. As questões foram extraídas automaticamente dos PDFs e os gabaritos são os dos cadernos.
- Prova de Conhecimentos Básicos e gabarito definitivo da Câmara dos Deputados de 2012 (guardados no repositório Jos-).

A pasta `fontes/` tem o que gera a página: `parse.py` extrai as questões do texto dos cadernos, `comentarios.py` e `extras.py` guardam os comentários e o simulado, e `build.py` monta o HTML a partir de `template.html`. Para regenerar:

```
python3 fontes/build.py pagina.html
python3 fontes/embrulha.py pagina.html Responsabilidade_Civil_do_Estado.html
node fontes/pdf.js Responsabilidade_Civil_do_Estado.html Responsabilidade_Civil_do_Estado.pdf
```
