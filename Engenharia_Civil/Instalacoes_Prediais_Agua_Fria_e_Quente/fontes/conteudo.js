// Conteúdo do resumo de estudo da NBR 5626:2020 (texto próprio).
// Marcação: **negrito**. Tipos de bloco: h1, h2, p, ul, nota, tabela, fig, questoes, gabarito.

const blocos = [];
const h1 = (t) => blocos.push({ tipo: "h1", t });
const h2 = (t) => blocos.push({ tipo: "h2", t });
const p = (t) => blocos.push({ tipo: "p", t });
const ul = (...itens) => blocos.push({ tipo: "ul", itens });
const nota = (titulo, t) => blocos.push({ tipo: "nota", titulo, t });
const tabela = (cab, linhas, larg, opts = {}) => blocos.push({ tipo: "tabela", cab, linhas, larg, opts });
const fig = (arq, legenda, larguraPx) => blocos.push({ tipo: "fig", arq, legenda, larguraPx });

// ------------------------------------------------------------------ abertura
nota("Sobre este material",
  "Resumo escrito em linguagem própria e organizado por tema. Não reproduz nem substitui o texto da norma: os números entre parênteses indicam o item da NBR 5626:2020 para você conferir na fonte. " +
  "Os esquemas são desenhos didáticos simplificados, feitos para este resumo, e não as figuras originais. " +
  "As seções 18 a 20 trazem as questões do seu caderno comentadas e um treino extra. " +
  "**Lacuna da cópia usada como base:** faltam as páginas 4, 5 e 31 da norma. Por isso ficaram de fora as definições 3.21 a 3.42, os itens 6.15.2.5 a 6.15.2.9 (parte da proteção contra refluxo) e a figura sobre ventilação de coluna de distribuição.");

// ------------------------------------------------------------------ 1
h1("1. Ficha rápida: os números da norma");
p("Os valores abaixo concentram a maior parte das cobranças numéricas. As seções seguintes explicam o contexto de cada um.");
tabela(["Assunto", "Valor", "Item"], [
  ["Reserva mínima de água potável", "Pelo menos 24 h de consumo normal do edifício, somando o volume de incêndio quando armazenado junto", "6.5.6.2"],
  ["Reserva máxima (recomendação, em nota)", "3 dias de consumo diário, quando não for possível determinar o volume máximo, ou meios que preservem a água", "6.5.6.3"],
  ["Reposição do reservatório", "Volume de consumo diário reposto em até 6 h; em residência unifamiliar, até 3 h", "6.7.2"],
  ["Bombas de recalque ou pressurização", "No mínimo 2, com funcionamento independente", "6.5.11.2"],
  ["Pressão dinâmica mínima no ponto de utilização", "10 kPa (1 mca), em qualquer caso", "6.9.2"],
  ["Pressão dinâmica mínima em qualquer ponto da rede", "5 kPa (0,5 mca), exceto trechos verticais de saída de reservatório elevado para o barrilete", "6.9.3"],
  ["Pressão estática máxima no ponto de utilização", "400 kPa (40 mca)", "6.9.4"],
  ["Sobrepressão por transientes", "Até 200 kPa (20 mca) acima da pressão dinâmica de projeto", "6.9.6"],
  ["Velocidade da água", "Sem limite numérico obrigatório; 3 m/s aparece só em nota", "6.8.3"],
  ["Estação redutora de pressão", "Pelo menos 2 válvulas em paralelo (uma sobressalente); uma estação por zona de pressão", "6.9.7 e 6.9.11"],
  ["Água quente para uso corporal", "Acima de 45 °C, limitador automático obrigatório", "6.10.4.3"],
  ["Água quente em ambiente sanitário com misturador convencional", "Limite de 70 °C na tubulação", "6.10.3"],
  ["Temperatura máxima recomendada (nota)", "38 °C para duchas higiênicas, jardins de infância e certas clínicas e hospitais", "6.10.4.4"],
  ["Medidas extras de segurança", "Precauções acima de 90 °C no sistema; controles na geração acima de 95 °C", "6.10.7.1 e 6.13.2.1"],
  ["Separação atmosférica", "Afastamento lateral L ≥ 3d; altura S conforme o diâmetro (ver seção 12)", "6.15.2.3"],
  ["Ensaio de estanqueidade das tubulações", "600 kPa ou 1,5 vez a máxima pressão de trabalho, o que for menor; sem queda de pressão por 1 h", "7.3.1"],
  ["Ensaio em tubulação de água quente", "Água a no mínimo 80 °C, antes do isolamento ou do recobrimento", "7.3.1.3"],
  ["Ensaio de estanqueidade de reservatório", "72 h sem vazamento nem extravasamento", "7.3.3.3"],
  ["Desinfecção química (Anexo F)", "Cloro livre de no mínimo 20 mg/L, com repouso mínimo de 2 h", "F.3.3"],
  ["Desinfecção térmica (Anexo F)", "No mínimo 70 °C, com fluxo de pelo menos 30 min em cada peça", "F.3.4"],
], [3300, 5138, 1200]);
fig("e4_pressoes.png", "Esquema 1. Limites de pressão da norma (elaboração própria).", 600);

// ------------------------------------------------------------------ 2
h1("2. O que é a norma e onde se aplica");
ul(
  "**Objeto:** requisitos de projeto, execução, operação e manutenção dos sistemas prediais de água fria e água quente, abreviados na norma como **SPAFAQ** (seção 1).",
  "**Só água potável.** Vale para qualquer tipo de edifício, residencial ou não. Não se aplica a água não potável, a água de processos industriais nem a processos internos de equipamentos específicos.",
  "**Preocupações centrais:** bom desempenho do sistema, uso racional de água e energia, preservação da potabilidade e segurança sanitária.",
  "**Histórico:** é a segunda edição, de 29.06.2020, com versão corrigida em 30.09.2020 (Errata 1). Cancela e substitui a NBR 5626:1998 e também a NBR 7198:1993, de água quente. A partir de 2020, água fria e água quente estão na mesma norma.",
  "**Transição:** a edição de 2020 não se aplica a projetos protocolados para aprovação antes da publicação, nem aos protocolados até 180 dias depois dela. Nesses casos vale a edição de 1998.",
  "**Normas citadas que costumam aparecer junto:** NBR 5674 (gestão da manutenção), NBR 14037 (manual de uso, operação e manutenção), NBR 6493 (cores de tubulações), NBR 10152 (níveis de ruído), NBR 15575-6 (desempenho, sistemas hidrossanitários), NBR 15932 (instalador hidráulico), NBR 16280 (reformas), NBR 16792 (conservação de água) e NBR 16824 (prevenção de legionelose)."
);

// ------------------------------------------------------------------ 3
h1("3. Vocabulário essencial");
p("Definições reescritas de forma resumida, a partir da seção 3. A ordem segue o caminho da água, da rua até o ponto de uso.");
fig("e1_sistema.png", "Esquema 2. Partes de um sistema com abastecimento indireto (elaboração própria).", 560);
tabela(["Termo", "Ideia central"], [
  ["Água fria / água quente", "Água potável à temperatura ambiente / água potável acima da temperatura ambiente por aquecimento artificial."],
  ["Ramal predial", "Trecho entre a rede pública e o início do alimentador predial (ou da rede predial de distribuição). O ponto onde termina é convencionado pela concessionária."],
  ["Alimentador predial", "Liga a fonte de abastecimento a um reservatório ou à rede predial de distribuição."],
  ["Sistema direto / indireto", "Direto: a água vem diretamente da fonte de abastecimento. Indireto: a água vem de um reservatório do edifício."],
  ["Barrilete", "Tubulação da qual saem as colunas de distribuição."],
  ["Coluna de distribuição", "Sai do barrilete e alimenta os ramais."],
  ["Ramal", "Sai da coluna (ou direto do barrilete) e alimenta os sub-ramais."],
  ["Sub-ramal", "Liga o ramal ao ponto de utilização."],
  ["Aquecimento individual", "Aquecedor a jusante do ponto de água fria; dispensa rede de distribuição de água quente."],
  ["Aquecimento central privado", "Aquecedor remoto que atende pontos de uma mesma unidade."],
  ["Aquecimento central coletivo", "Aquecedor remoto que atende pontos de mais de uma unidade."],
  ["Conexão cruzada", "Qualquer contato entre a água potável do sistema e água não potável ou de qualidade desconhecida."],
  ["Refluxo", "Entrada, na tubulação, de água vinda de outra origem que não a fonte prevista. Inclui a retrossifonagem e o refluxo por vasos comunicantes."],
  ["Retrossifonagem", "Refluxo de água usada para dentro da tubulação porque a pressão nela ficou abaixo da atmosférica."],
  ["Separação atmosférica", "Espaço preenchido por ar entre a saída do ponto de suprimento (ou da peça de utilização) e o nível de transbordamento do reservatório ou aparelho."],
  ["Quebrador de vácuo", "Componente que impede o refluxo causado por queda transitória da pressão a montante."],
  ["Pressão estática", "Carga de pressão em uma seção da tubulação cheia, mas sem escoamento."],
  ["Válvula redutora de pressão", "Reduz a pressão dinâmica a jusante e impede a transmissão da pressão estática de montante quando não há escoamento."],
  ["Relação de redução de pressões", "Quanto a pressão de entrada pode superar a de saída sem cavitação, ruído e desgaste. Em uma relação 4:1, a de montante pode ser até quatro vezes a de jusante."],
  ["Zona de pressão", "Pavimentos ou setores atendidos diretamente por uma mesma estação redutora de pressão."],
  ["Tubo respiro / tubo ventilador", "Respiro: deixa sair ar ou vapor. Ventilador: deixa entrar ar na tubulação no esvaziamento ou em pressão negativa, servindo de proteção não localizada contra refluxo."],
  ["Extravasão, aviso e limpeza", "Extravasão: escoa o excesso acima do nível de transbordamento. Aviso: leva parte do excesso a local visível, como alerta de falha. Limpeza: esvazia o reservatório."],
  ["Sifão térmico", "Trecho vertical em U (invertido ou não) que dificulta a passagem de calor por convecção natural."],
  ["Tubulação de retorno / recirculação", "O retorno leva a água quente de volta ao reservatório ou aquecedor; a recirculação mantém a água quente em movimento para que chegue mais rápido ao ponto."],
  ["Tubulação aparente / recoberta", "Aparente: externa ao elemento construtivo, sem cobertura. Recoberta: em espaço projetado para isso, com acesso pela remoção do cobrimento."],
  ["Diâmetro nominal (DN)", "Número que classifica os componentes. Não é medido nem usado em cálculo."],
  ["Vida útil de projeto (VUP)", "Período para o qual o sistema é projetado, supondo manutenção correta. Não se confunde com vida útil, durabilidade ou prazo de garantia."],
], [2700, 6938]);
nota("Três tipos de profissional",
  "**Habilitado:** graduado e registrado no órgão de classe; elabora projetos e assume responsabilidade técnica (3.46). " +
  "**Qualificado:** tem treinamento comprovado por entidade reconhecida para montagens, manutenções e ensaios (3.47). " +
  "**Capacitado:** trabalha sob orientação e responsabilidade de um profissional habilitado (3.45).");

// ------------------------------------------------------------------ 4
h1("4. Documentação e materiais");
h2("Documentação (seção 4)");
ul(
  "O projeto deve trazer, entre outros elementos: premissas e método de dimensionamento, memorial descritivo, volumes de armazenamento, pressões de trabalho, simultaneidade de uso e vazões de projeto, fontes de abastecimento, dispositivos de segurança, desenhos e diagrama vertical, especificações de componentes e a vida útil de projeto com as manutenções necessárias para atingi-la (4.1).",
  "O projeto fornece subsídios para o manual de operação, uso e manutenção (NBR 14037) e para o programa de manutenção preventiva (NBR 5674) (4.2).",
  "Os documentos do sistema ficam em posse do **responsável legal pela edificação** (4.3)."
);
h2("Materiais e componentes (seção 5)");
ul(
  "Não podem afetar a potabilidade, não podem ter o desempenho comprometido pela água ou pelo meio e devem resistir às solicitações de uso (5.1).",
  "O que fica em contato permanente com a água não pode transmitir gosto, cor, odor ou toxicidade, nem favorecer micro-organismos (5.2).",
  "Superfícies em contato com a água potável devem resistir à corrosão (5.4).",
  "Se for inevitável usar material que favoreça biofilme (poroso, rugoso, com microfissuras), a manutenção deve ser avisada da necessidade de limpezas programadas (5.3).",
  "A norma não pretende barrar novos materiais e tecnologias; o Anexo E orienta como avaliá-los (5.1, nota)."
);

// ------------------------------------------------------------------ 5
h1("5. Projeto: regras gerais e abastecimento");
ul(
  "O projeto é feito por **profissional habilitado**, com os dados de registro em todos os elementos, em qualquer etapa (6.1.1).",
  "Requisitos de projeto durante a vida útil: preservar a potabilidade; fornecer água de forma contínua, em quantidade, pressão, vazão e temperatura adequadas; prever acesso para verificação e manutenção; setorizar a distribuição; evitar ruído inadequado; posicionar bem as peças de utilização; minimizar patologias; considerar a manutenibilidade; equilibrar as pressões de água fria e quente a montante de misturadores convencionais (6.2).",
  "Onde há rede pública, é obrigatória a **consulta prévia à concessionária** sobre vazões, pressões, características da água e constância do abastecimento (6.3.1).",
  "Para água de poço, consulta prévia ao órgão gestor de recursos hídricos e verificação do padrão de potabilidade (6.3.2).",
  "Usando água da concessionária e de outra fonte ao mesmo tempo, é preciso impedir o refluxo dessa outra fonte para a rede pública (6.3.3).",
  "Sistema de água não potável, quando existir, é **totalmente independente**. Conexão cruzada é vedada (6.5.1.2).",
  "O abastecimento pode ser direto ou indireto, conforme as informações preliminares e as exigências da concessionária (6.5.2.1)."
);
h2("Alimentador predial (6.5.3)");
ul(
  "Resiste à pressão máxima da fonte e tem capacidade de vazão para abastecer o reservatório na pressão mínima. Essas pressões são informadas pela concessionária.",
  "Enterrado, guarda afastamento horizontal de fontes potencialmente poluidoras. Se ficar na mesma vala de uma tubulação poluidora, deve passar **por cima**: a geratriz inferior externa do alimentador fica acima da geratriz superior externa da outra tubulação (6.5.3.2)."
);

// ------------------------------------------------------------------ 6
h1("6. Reservatórios de água fria");
fig("e2_reservatorio.png", "Esquema 3. Elementos de um reservatório de água potável (elaboração própria).", 580);
h2("Proteção sanitária (6.5.5)");
ul(
  "Opaco ou protegido contra a luz; estanque; com tampa ou porta de acesso opaca e firmemente presa.",
  "Deve permitir ver e reparar vazamentos e impedir contaminação por agente externo.",
  "Toda abertura que se comunique com o exterior é protegida contra a entrada de líquidos, poeira, insetos e outros animais.",
  "Resistente à corrosão ou com revestimento interno protetor. As superfícies acima do nível da água também não podem liberar substâncias nem favorecer biofilme, por causa da condensação."
);
h2("Capacidade e forma (6.5.6)");
ul(
  "**Mínimo:** 24 h de consumo normal, somado ao volume de incêndio quando armazenado junto (6.5.6.2).",
  "**Máximo:** o volume deve preservar a potabilidade durante o tempo de detenção, para não perder o efeito residual do desinfetante. Se não for possível calcular, a nota recomenda limitar a 3 dias de consumo diário ou prever meios de preservação (6.5.6.3).",
  "Reservatórios elevados são divididos em **dois ou mais compartimentos**, para permitir manutenção sem interromper a distribuição. A exceção são as **residências unifamiliares isoladas**. O menor compartimento deve cobrir o pico de consumo durante uma manutenção normal, e cada um opera de forma autônoma (6.5.6.5).",
  "O reservatório inferior pode ter compartimento único quando o volume do superior for suficiente para o período de limpeza do inferior (6.5.6.7).",
  "Forma, posição de entrada e saída e tomada de água devem evitar zonas de estagnação (6.5.6.6).",
  "Em reservatórios interligados, a água deve circular por todos. É vedado operá-los exclusivamente como vasos comunicantes (6.5.6.8)."
);
h2("Instalação e operação (6.5.7 e 6.5.8)");
ul(
  "Reservatório pré-fabricado fica sobre base plana e estável, em local com escoamento para vazamentos; as tubulações ligadas a ele não podem transmitir esforços às paredes (6.5.7.2).",
  "O alimentador predial termina em um componente de controle automático de nível, ajustável e com proteção contra refluxo (6.5.8.1).",
  "Registro de fechamento no alimentador predial, a montante e próximo do reservatório, e na tubulação de recalque, a montante e próximo do reservatório superior (6.5.8.2).",
  "O nível máximo da água fica abaixo da geratriz inferior do extravasor e, se houver, da tubulação de aviso (6.5.8.3)."
);
h2("Limpeza, extravasão e aviso (6.5.9)");
ul(
  "Reservatórios de água fria ou quente têm tubulação de limpeza, com registro de fácil acesso próximo à saída (6.5.9.1).",
  "Reservatório moldado no local: cantos internos arredondados ou chanfrados e fundo com leve declividade para a limpeza (6.5.9.2).",
  "Reservatórios atmosféricos de água fria têm extravasor, dimensionado para escoamento livre e sem risco de bloqueio por partículas flutuantes (6.5.9.3 e 6.5.9.4).",
  "Deve haver um meio de alerta de falha no controle de nível, como a tubulação de aviso de extravasão (6.5.9.5). Quando adotada, ela descarrega imediatamente, em local adequado e de fácil constatação (6.5.9.7), e é derivada do extravasor de modo a não receber a água da limpeza (6.5.9.8).",
  "As extremidades do extravasor e do aviso recebem tela ou malha contra vetores. A área de passagem das frestas deve ser **maior** que a seção interna do tubo (6.5.9.6).",
  "A descarga de extravasão, limpeza e aviso não pode permitir refluxo, conexão cruzada nem entrada de gases. **É vedada a ligação direta com esgoto sanitário e com águas pluviais** (6.5.9.10)."
);
p("O reservatório deve ter abertura e espaço ao redor suficientes para inspeção, manutenção e limpeza com segurança (6.5.10).");

// ------------------------------------------------------------------ 7
h1("7. Recalque e pressurização");
ul(
  "**No mínimo duas bombas independentes**, para manter o abastecimento na falha ou manutenção de uma delas (6.5.11.2). O sistema deve permitir o funcionamento simulado de qualquer bomba para teste (6.5.11.3).",
  "**Alternância automática** entre partidas consecutivas, para não deixar água parada em bomba inoperante (6.5.11.9).",
  "Local com baixa transmissão de ruído e vibração, espaço e acesso para manutenção, ventilação para dissipar calor e drenagem (6.5.11.4). Ruído e vibração dentro dos limites da NBR 10152 (6.5.11.11).",
  "Sucção: evitar vórtice e entrada de ar, proteger contra detritos (6.5.11.5) e posicionar a tomada elevada em relação ao fundo (6.5.11.8). A perda de carga do dispositivo de proteção entra na verificação do NPSH disponível (6.5.11.7).",
  "Bombas selecionadas para não cavitar e para o maior rendimento possível (6.5.11.6 e 6.5.11.12).",
  "Comandos automáticos condicionados ao nível dos reservatórios (6.5.11.16). O sistema não pode ser acionado com o reservatório que o abastece no nível mínimo operacional (6.5.11.17).",
  "**Recalque comum a duas ou mais torres:** partidas e paradas com variação gradual de rotação (6.5.11.13); alternância automática da primeira bomba, uma bomba reserva e isolamento automático da defeituosa, com alarme sonoro ou visual (6.5.11.14).",
  "**Pressurização:** deve garantir a continuidade do abastecimento, com desvio (by-pass) dotado de válvula de retenção e **sem** válvula de bloqueio, para que o abastecimento por gravidade seja automático quando a bomba parar (6.5.11.18). Precisa de dispositivo que admita ar no esvaziamento, expulse ar no enchimento e elimine bolhas em operação (6.5.11.20)."
);

// ------------------------------------------------------------------ 8
h1("8. Distribuição e tubulações");
h2("Setorização (6.5.12)");
p("A distribuição deve permitir manutenção em partes, com registros de fechamento ou dispositivos equivalentes, em especial (6.5.12.4):");
ul(
  "no barrilete, no trecho que o alimenta; no abastecimento indireto, em cada trecho que liga o barrilete ao reservatório;",
  "na coluna de distribuição, a montante do primeiro ramal;",
  "no ramal, a montante do primeiro sub-ramal, em ao menos um dos ambientes sanitários da unidade;",
  "a montante do hidrômetro, quando houver medição individualizada."
);
ul(
  "Em sanitários de uso público, ao menos um ponto de cada tipo de aparelho tem registro exclusivo, para não interditar o ambiente por causa de uma avaria (6.5.12.6).",
  "Medidores de consumo em local de fácil acesso e facilmente removíveis. Se a instalação for futura, o projeto prevê um espaçador de fácil remoção (6.5.12.7).",
  "Água fria e água quente são protegidas uma contra a entrada da outra. **Duchas higiênicas e torneiras com gatilho de ponta** exigem válvula de retenção, no aparelho ou no ponto de utilização (6.5.12.8).",
  "Minimizar a transferência de calor da água quente para a água fria (6.5.12.9) e o tempo de chegada da água quente ao ponto mais distante (6.5.12.10)."
);
h2("Tubulações (6.6)");
ul(
  "Projetar para minimizar o acúmulo de ar ou vapor. Onde um trecho em forma de sifão for inevitável, o ponto mais alto a jusante recebe meio de eliminação de ar (6.6.2).",
  "Trechos horizontais com apoios que evitem flechas, considerando o tubo cheio de água (6.6.3).",
  "O retorno de água quente pode ter dispositivo de recirculação, cujo acionamento não pode causar variações de pressão e vazão que provoquem escaldamento (6.6.4). Com dois ou mais ramais no retorno, as vazões são balanceadas hidraulicamente (6.6.5)."
);

// ------------------------------------------------------------------ 9
h1("9. Vazões, velocidades e pressões");
h2("Vazões (6.7)");
ul(
  "O projeto explicita as vazões consideradas nos pontos de utilização, inclusive as máximas (6.7.1.1 e 6.7.1.2).",
  "O projeto informa expressamente que usar aparelhos de consumo superior ao previsto é responsabilidade do usuário. A informação vai para o manual entregue ao usuário final (6.7.1.3).",
  "Abastecimento do reservatório: repor o volume de consumo diário em até **6 h**; em residências unifamiliares, até **3 h** (6.7.2)."
);
h2("Velocidades (6.8)");
p("A norma trata a velocidade por critério de desempenho, sem fixar um teto obrigatório. O dimensionamento deve limitar a velocidade para evitar:");
ul(
  "ruído acima dos níveis da NBR 10152 (6.8.1);",
  "golpes de aríete prejudiciais aos componentes (6.8.3);",
  "cavitação, sobretudo em mudanças bruscas de direção e em componentes com restrição de seção, como válvulas redutoras e torneiras de boia (6.8.5)."
);
nota("Atenção",
  "O valor de **3 m/s** aparece apenas em nota: adotá-lo como velocidade média máxima limita os picos de sobrepressão, mas **não evita** o golpe de aríete (6.8.3). " +
  "A limitação de velocidade não se aplica a trechos comprovadamente livres de golpe de aríete e com isolação acústica adequada (6.8.4).");
h2("Pressões (6.9)");
ul(
  "A pressão dinâmica mínima no ponto de utilização é a necessária para garantir a vazão de projeto, e nunca inferior a **10 kPa** (6.9.1 e 6.9.2).",
  "Ela pode ser obtida com o fabricante ou pelo fator de vazão da peça: Q = K·√P, com Q em L/s e P em kPa (6.9.2).",
  "Em qualquer ponto da rede de distribuição, pressão dinâmica mínima de **5 kPa**. A exceção são os trechos verticais de tomada d'água na saída de reservatórios elevados para os barriletes, em sistemas indiretos (6.9.3).",
  "Pressão **estática** máxima nos pontos de utilização: **400 kPa** (6.9.4).",
  "Sobrepressões por transientes hidráulicos são admitidas até **200 kPa** acima da pressão dinâmica de projeto (6.9.6).",
  "A montante de misturadores convencionais, as pressões dinâmicas de água fria e quente devem ser próximas, para evitar oscilação de temperatura (6.9.5)."
);
h2("Válvulas e estações redutoras de pressão (6.9.7 a 6.9.15)");
ul(
  "Estação que atende várias unidades ou setores: **pelo menos duas válvulas redutoras em paralelo**, uma delas sobressalente (6.9.7).",
  "Válvula isolada, que atende uma única unidade, um setor, um trecho ou um ponto: pode ser uma só e sem by-pass, desde que o projeto exija manter na edificação ao menos uma válvula sobressalente idêntica (6.9.8).",
  "Cada estação abastece **uma única zona de pressão** (6.9.11).",
  "A seleção respeita o diferencial mínimo, a relação de redução de pressões e a faixa de vazões do equipamento (6.9.9 e 6.9.10).",
  "A estação deve evitar acúmulo de ar na saída (6.9.12), ter proteção contra sobrepressão a jusante em caso de falha, com alerta (6.9.13), e ficar em área comum, com acesso e drenagem (6.9.15)."
);

// ------------------------------------------------------------------ 10
h1("10. Água quente");
fig("e5_temperaturas.png", "Esquema 4. Temperaturas de referência da norma (elaboração própria).", 600);
h2("Limites de temperatura e escaldamento (6.10)");
ul(
  "Trechos que possam conduzir água acima de **70 °C** são identificados, isolados e protegidos (6.10.2).",
  "Em ambientes sanitários com misturadores convencionais, a água na tubulação é limitada a **70 °C**. Acima disso, é obrigatório um meio automático de segurança intrínseca que limite a temperatura nos pontos (6.10.3).",
  "Onde a água para **uso corporal** puder passar de **45 °C**, usa-se recurso automático de segurança intrínseca para limitar a esse valor (6.10.4.3).",
  "Em hospitais, escolas, jardins de infância e residências de idosos, a temperatura máxima é limitada automaticamente. A nota recomenda 38 °C para duchas higiênicas, jardins de infância e determinadas clínicas e hospitais (6.10.4.4).",
  "A tubulação de água fria que alimenta aquecedor ou misturador **não pode** alimentar aparelho cuja operação cause transiente de pressão ou escaldamento, como a válvula de descarga (6.10.4.1).",
  "Superfícies expostas do sistema de água quente recebem isolamento térmico contra queimaduras (6.10.5). A água fria é protegida de fontes de calor, inclusive onde cruza ou passa perto de tubos de água quente (6.10.6).",
  "Onde a temperatura puder passar de **90 °C**, tomam-se precauções contra danos ao sistema e aos usuários. Dispositivos de segurança ficam acessíveis (6.10.7)."
);
h2("Dilatação e isolamento térmico (6.11 e 6.12)");
fig("e6_braco_flexao.png", "Esquema 5. Braço de flexão: o trecho perpendicular absorve a dilatação ΔL do trecho longo (elaboração própria).", 430);
ul(
  "O projeto considera dilatação e contração e prevê liras ou juntas de expansão quando necessário. Sem essa possibilidade, usam-se ancoragens, suportes, tubos e conexões que resistam às tensões e à fadiga (6.11.2).",
  "Apoios e abraçadeiras com material resiliente entre o tubo e a fixação (6.11.3).",
  "Mudanças de direção e derivações devem absorver a movimentação de trechos retos longos, pelo próprio traçado (braço de flexão) ou por componente adequado (6.11.4).",
  "O sistema de **distribuição de água quente tem isolamento térmico em toda a extensão** (6.12.3). Aquecedores, reservatórios e tubulações são projetados para reduzir perdas, que devem ser estimadas no projeto (6.12.1 e 6.12.2)."
);
h2("Geração e armazenamento (6.13)");
ul(
  "O projeto especifica tipo de aquecimento, volume, temperaturas máxima e mínima de operação, fonte de calor e potência (6.13.1.1).",
  "Se a desinfecção térmica usar o próprio sistema, ele deve ser capaz de gerar água acima de 70 °C (6.13.1.4).",
  "O trecho horizontal de alimentação de água fria do reservatório de água quente **não pode ter isolamento térmico** e deve ser de material resistente à água quente, com volume interno equivalente à máxima expansão térmica prevista (6.13.1.5).",
  "**Geração que possa passar de 95 °C:** cada aquecedor tem controle térmico; tem corte por temperatura com intervenção manual, independente do controle térmico; e, onde necessário, meio de dissipar energia se o controle falhar (6.13.2.1).",
  "**Nenhuma válvula** pode ficar entre o recipiente e a válvula de alívio de pressão e temperatura (6.13.2.3).",
  "A descarga da válvula de alívio tem diâmetro no mínimo igual ao do orifício de saída (6.13.2.6), é feita com separação atmosférica sobre recipiente de recolhimento logo abaixo da válvula (6.13.2.7) e não pode gerar perigo nem danos elétricos, dando aviso perceptível quando atua (6.13.2.8).",
  "Recipiente com dispositivo de segurança não mecânico (fusível tampão) também precisa de válvula de alívio de temperatura que abra a uma temperatura pelo menos 5 °C inferior à de atuação desse dispositivo (6.13.2.9)."
);
p("Condições de instalação de aquecedores de acumulação e reservatórios de água quente (6.13.3.1):");
ul(
  "o ramal de água fria não pode permitir o esvaziamento do equipamento, a não ser pelo dreno;",
  "alimentado por gravidade, o equipamento permanece escorvado mesmo com o reservatório de água fria vazio;",
  "a saída de água quente tem expulsão automática de bolhas e admissão automática de ar, sem criar trechos de estagnação e sem registro entre esse recurso e a saída;",
  "alimentado por gravidade, é vedada válvula de retenção no ramal de água fria que não esteja protegido contra expansão térmica;",
  "a alimentação de água fria tem sifão térmico ou meio equivalente;",
  "**é vedado respiro coletivo.**"
);
p("Além disso, esses equipamentos têm limitador automático de temperatura e válvula de segurança à temperatura (6.13.3.2), dreno (6.13.3.4) e limitador automático de pressão, como válvula de alívio ou de segurança à pressão (6.13.3.5).");

// ------------------------------------------------------------------ 11
h1("11. Dimensionamento da distribuição");
ul(
  "As tubulações são dimensionadas para atender às vazões e pressões de projeto. O método de determinação das vazões deve ser **justificado** no projeto (6.14.1).",
  "A vazão de cálculo em cada trecho vem de método **reconhecido ou devidamente fundamentado, empírico ou probabilístico** (6.14.2). A norma não impõe um método único.",
  "Os diâmetros decorrem de velocidades, vazões, limitação de ruído, forma de instalação, material e perda de carga disponível. **Não há diâmetro nominal mínimo para sub-ramais** e engates (6.14.3).",
  "Perdas de carga calculadas por equações pertinentes. A nota indica a **equação universal** como a mais adequada (6.14.4)."
);

// ------------------------------------------------------------------ 12
h1("12. Proteção sanitária e refluxo");
p("O sistema não pode afetar a qualidade da água por contato com materiais inadequados, refluxo, interligação entre água potável e não potável ou conexão cruzada com esgoto e águas pluviais (6.15).");
ul(
  "Tubulação não pode ser projetada enterrada em solo contaminado. Se for inevitável, adotam-se medidas de proteção (6.15.1.1).",
  "Tubulação não pode ficar alojada em locais que comprometam a água, como caixas de inspeção, tanques sépticos, sumidouros, valas de infiltração e depósitos de lixo (6.15.1.2)."
);
h2("Proteção contra refluxo (6.15.2)");
ul(
  "**Proteção localizada** em cada ponto de utilização e de suprimento, com dispositivo o mais próximo possível do ponto (6.15.2.2).",
  "A **separação atmosférica padronizada** é o recurso mais efetivo. Outros recursos são aceitos se derem resultado satisfatório, como a separação não padronizada e o quebrador de vácuo (6.15.2.3).",
  "**Quebrador de vácuo não protege** onde o refluxo ocorre por vasos comunicantes (6.15.2.3, nota).",
  "Em edifícios de vários pavimentos alimentados por reservatório superior, além da separação atmosférica, cada coluna de distribuição tem meio de admitir ar no esvaziamento, expulsar ar no enchimento e eliminar bolhas. A solução não pode criar estagnação, e o registro da coluna não pode impedir a atuação desse recurso (6.15.2.4)."
);
fig("e3_separacao.png", "Esquema 6. Separação atmosférica: o que significam S, L e d (elaboração própria).", 520);
tabela(["Diâmetro interno d do tubo (mm)", "Separação atmosférica mínima S (mm)"], [
  ["até 14", "20"],
  ["acima de 14 até 21", "25"],
  ["acima de 21 até 41", "70"],
  ["acima de 41", "2 vezes o diâmetro (2d)"],
], [4819, 4819], { centro: true, junto: true });
p("Em todos os casos, a distância L entre o ponto de suprimento e qualquer obstáculo ao redor deve ser de pelo menos 3d.");
fig("e7_refluxo_conjunto.png", "Esquema 7. Edificações abastecidas por tubulação comum: cada uma tem seu dispositivo de proteção contra refluxo (elaboração própria, a partir da legenda da figura da norma).", 520);
h2("Biofilme (6.16)");
ul(
  "Minimizar trechos terminais sem renovação frequente de água (trechos mortos) e a extensão de tubos respiro (6.16.1).",
  "O sistema de água quente deve permitir a desinfecção periódica de todas as partes em contato com a água (6.16.2). A NBR 16824 e o Anexo F trazem os procedimentos."
);

// ------------------------------------------------------------------ 13
h1("13. Golpe de aríete, uso racional e instalação das tubulações");
ul(
  "**Golpe de aríete:** o fechamento de aparelhos não pode gerar sobrepressão acima de 200 kPa. Quando necessário, prevê-se dispositivo amortecedor próximo ao local onde o transiente é gerado (6.17).",
  "**Uso racional:** o projeto pode buscar eficiência no uso de água e energia (Anexo D). Se a edificação adotar princípios de conservação de água, deve atender também à NBR 16792 (6.18)."
);
h2("Acessibilidade e relação com a construção (6.19)");
ul(
  "Não pode haver interferência física com a estrutura. A tubulação **não pode ser embutida nem solidarizada longitudinalmente** a elementos estruturais (6.19.1.1 e 6.19.1.2).",
  "Na travessia de elemento estrutural no sentido da espessura, prevê-se abertura dimensionada. A vedação do interstício deve permitir a movimentação livre do tubo (6.19.1.3).",
  "Em alvenaria estrutural, a tubulação fica em duto ou elemento projetado para isso e considerado no projeto estrutural (6.19.1.4).",
  "Em paredes e pisos não estruturais, considerar a dificuldade de manutenção. A nota destaca as vantagens de soluções acessíveis, como shafts com cobertura removível, sancas, rodapés próprios e carenagens (6.19.2.1).",
  "Tubulação aparente: protegida contra impactos e com suportes que não a prejudiquem (6.19.3).",
  "Tubulação enterrada: metálica protegida contra corrosão externa; resistente a cargas de superfície e a recalques; afastada de fundações, sem interceptar o bulbo de tensões de fundação direta; registros enterrados com caixa de proteção ou canaleta (6.19.4)."
);

// ------------------------------------------------------------------ 14
h1("14. Execução e ensaios");
ul(
  "Execução conforme o projeto. Alterações durante a obra são **previamente aprovadas** (7.1.1 e 7.1.2).",
  "A execução ocorre sob **supervisão de profissional habilitado**. A verificação de conformidade é registrada e rastreável, conforme a NBR 15932 (7.1.3 e 7.1.4).",
  "Materiais e componentes passam por inspeção visual antes da instalação, com registro (7.2.1).",
  "Ferramentas de acoplamento, como rosqueadeiras, termofusores e alicates crimpadores, devem estar calibradas e conservadas (7.2.3.3).",
  "Trechos visíveis recebem pintura de identificação conforme a NBR 6493 (7.4.3). Aberturas de verificação de tubulações embutidas ou recobertas identificam cada tubulação (7.4.2).",
  "As tubulações passam por ensaio de suportação conforme a NBR 15575-6 (7.5).",
  "Ao final, elaboram-se os desenhos conforme construído (as built) (7.6)."
);
h2("Ensaios de estanqueidade (7.3)");
tabela(["Ensaio", "Condição", "Critério de aprovação"], [
  ["Tubulações (7.3.1)", "Cada seção submetida a 600 kPa ou a 1,5 vez a máxima pressão de trabalho, o que for menor. Água quente: água a no mínimo 80 °C, antes do isolamento ou do recobrimento.", "Sem vazamento nem queda de pressão manométrica por no mínimo 1 h após a estabilização."],
  ["Peças de utilização (7.3.2)", "Pressão estática prevista, com as peças sendo manobradas.", "Sem vazamento nem queda de pressão por no mínimo 1 h."],
  ["Reservatório (7.3.3)", "Cheio até o nível máximo permitido pelo controle de nível.", "Sem vazamento nem extravasamento por no mínimo 72 h."],
], [2300, 4038, 3300], { junto: true });
p("Em caso de reprovação, o ensaio é refeito depois das correções. O ensaio de proteção contra refluxo está no Anexo A.");

// ------------------------------------------------------------------ 15
h1("15. Operação, uso e manutenção");
ul(
  "Os procedimentos de manutenção se baseiam no projeto, no as built, nos registros de execução e nas especificações dos fabricantes, e seguem a NBR 5674 (8.1.1 e 8.1.2).",
  "Reformas durante a operação são registradas e aprovadas por profissional habilitado, além de atender à NBR 16280 (8.1.8).",
  "Válvulas redutoras são verificadas por leitura de manômetros calibrados a montante e a jusante. Em estação redutora, a válvula com defeito é isolada e a sobressalente segue em operação (8.2.2). **É vedado operar sem a válvula redutora** (8.2.3).",
  "A potabilidade é monitorada periodicamente, com atenção especial aos reservatórios (8.3.1). Constatada contaminação, elimina-se a causa e restauram-se as condições do sistema (8.3.3).",
  "O consumo é controlado por leituras periódicas dos medidores (8.4.2). Registros de fechamento são operados periodicamente para confirmar o bloqueio (8.4.5).",
  "Se houver água para uso corporal acima dos limites de temperatura, o ponto é bloqueado ou limitado até a correção (8.6.4)."
);
h2("Periodicidades máximas de manutenção (Tabela 2 da norma, reorganizada)");
p("A regra geral é verificação **semestral**. São **anuais** a verificação dos dispositivos de proteção contra refluxo e todas as atividades do grupo de temperatura. Os prazos são máximos e podem ser reduzidos conforme as condições de campo (8.1.4).");
tabela(["Profissional", "Semestral", "Anual"], [
  ["Habilitado", "Válvulas de alívio e válvulas de segurança à pressão", "(nenhuma atividade)"],
  ["Qualificado", "Válvulas redutoras de pressão; vasos de expansão térmica; bombas e pressurizadores; capacidade filtrante de filtros", "Dispositivos de proteção contra refluxo; válvulas termostáticas; dispositivos limitadores de temperatura"],
  ["Capacitado", "Vasos e tanques de pressão; limpeza de reservatórios e da distribuição; simultaneidade das válvulas em estações redutoras; deterioração e oxidação; estanqueidade de reservatório, distribuição, registros e peças de utilização; funcionamento das peças; espaços de tubulações; limpeza de crivos e arejadores", "Liras e juntas de expansão; temperatura das fontes de aquecimento; integridade do isolante térmico"],
], [1700, 4438, 3500], { junto: true });

// ------------------------------------------------------------------ 16
h1("16. Anexos");
tabela(["Anexo", "Caráter", "Conteúdo em resumo"], [
  ["A", "Normativo", "Ensaio de proteção contra refluxo. Separação atmosférica: com o reservatório no nível máximo, simula-se a falha da boia e mede-se a separação, que deve atender aos mínimos. Válvula de retenção: com o sistema pressurizado, fecha-se o registro a montante e abre-se um dreno; é estanque se não houver fluxo após 1 h."],
  ["B", "Normativo", "Corrosão e degradação. Componentes com ferro ficam isolados dos componentes com cobre (par galvânico). Plásticos sem aditivo são protegidos de radiação ultravioleta e calor; os suscetíveis à fadiga não podem sofrer golpes de aríete."],
  ["C", "Informativo", "Ruídos e vibrações. Apoios resilientes, dutos vedados, isoladores de vibração. Alimentação afogada do reservatório para evitar ruído, desde que haja quebrador de vácuo ou outra proteção contra refluxo."],
  ["D", "Informativo", "Eficiência energética. Aquecedores nível A no PBE, menor volume armazenado, menor percurso de distribuição. Em sistema sem recirculação, isolar a tubulação de água quente com mais de 1,5 m a jusante do aquecedor."],
  ["E", "Informativo", "Critérios para avaliar novos materiais, componentes e tecnologias."],
  ["F", "Informativo", "Limpeza e desinfecção. Limpeza do reservatório sem sabão ou detergente, com solução de cloro livre a 1,0 mg/L aplicada três vezes, em intervalos de 30 min. Desinfecção química: 20 mg/L, repouso de 2 h; depois, repouso de 12 h e escoamento de 4 min por ponto. Desinfecção térmica: 70 °C, por 30 min em cada peça. A água não deve ser usada durante os procedimentos e os ocupantes são avisados antes."],
], [900, 1500, 7238]);

// ------------------------------------------------------------------ 17
h1("17. Onde a banca costuma inverter");
ul(
  "**5 kPa e 10 kPa.** O primeiro vale para qualquer ponto da rede; o segundo, para o ponto de utilização. Os dois são pressões dinâmicas.",
  "**400 kPa é pressão estática.** Os 200 kPa são sobrepressão transitória acima da pressão dinâmica de projeto.",
  "**Ensaio de estanqueidade:** 600 kPa ou 1,5 vez a pressão de trabalho, o que for **menor**. Tubulações e peças: 1 h. Reservatório: 72 h.",
  "**3 m/s** não é requisito e não evita golpe de aríete.",
  "**24 h** é o mínimo obrigatório de reserva; **3 dias** é recomendação de máximo, em nota.",
  "**6 h** para repor o reservatório; **3 h** em residência unifamiliar.",
  "**Compartimentos:** reservatório elevado tem dois ou mais, exceto em residência unifamiliar isolada.",
  "**Válvulas redutoras:** em paralelo, não em série. Válvula isolada pode ser única, com sobressalente guardada.",
  "**45 °C** para uso corporal; **70 °C** em ambiente sanitário com misturador convencional; **38 °C** é recomendação em nota.",
  "**Isolamento térmico:** toda a distribuição de água quente, no corpo da norma. O critério de 1,5 m está em anexo informativo.",
  "**Anexos normativos:** apenas A e B. Os anexos C, D, E e F são informativos.",
  "**Separação atmosférica** é o recurso mais efetivo contra refluxo. Quebrador de vácuo não resolve o refluxo por vasos comunicantes.",
  "**Extravasão, limpeza e aviso** não podem ser ligados diretamente ao esgoto nem às águas pluviais.",
  "**Método de cálculo:** a edição de 2020 não impõe método nem tabela de pesos; exige método reconhecido ou fundamentado, justificado no projeto. Desconfie de questões baseadas em material anterior a 2020."
);

module.exports = { blocos };
