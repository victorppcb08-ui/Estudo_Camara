const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, Footer,
  AlignmentType, HeadingLevel, WidthType, ShadingType, BorderStyle, LevelFormat,
  PageNumber, TabStopType, VerticalAlign, LineRuleType,
} = require("docx");
const { blocos } = require("./conteudo.js");
const { questoes } = require("./questoes.js");
const { aguaFria, aguaQuente } = require("./caderno.js");

const IMG = path.join(__dirname, "..", "esquemas");
const SAIDA = process.argv[2];
const FONTE = "Calibri";
const AZUL = "1F4E79";
const CINZA = "5B6570";
const LARGURA = 9638; // A4 com margens de 2 cm

// ---- texto com **negrito**
function runs(texto, base = {}) {
  return texto.split("**")
    .map((parte, i) => (parte === "" ? null : new TextRun({ text: parte, ...base, bold: Boolean(base.bold) || i % 2 === 1 })))
    .filter(Boolean);
}

function dimensoesPng(arq) {
  const b = fs.readFileSync(arq);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}

const bordaFina = { style: BorderStyle.SINGLE, size: 4, color: "BFC5CC" };
const bordas = { top: bordaFina, bottom: bordaFina, left: bordaFina, right: bordaFina };

function celula(texto, largura, { cab = false, centro = false, negrito = false, junto = false } = {}) {
  return new TableCell({
    width: { size: largura, type: WidthType.DXA },
    borders: bordas,
    verticalAlign: VerticalAlign.CENTER,
    shading: cab ? { type: ShadingType.CLEAR, fill: "DCE6F1", color: "auto" } : undefined,
    margins: { top: 70, bottom: 70, left: 110, right: 110 },
    children: [new Paragraph({
      alignment: centro ? AlignmentType.CENTER : AlignmentType.LEFT,
      keepNext: junto,
      spacing: { before: 0, after: 0, line: 252, lineRule: LineRuleType.AUTO },
      children: runs(texto, { size: 19, bold: cab || negrito, color: cab ? AZUL : undefined }),
    })],
  });
}

function tabela(cab, linhas, larg, opts = {}) {
  const centroCols = opts.centroCols || [];
  return new Table({
    width: { size: LARGURA, type: WidthType.DXA },
    columnWidths: larg,
    rows: [
      new TableRow({ tableHeader: true, cantSplit: true, children: cab.map((c, i) => celula(c, larg[i], { cab: true, junto: true, centro: opts.centro || centroCols.includes(i) })) }),
      ...linhas.map((l, n) => new TableRow({
        cantSplit: true,
        children: l.map((c, i) => celula(c, larg[i], { junto: Boolean(opts.junto) && n < linhas.length - 1, centro: opts.centro || centroCols.includes(i), negrito: opts.negritoCol === i })),
      })),
    ],
  });
}

const espaco = (after = 120) => new Paragraph({ spacing: { before: 0, after }, children: [] });

function converter(b) {
  switch (b.tipo) {
    case "h1":
      return [new Paragraph({ heading: HeadingLevel.HEADING_1, keepNext: true, children: [new TextRun(b.t)] })];
    case "h2":
      return [new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true, children: [new TextRun(b.t)] })];
    case "p":
      return [new Paragraph({ spacing: { before: 0, after: 120, line: 276, lineRule: LineRuleType.AUTO }, children: runs(b.t) })];
    case "ul":
      return b.itens.map((t, i) => new Paragraph({
        numbering: { reference: "marcadores", level: 0 },
        spacing: { before: 0, after: i === b.itens.length - 1 ? 140 : 60, line: 270, lineRule: LineRuleType.AUTO },
        children: runs(t),
      }));
    case "nota":
      return [
        new Paragraph({
          keepNext: true,
          spacing: { before: 120, after: 0, line: 270, lineRule: LineRuleType.AUTO },
          indent: { left: 170, right: 170 },
          shading: { type: ShadingType.CLEAR, fill: "F3F6FA", color: "auto" },
          border: { left: { style: BorderStyle.SINGLE, size: 24, color: AZUL, space: 8 } },
          children: [new TextRun({ text: b.titulo, bold: true, color: AZUL })],
        }),
        new Paragraph({
          spacing: { before: 0, after: 200, line: 270, lineRule: LineRuleType.AUTO },
          indent: { left: 170, right: 170 },
          shading: { type: ShadingType.CLEAR, fill: "F3F6FA", color: "auto" },
          border: { left: { style: BorderStyle.SINGLE, size: 24, color: AZUL, space: 8 } },
          children: runs(b.t),
        }),
      ];
    case "tabela":
      return [tabela(b.cab, b.linhas, b.larg, b.opts), espaco(160)];
    case "fig": {
      const arq = path.join(IMG, b.arq);
      const { w, h } = dimensoesPng(arq);
      const larg = b.larguraPx;
      return [
        new Paragraph({
          alignment: AlignmentType.CENTER, keepNext: true, spacing: { before: 120, after: 60, line: 240, lineRule: LineRuleType.AUTO },
          children: [new ImageRun({
            type: "png", data: fs.readFileSync(arq),
            transformation: { width: larg, height: Math.round(larg * h / w) },
            altText: { title: b.legenda, description: b.legenda, name: b.arq },
          })],
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER, spacing: { before: 0, after: 200 },
          children: [new TextRun({ text: b.legenda, italics: true, size: 18, color: CINZA })],
        }),
      ];
    }
  }
  throw new Error("tipo desconhecido: " + b.tipo);
}

// ---- cabeçalho do documento
const abertura = [
  new Paragraph({
    spacing: { before: 0, after: 60 },
    children: [new TextRun({ text: "NBR 5626:2020", bold: true, size: 44, color: AZUL })],
  }),
  new Paragraph({
    spacing: { before: 0, after: 60 },
    children: [new TextRun({ text: "Sistemas prediais de água fria e água quente", bold: true, size: 30, color: "1F2933" })],
  }),
  new Paragraph({
    spacing: { before: 0, after: 80 },
    children: [new TextRun({ text: "Resumo de estudo com esquemas e questões comentadas", size: 24, color: CINZA })],
  }),
  new Paragraph({
    spacing: { before: 0, after: 240 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: AZUL, space: 6 } },
    children: [new TextRun({ text: "Base: ABNT NBR 5626:2020, segunda edição (29.06.2020), versão corrigida de 30.09.2020", size: 18, color: CINZA })],
  }),
];

// ---- questões do caderno (comentadas)
const REL = {
  N: { rotulo: "Norma de 2020 confirma", cor: "2E7D5B" },
  A: { rotulo: "Edição anterior: atenção", cor: "B45309" },
  D: { rotulo: "Doutrina e prática", cor: CINZA },
};
const nums = (lista, rel) => lista.filter((q) => q[3] === rel).map((q) => q[0]).join(", ");
const todas = [...aguaFria, ...aguaQuente];

function blocoCaderno([num, origem, gab, rel, resumo, comentario]) {
  const r = REL[rel];
  return [
    new Paragraph({
      keepNext: true,
      spacing: { before: 140, after: 50, line: 270, lineRule: LineRuleType.AUTO },
      border: { top: { style: BorderStyle.SINGLE, size: 4, color: "BFC5CC", space: 6 } },
      tabStops: [{ type: TabStopType.RIGHT, position: LARGURA }],
      children: [
        new TextRun({ text: (num.includes(" a ") ? "Questões " : "Questão ") + num, bold: true, color: AZUL, size: 23 }),
        new TextRun({ text: "   " + origem + "   ", color: CINZA }),
        new TextRun({ text: "Gabarito oficial: " }),
        new TextRun({ text: gab, bold: true }),
        new TextRun({ text: "\t" + r.rotulo, bold: true, color: r.cor, size: 18 }),
      ],
    }),
    new Paragraph({
      keepNext: true,
      spacing: { before: 0, after: 50, line: 270, lineRule: LineRuleType.AUTO },
      children: [new TextRun({ text: "Item (resumo): ", bold: true }), new TextRun({ text: resumo, italics: true })],
    }),
    new Paragraph({
      spacing: { before: 0, after: 120, line: 270, lineRule: LineRuleType.AUTO },
      children: [new TextRun({ text: "Comentário: ", bold: true }), new TextRun(comentario)],
    }),
  ];
}

const blocoCaderno18 = [
  new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun("18. Questões do caderno comentadas (117 a 163)")] }),
  new Paragraph({
    spacing: { before: 0, after: 120, line: 276, lineRule: LineRuleType.AUTO },
    children: runs("Comentários às questões **117 a 158 (água fria)** e **159 a 163 (água quente)** do caderno “Engª Civil, Edificações, Instalações”, todas do Cebraspe. O enunciado aparece aqui **resumido**; o texto integral está no caderno, na questão de mesmo número. O melhor uso é resolver no caderno e vir aqui conferir. Os gabaritos são os oficiais indicados no caderno."),
  }),
  new Paragraph({
    spacing: { before: 0, after: 120, line: 276, lineRule: LineRuleType.AUTO },
    children: runs("Cada questão recebe uma classificação, que mostra quanto do gabarito se sustenta no texto atual da norma:"),
  }),
  tabela(["Classificação", "O que significa", "Questões"], [
    [REL.N.rotulo, "O texto da NBR 5626:2020 sustenta o gabarito.", nums(todas, "N")],
    [REL.A.rotulo, "O gabarito se apoia em critério de edição anterior (pesos, limites numéricos, materiais). Leia o comentário antes de levar a regra para a prova.", nums(todas, "A")],
    [REL.D.rotulo, "Assunto de hidráulica, materiais ou prática de projeto que não está no texto da norma.", "As demais"],
  ], [2400, 4438, 2800], { negritoCol: 0 }),
  espaco(120),
  new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true, children: [new TextRun("Água fria (117 a 158)")] }),
  ...aguaFria.flatMap(blocoCaderno),
  new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true, children: [new TextRun("Água quente (159 a 163)")] }),
  ...aguaQuente.flatMap(blocoCaderno),
];

// ---- treino extra (itens inéditos)
const blocoQuestoes = [
  new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun("19. Treino extra: itens inéditos sobre a edição de 2020")] }),
  new Paragraph({
    spacing: { before: 0, after: 160, line: 276, lineRule: LineRuleType.AUTO },
    children: runs("Itens escritos para este resumo, no formato **certo (C)** ou **errado (E)**. Servem para fixar os números e as regras da edição de 2020 que as questões antigas ainda não cobrem. Não são questões de prova."),
  }),
  ...questoes.map(([enun]) => new Paragraph({
    numbering: { reference: "questoes", level: 0 },
    spacing: { before: 0, after: 110, line: 270, lineRule: LineRuleType.AUTO },
    children: [new TextRun(enun)],
  })),
  new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun("20. Gabarito comentado do treino extra")] }),
  tabela(["Item", "Gabarito", "Comentário"],
    questoes.map(([, g, c], i) => [String(i + 1), g, c]),
    [800, 1100, 7738], { centroCols: [0, 1], negritoCol: 1 }),
];

const doc = new Document({
  creator: "Resumo de estudo",
  title: "NBR 5626:2020 - Resumo de estudo",
  description: "Resumo de estudo da NBR 5626:2020 com esquemas e questões comentadas",
  styles: {
    default: { document: { run: { font: FONTE, size: 21 }, paragraph: { spacing: { line: 276, lineRule: LineRuleType.AUTO } } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: FONTE, size: 30, bold: true, color: AZUL },
        paragraph: { spacing: { before: 360, after: 140 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: FONTE, size: 24, bold: true, color: "1F2933" },
        paragraph: { spacing: { before: 220, after: 100 }, outlineLevel: 1 } },
    ],
  },
  numbering: {
    config: [
      { reference: "marcadores", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 400, hanging: 240 } } } }] },
      { reference: "questoes", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { run: { bold: true, color: AZUL }, paragraph: { indent: { left: 520, hanging: 520 } } } }] },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    footers: {
      default: new Footer({ children: [new Paragraph({
        tabStops: [{ type: TabStopType.RIGHT, position: LARGURA }],
        children: [
          new TextRun({ text: "NBR 5626:2020 · resumo de estudo (não substitui a norma)", size: 16, color: CINZA }),
          new TextRun({ children: ["\t", PageNumber.CURRENT], size: 16, color: CINZA }),
        ],
      })] }),
    },
    children: [...abertura, ...blocos.flatMap(converter), ...blocoCaderno18, ...blocoQuestoes],
  }],
});

Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(SAIDA, buf); console.log("gravado", SAIDA, buf.length); });
