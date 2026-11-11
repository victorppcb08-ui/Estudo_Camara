# Licitações, Orçamento e Fiscalização de Obras

Estudo para a Câmara dos Deputados (Cebraspe, prova em 17/01/2027), cargo de Analista Legislativo – Engenharia Civil. Atende ao prompt [Prompt_Estudo_Fiscalização.docx](../Prompt_Estudo_Fiscaliza%C3%A7%C3%A3o.docx): os três blocos do edital estudados juntos.

| Arquivo | Para que serve |
|---|---|
| [Licitacoes_Orcamento_Fiscalizacao.pdf](Licitacoes_Orcamento_Fiscalizacao.pdf) | Abre direto no GitHub, com todos os gabaritos e comentários revelados (250 páginas). |
| [Licitacoes_Orcamento_Fiscalizacao.html](Licitacoes_Orcamento_Fiscalizacao.html) | Página interativa: responda Certo/Errado ou a–e, veja o comentário na hora, filtre as erradas e acompanhe o placar (com pontos líquidos, acertos − erros). |

## O que há no estudo

- **Bloco 1, Licitações e contratos** (Conhecimentos Básicos, itens 10.1 a 10.7): conceito, princípios e fases; modalidades, critérios e procedimentos auxiliares; dispensa × inexigibilidade; ETP, TR, anteprojeto, projeto básico e regimes de execução; contratos (características, formalização, garantias, duração, alterações, reajuste × repactuação × revisão, extinção, pagamento, sanções); gestão e fiscalização com o Decreto 11.246/2022.
- **Bloco 2, Orçamento de obras** (Específicos, itens 3.1 a 3.6): escada custo → preço, Decreto 7.983/2013 artigo por artigo, BDI (fórmula do TCU, faixas, o que não entra), encargos sociais, composições e SINAPI, levantamento de quantidades, cronograma, curva S, valor agregado e PERT-CPM (Limmer) com exemplo resolvido.
- **Bloco 3, Fiscalização** (Específicos, itens 6.1 a 6.4): medição, fatura, liquidação e pagamento; reajuste na prática; superfaturamento; controle de materiais (cimento, agregados, aditivos, concreto usinado, aço, madeira, cerâmicos, vidro) com as normas; documentação, recebimento, manutenção, garantias e normas legais.
- **Ponte com o Regimento Interno e a CF**: quem autoriza licitações e ordena despesas na Câmara (RICD, arts. 14, 15, 19 e 262 a 266), controle externo (CF, arts. 70 e 71), incompatibilidades dos deputados (arts. 54 e 55) e alertas para a P1.
- **580 questões**: as 511 questões únicas dos quatro cadernos (Licitação e Contratos, Dec. 7.983 e 11.246, Cadernos 03 e 04), todas comentadas com o dispositivo legal; os 3 itens de licitação da prova da Câmara de 2026; 25 itens do **Simulado P1** de Direito Administrativo; 41 itens inéditos "do examinador" por bloco.
- **Discursivas** (3 questões de 20 pontos): método, 8 temas prováveis, 3 respostas-modelo completas e espelhos dos outros 5.
- **As 25 pegadinhas**, técnica de leitura de itens, plano semanal até a prova e checklist da véspera.

## Como abrir

- **PDF:** clique no arquivo aqui no GitHub.
- **Página interativa:** o GitHub mostra o código, não a página. Baixe o `.html` e abra no navegador (funciona no celular). As respostas ficam salvas no próprio navegador.
- **Versão online** (abre só na sua conta do Claude): [Licitações, Orçamento e Fiscalização](https://claude.ai/artifact/GT1epHpkny7TwP6dAYRaFk)

## Fontes

- Cadernos do TEC Concursos nesta pasta: [Licitação e Contratos](../Dir.%20Administrativo%20-%20Licita%C3%A7%C3%A3o_Contratos.pdf) (191 questões), [Dec. 7.983 e 11.246](../Dir.%20Administrativo%20-%20Dec.%207983_e_11246.pdf) (41), [Caderno 03](../Caderno%2003_Engenharia_Civil_Planejam_Fiscaliza%C3%A7%C3%A3o.pdf) (200) e [Caderno 04](../Caderno%2004_Engenharia_Civil_Planejam_Fiscaliza%C3%A7%C3%A3o.pdf) (83). Quatro questões aparecem em dois cadernos e foram contadas uma vez. Os gabaritos são os dos cadernos.
- [Edital](../Edital.pdf) (Edital nº 1, de 2/10/2026) e as provas da Câmara guardadas em [Regimentos_CD_e_CN](../../Regimentos_CD_e_CN): Conhecimentos Gerais do Policial Legislativo de 2026 (itens 77, 79 e 80) e a P2 de 2025/2026, usadas para calibrar o estilo do examinador.
- Lei 14.133/2021, Decretos 7.983/2013 e 11.246/2022, RICD (até a RCD 16/2025) e CF/1988. Os artigos do Regimento e da Constituição foram conferidos nos arquivos da pasta Regimentos_CD_e_CN. Os valores em reais da Lei 14.133 aparecem como valores originais (são atualizados todo ano por decreto).

A pasta `fontes/` tem o que gera a página: `parse.py` extrai as questões do texto dos cadernos (`pdftotext -layout`), `comentarios.py` guarda os comentários, `extras.py` os itens da Câmara e os inéditos, e `build.py` monta o HTML com `corpo*.html`, `estilo.css.html` e `script.js`. Para regenerar:

```
python3 fontes/build.py pagina.html
python3 fontes/embrulha.py pagina.html Licitacoes_Orcamento_Fiscalizacao.html
node fontes/pdf.js Licitacoes_Orcamento_Fiscalizacao.html Licitacoes_Orcamento_Fiscalizacao.pdf
```
