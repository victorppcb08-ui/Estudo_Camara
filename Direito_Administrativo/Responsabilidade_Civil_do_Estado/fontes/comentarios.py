# Comentários por questão (chave = id do TEC Concursos).
# t = item do edital (6.1A teorias | 6.1B quem responde | 6.1C ação, regresso, prescrição |
#     6.1D atos legislativos, judiciais e casos especiais | 6.2 | 6.3 | 6.4 | 6.5)
# c = comentário; a = alerta de pegadinha (opcional)

C = {}
def q(i, t, c, a=None):
    C[i] = {'t': t, 'c': c, 'a': a}

# ---------------- 6.1 A — conceito, evolução e teorias ----------------
q('4148298', '6.1A', 'A responsabilidade extracontratual do Estado é tema de direito público: desde o caso Blanco (1873) entende-se que ela não se rege pelos princípios do Código Civil, mas por regras próprias (MSZ 15.2.3). Está no art. 37, § 6º, da CF, dentro do capítulo da Administração Pública.',
  'O Código Civil (art. 43) também trata do tema, mas isso não tira a matéria do direito administrativo.')
q('3374000', '6.1A', 'Correto. Teoria da irresponsabilidade: Estado absolutista, soberania incontestável, "the king can do no wrong" / "le roi ne peut mal faire". O Brasil nunca a adotou (MSZ 15.3).')
q('3103037', '6.1A', 'Correto. "The king can do no wrong" e "quod principi placuit habet legis vigorem" são as máximas da teoria da irresponsabilidade (MSZ 15.2.1).',
  'EUA e Inglaterra só abandonaram a irresponsabilidade em 1946 (Federal Tort Claims Act) e 1947 (Crown Proceedings Act). Datas que a banca troca.')
q('2613075', '6.1A', 'A distinção atos de império × atos de gestão pertence à primeira fase das teorias civilistas, abandonada por ser impossível dividir a personalidade do Estado (MSZ 15.2.2). Hoje o ponto de partida é o art. 37, § 6º (risco administrativo).')
q('3733846', '6.1A', 'Gabarito C. A sistematização clássica da faute du service (culpa anônima) é atribuída a Paul Duez, com três modalidades: o serviço não funcionou, funcionou mal ou funcionou atrasado (retardamento). Duguit, Hauriou e Rolland são nomes do direito público francês colocados como distratores.',
  'Questão de "autor". Guarde: culpa do serviço → Paul Duez → inexistência, mau funcionamento ou retardamento.')
q('3450856', '6.1A', 'Correto. No risco integral o Estado é "segurador universal": basta o dano ligado à atividade, e as excludentes (culpa da vítima, de terceiro, força maior) não são admitidas (Hely; MSZ 15.2.3). É exceção no Brasil (danos nucleares, atentados terroristas contra aeronaves).')
q('4148369', '6.1A', 'A regra é o risco administrativo, que admite excludentes. Mesmo no risco integral é preciso dano e vínculo com a atividade; "bastando a demonstração do dano" é exagero.',
  'Duas armadilhas no mesmo item: "risco integral" como regra e "bastando o dano".')
q('3661479', '6.1A', 'A regra geral é o risco administrativo. A segunda parte (afastada por culpa exclusiva da vítima, de terceiro ou força maior) descreve justamente o risco administrativo, não o integral.',
  'Item com definição certa e rótulo errado. Leia o nome da teoria.')
q('2208322', '6.1A', 'Prevalece o risco administrativo (art. 37, § 6º). Risco integral só em hipóteses excepcionais previstas em norma.')
q('2119127', '6.1A', 'Gabarito E. Pela doutrina clássica e pelo STF, a CF/88 adota, em regra, a teoria do risco administrativo. Culpa anônima e falta do serviço são a mesma teoria (subjetiva), aplicada à omissão genérica.',
  'Culpa anônima = falta do serviço = faute du service = culpa administrativa = acidente administrativo. Se a banca puser duas delas como alternativas, nenhuma é a regra da CF.')
q('2339346', '6.1A', 'A CF/88 adotou a teoria do risco administrativo (responsabilidade objetiva). A culpa anônima/culpa do serviço é subjetiva e aparece na omissão genérica, não como regra constitucional.')
q('2028192', '6.1A', 'Correto. Foi a CF/1946 (art. 194) que consagrou a responsabilidade objetiva; desde então as Constituições mantiveram a regra, e a CF/88 a estendeu às pessoas privadas prestadoras de serviço público (MSZ 15.3).',
  'Linha do tempo: CC/1916 (subjetiva) → CF/1934 e 1937 (solidária, com culpa) → CF/1946 (objetiva) → CF/1967 (regresso com "dolo ou culpa") → CF/1988 (inclui privadas prestadoras).')
q('3429053', '6.1A', 'Gabarito E. (a) imperícia é falta de aptidão técnica, não negligência; (b) a intenção deliberada é dolo, não culpa; (c) objetiva dispensa culpa; (d) risco profissional é responsabilidade objetiva; (e) correta: o risco administrativo dispensa a prova de culpa, mas exige dano e nexo com a atividade pública.')
q('2367872', '6.1A', 'Anulada. A tese de que danos nucleares seguem o risco integral é a da doutrina (MSZ 15.2.3, citando o art. 21, XXIII, d, da CF). Mas a Lei nº 6.453/1977 admite exclusão: culpa exclusiva da vítima (art. 6º) e conflito armado, guerra civil, insurreição ou excepcional fato da natureza (art. 8º). Por isso o item, que dizia que culpa da vítima, fato de terceiro e força maior não rompem o nexo, ficou sem resposta segura.',
  'Em item genérico ("danos nucleares independem de culpa"), marque CERTO: é a letra do art. 21, XXIII, d. Cuidado só quando o item afirmar que nenhuma excludente é aceita.')
q('3202210', '6.1A', 'Correto. Art. 21, XXIII, d, da CF: "a responsabilidade civil por danos nucleares independe da existência de culpa". Vale para ação ou omissão.')
q('2520660', '6.1A', 'Correto. Letra do art. 21, XXIII, d, da CF.')
q('3048721', '6.1A', 'Gabarito C (III e IV). I: a regra é objetiva. II: há responsabilidade por omissão. III: risco administrativo admite excludentes, como culpa exclusiva da vítima. IV: o nexo causal é indispensável.')
q('2875355', '6.1A', 'Correto. MSZ (15.1): obrigação de reparar danos causados a terceiros por comportamentos comissivos ou omissivos, materiais ou jurídicos, lícitos ou ilícitos. A responsabilidade é sempre civil, de ordem pecuniária, e abrange dano material e moral.')

# ---------------- 6.1 B — quem responde ----------------
q('3348044', '6.1B', 'Concessionárias respondem objetivamente pelo risco administrativo (art. 37, § 6º), que admite excludentes. Risco integral é exceção.')
q('2796448', '6.1B', 'Gabarito B. Concessionária de transporte, no exercício do serviço público, responde objetivamente (risco administrativo): provar conduta, dano e nexo. (d) "risco do negócio" é linguagem do CDC, não do art. 37, § 6º.')
q('2854349', '6.1B', 'Responsabilidade objetiva da concessionária perante o usuário (art. 37, § 6º; Lei 8.987/95, art. 25): o usuário não precisa provar dolo ou culpa do preposto.')
q('3206584', '6.1B', 'Correto. STF, RE 591.874 (Tema 130): a responsabilidade das prestadoras privadas é objetiva tanto perante usuários quanto perante não usuários. MSZ (15.3) critica o entendimento antigo (RE 262.651) que restringia a objetiva aos usuários.')
q('2424371', '6.1B', 'Dois erros: o § 6º alcança as privadas prestadoras de serviço público, não as exploradoras de atividade econômica; e o regresso é assegurado, não vedado, nos casos de dolo ou culpa.',
  'Troca de "prestadoras de serviço público" por "exploradoras de atividade econômica" é a pegadinha mais comum do art. 37, § 6º.')
q('2450543', '6.1B', 'Gabarito D. A concessionária responde objetivamente e em nome próprio (Lei 8.987/95, art. 25); o poder concedente responde de forma subsidiária, se ela não tiver como pagar. Não há solidariedade.',
  'Concessionária = responsabilidade primária. Poder concedente = subsidiária. "Solidária" está errado.')
q('2452982', '6.1B', 'Gabarito E. A natureza da responsabilidade é objetiva perante todos: passageiros (usuários), pedestre e dono do muro (não usuários), conforme o Tema 130. O choque provocado por terceiro não muda a natureza da responsabilidade; no transporte de pessoas, a culpa de terceiro sequer exclui o dever de indenizar o passageiro (CC, art. 735; Súmula 187 do STF).',
  'A pergunta é sobre a natureza (objetiva ou subjetiva), não sobre se a empresa vai pagar no final. Não misture os planos.')
q('1972639', '6.1B', 'Anulada. O Tema 940 fala em ação contra "o Estado ou a pessoa jurídica de direito privado prestadora de serviço público". O item falou em sociedade de economia mista sem dizer se presta serviço público ou explora atividade econômica. Se explora atividade econômica, o § 6º não se aplica.',
  'Estatal sem qualificação é ambígua. Procure no enunciado "prestadora de serviço público".')
q('2208581', '6.1B', 'Inverteu e errou: a responsabilidade das privadas prestadoras é objetiva para usuários e para não usuários (Tema 130).')
q('2591966', '6.1B', 'Gabarito D, letra do art. 37, § 6º: pessoas jurídicas de direito público e as de direito privado prestadoras de serviço público; agentes "nessa qualidade"; terceiros; regresso "nos casos de dolo ou culpa".',
  'Questão de letra de lei. As erradas tiram "prestadoras de serviços públicos", dispensam dolo/culpa no regresso ou vedam o regresso.')
q('2182032', '6.1B', 'Gabarito E. Respondem as pessoas jurídicas de direito público e as de direito privado prestadoras de serviço público, com direito de regresso. Exploradoras de atividade econômica ficam fora do § 6º (CF, art. 173, § 1º, II).')
q('2028191', '6.1B', 'O § 6º alcança também as pessoas jurídicas de direito privado prestadoras de serviço público (concessionárias, permissionárias, estatais prestadoras, cartórios, entidades do terceiro setor que recebam delegação).')
q('2756960', '6.1B', 'Gabarito C. I: o Corpo de Bombeiros é órgão, sem personalidade jurídica; quem responde é o Estado. II: empresa pública prestadora de serviço público responde pelo § 6º. III: o regresso exige dolo ou culpa.',
  'Órgão não responde: polícia civil, Corpo de Bombeiros, secretaria, gabinete. Responde a pessoa jurídica a que pertencem.')
q('2795820', '6.1B', 'Gabarito D. I: polícia civil é órgão, sem personalidade; responde o Estado. II: regresso nos casos de dolo ou culpa. III: art. 21, XXIII, d.')
q('2156812', '6.1B', 'STF, RE 842.846 (Tema 777): o Estado responde objetivamente pelos atos dos tabeliães e registradores, com dever de regresso contra o responsável nos casos de dolo ou culpa, sob pena de improbidade. A responsabilidade do Estado não segue a culpa do serviço.',
  'Estado → objetiva. Notário → subjetiva (Lei 8.935/94, art. 22, com redação da Lei 13.286/2016). Não inverta.')
q('2520659', '6.1B', 'O exercício em caráter privado, por delegação (CF, art. 236), não afasta a responsabilidade objetiva do Estado (Tema 777). MSZ inclui os cartórios extrajudiciais entre os sujeitos do § 6º.')
q('2486043', '6.1B', 'Gabarito A. O Tema 777 diz que o regresso contra o notário é dever, "sob pena de improbidade"; na esfera federal a Lei 4.619/65 já tornava obrigatória a ação regressiva (MSZ 15.8). (b) o STF não equiparou notários a pessoas jurídicas prestadoras; (c) o Estado responde sem depender de dolo ou culpa; (d) o notário responde por dolo ou culpa (subjetiva); (e) não há risco integral.')
q('2593553', '6.1B', 'Gabarito A. Ato de notário gera responsabilidade objetiva do Estado (Tema 777), e a banca aplicou a lógica da dupla garantia (ação contra o Estado). (b) exploradoras seguem o regime privado; (c) fato imprevisível (força maior) pode excluir; (d) omissão nem sempre é objetiva; (e) obra feita por empreiteiro: o empreiteiro responde pelos danos que causar (Lei 14.133/21, art. 120), mas o Estado não fica totalmente isento (pode responder subsidiariamente ou pelo só fato da obra).')
q('4249217', '6.1B', 'Correto. Autarquia (direito público) e empresa pública prestadora de serviço público respondem objetivamente pelo risco administrativo.')
q('1624286', '6.1B', 'Estatal que explora atividade econômica não está no art. 37, § 6º; submete-se ao regime das empresas privadas (CF, art. 173, § 1º, II), em regra responsabilidade subjetiva.',
  'Pode haver responsabilidade objetiva por outra lei (por exemplo, o CDC numa relação de consumo), mas não "conforme a teoria do risco administrativo".')
q('1727741', '6.1B', 'A Caixa explora atividade econômica (bancária); não está no § 6º. O item atribuiu responsabilidade objetiva pelo regime do Estado, e a banca deu ERRADO.',
  'Perante o consumidor bancário a Caixa responde objetivamente pelo CDC (art. 14). A banca, porém, julga pelo art. 37, § 6º. Leia o fundamento pedido.')
q('1120734', '6.1B', 'Gabarito B. Entidade da indireta com personalidade de direito privado que explora atividade econômica submete-se ao regime de responsabilidade civil privada.')
q('2415154', '6.1B', 'Gabarito C. Entidade da indireta tem personalidade própria e responde com patrimônio próprio; o ente político responde apenas subsidiariamente. (a) não há responsabilidade "preventiva" na CF; (b) dano moral é autônomo (Súmula 37 do STJ); (d) delegatários e concessionários estão no § 6º.')
q('3206683', '6.1B', 'Correto. STF (AI 473.381): o intérprete não pode distinguir quanto ao "terceiro"; o Estado responde qualquer que seja a vítima, servidor público ou não (MSZ, nota 2 do cap. 15).')
q('3441736', '6.1B', 'STF, RE 662.405 (Tema 512): o Estado responde subsidiariamente (não solidariamente) por danos materiais a candidatos quando o concurso organizado por pessoa jurídica de direito privado é cancelado por indícios de fraude.',
  'Concurso cancelado por fraude: banca organizadora responde direta e objetivamente; Estado, subsidiariamente.')
q('3950180', '6.1B', 'Gabarito D (II, III e IV). I: é aplicável a responsabilidade por ato baseado em lei declarada inconstitucional (MSZ 15.6). II: objetiva mesmo para não usuário (Tema 130). III: permissionária responde objetivamente quando o dano decorre do serviço. IV: o risco administrativo examina o comportamento estatal e admite excludentes.')
q('2789358', '6.1B', 'Gabarito C. Empresa pública prestadora de serviço público responde objetivamente, mas ainda é preciso provar dano e nexo causal. (a) é objetiva, como a do Estado; (b) a regra é o risco administrativo; (d) culpa concorrente atenua, não rompe o nexo; (e) o regresso exige dolo ou culpa do empregado.')

# ---------------- 6.1 C — ação, regresso, reparação, prescrição ----------------
q('3312851', '6.1C', 'Correto. STF, RE 1.027.633 (Tema 940): ação contra o Estado ou a pessoa jurídica privada prestadora de serviço público; o agente autor do ato é parte ilegítima (dupla garantia, RE 327.904).',
  'A doutrina (MSZ, Celso Antônio, Cahali) admite ação direta contra o agente ou litisconsórcio. Em prova, prevalece o STF: só contra a pessoa jurídica.')
q('3962945', '6.1C', 'Correto. Item da própria Câmara dos Deputados (Policial Legislativo, 2026). Tema 940: a ação vai contra o Estado (pessoa jurídica), que tem regresso contra o servidor nos casos de dolo ou culpa.',
  'Prova recente da Câmara, mesma banca. Esse é o padrão que cai: dupla garantia + regresso com dolo ou culpa.')
q('4148376', '6.1C', 'Correto. O regresso contra o agente é subjetivo: depende de dolo ou culpa (art. 37, § 6º, parte final).')
q('3495310', '6.1C', 'Correto. Só há regresso se demonstrado dolo ou culpa do agente. Responsabilidade do Estado: objetiva; do agente: subjetiva (MSZ 15.3).')
q('3552572', '6.1C', 'A banca deu ERRADO. A ação é contra a pessoa jurídica a que o agente se vincula, que nem sempre é "o Estado" ente político: pode ser autarquia, fundação ou pessoa privada prestadora de serviço público. Por isso o "somente contra o Estado" foi considerado restritivo demais.',
  'Compare com o item da Câmara 2026 ("deve ser ajuizada diretamente contra o Estado", CERTO). A palavra "somente" e a ausência das demais pessoas jurídicas mudaram o gabarito. Diante de "somente/apenas", pergunte: existe outra pessoa que também responde?')
q('3681718', '6.1C', 'Gabarito D. O Estado responde objetivamente; o servidor não pode ser acionado diretamente pela vítima (Tema 940), mas responde em regresso, por culpa (distração) ou dolo. (b) regresso também por culpa, não só dolo; (c) o exercício da função não é excludente; (e) o servidor agia nessa qualidade.')
q('3732678', '6.1C', 'Gabarito C. Nenhum servidor responde diretamente perante a vítima (Tema 940). Secretaria de saúde e gabinete são órgãos do Estado.',
  'Rigor técnico: o servidor da autarquia (João) e o da fundação (Frederico) geram responsabilidade da própria autarquia e da própria fundação, que têm personalidade. A alternativa "o Estado" ganha por eliminação, porque as outras atribuem responsabilidade direta ao servidor.')
q('2775373', '6.1C', 'Marcos é parte ilegítima (Tema 940); a ação vai contra a concessionária, que responde objetivamente. O DF (poder concedente) só responde de forma subsidiária. Logo, a alternativa "ou o DF, ou a concessionária, ou Marcos" está errada.')
q('3103039', '6.1C', 'A reparação pode ser feita na via administrativa, se a Administração reconhecer a responsabilidade e houver acordo sobre o valor (MSZ 15.8).')
q('3202209', '6.1C', 'O regresso exige dolo ou culpa do agente. Conduta, dano e nexo bastam para a vítima contra o Estado, não para o Estado contra o agente.',
  'Item que copia os requisitos da responsabilidade objetiva e os aplica ao regresso. Regresso = subjetivo, sempre.')
q('2332187', '6.1C', 'Gabarito B: o agente pode ressarcir voluntariamente ou na via administrativa (por exemplo, desconto em folha com sua concordância), sem necessidade de ação regressiva. (a) o Tema 777 diz que o regresso contra o notário cabe "nos casos de dolo ou culpa"; a alternativa omitiu essa condição; (c) a vítima não pode incluir o agente no polo passivo (Tema 940); (d) fora das funções não há responsabilidade do Estado; (e) o regresso pressupõe que o Estado tenha sido condenado e pago.',
  'Em múltipla escolha, a alternativa A parece certa, mas omite o requisito de dolo ou culpa. Prefira a alternativa sem condição faltando.')
q('2397434', '6.1C', 'Anulada. A doutrina (MSZ e Cahali, 15.8) admite litisconsórcio facultativo quando o autor alega dolo ou culpa do agente; o STF (Tema 940) não admite. Com fundamentos opostos, o item ficou sem gabarito seguro.',
  'Se o item disser "segundo o STF", o agente é parte ilegítima. Se disser "segundo a doutrina de Maria Sylvia", o litisconsórcio é possível.')
q('1939489', '6.1C', 'Gabarito D, transcrição do Tema 940, com o nome do princípio: dupla garantia (para a vítima, um patrimônio solvente; para o servidor, só responder perante a pessoa jurídica). (a) e (c) atribuem legitimidade ao servidor; (b) nega o regresso; (e) o regresso cabe também por culpa.')
q('1942601', '6.1C', 'Gabarito B. (a) Absolvida a Administração, não há o que ressarcir; (c) o regresso é subjetivo; (d) o prazo de 30 dias para quitar com parcelamento de 24 meses não está na Lei 8.112 (art. 46: parcelas não inferiores a 10% da remuneração; art. 47: 60 dias para quem é demitido ou exonerado); (e) a responsabilidade da concessionária é objetiva e primária. A alternativa B aplica ao regresso contra pessoa privada o prazo trienal do art. 206, § 3º, V, do CC, contado do trânsito em julgado.',
  'Tema de baixa incidência. Guarde a ideia: o regresso nasce do pagamento ou da condenação, não do fato danoso.')
q('2028197', '6.1C', 'Anulada. O art. 46 da Lei 8.112 prevê reposição em folha mediante prévia comunicação ao servidor, e a jurisprudência exige concordância ou processo com contraditório para descontar indenização ao erário. O item admitia leituras opostas.')
q('2151815', '6.1C', 'O prazo de 5 anos (Lei 9.494/97, art. 1º-C; Decreto 20.910/32) alcança também as pessoas jurídicas de direito privado prestadoras de serviço público (MSZ 15.8).',
  'O STJ firmou que contra a Fazenda vale o prazo quinquenal, e não o trienal do Código Civil.')
q('2151828', '6.1C', 'Correto. Responsabilidade objetiva; reparação administrativa possível quando a Administração reconhece a responsabilidade e há acordo sobre o valor. O item reproduz MSZ 15.8.')
q('2181711', '6.1C', 'Gabarito A. (a) Tema 940; (b) o soldado continua sujeito a regresso; (c) a vítima não precisa provar culpa; (d) culpa exclusiva da vítima exclui; (e) sem dano não há responsabilidade.')
q('2181712', '6.1C', 'Gabarito C: sem dolo ou culpa do agente, ou sem a condenação do Estado a indenizar, não há regresso. (a) o dolo ou culpa é apurado na própria ação regressiva; (b) sem nexo não há responsabilidade; (d) os regimes são distintos; (e) o regresso é dever, não faculdade discricionária.')
q('4251369', '6.1C', 'Tema 940: a vítima não pode acionar diretamente o servidor, ainda que ele tenha agido com dolo ou culpa. Dolo ou culpa só importam para o regresso.')
q('4252942', '6.1C', 'Correto. A responsabilidade objetiva da pessoa jurídica não se estende ao regresso, que depende de dolo ou culpa do agente.')
q('2673533', '6.1C', 'Gabarito E. Juízes podem responder em regresso, mas só por dolo ou fraude (CPC, art. 143), conforme o RE 228.977. (a) o regresso cabe por culpa; (b) o ressarcimento pode ser administrativo; (c) o concessionário responde em nome próprio, sem regresso contra o poder concedente; (d) contraria o Tema 777.',
  'Juiz, membro do MP, advogado público e defensor: regresso só com dolo ou fraude (CPC, arts. 143, 181, 184 e 187). Servidor comum: dolo ou culpa.')
q('3994894', '6.1C', 'Gabarito A. A responsabilidade civil do servidor é subjetiva (Lei 8.112, art. 122), e o desconto em folha depende de anuência ou previsão legal. (b) estrito cumprimento do dever não isenta em todos os casos; (c) absolvição criminal por falta de provas não impede as esferas civil e administrativa (só a que nega o fato ou a autoria); (d) é subjetiva; (e) não há prazo de 2 anos.')
q('4222327', '6.1C', 'Gabarito E (todos certos). I: Tema 777. II: "agente" abrange políticos, estatutários, celetistas, temporários e particulares em colaboração (MSZ 15.3). III: depois de indenizar, o Estado tem o dever de cobrar do agente que agiu com dolo ou culpa.')
q('3441733', '6.1C', 'Ação por ato de magistrado vai contra o Estado, não contra o juiz, e muito menos em conjunto (RE 228.977; Tema 940). O juiz responde em regresso por dolo ou fraude.')
q('3639160', '6.1C', 'Gabarito C: em desastres como o rompimento de barragem, admite-se prova exclusivamente testemunhal de danos materiais quando outro meio é impossível. (a) risco social não tem relação com império e gestão; (b) causa excludente de ilicitude penal não afasta a responsabilidade civil do Estado (ato lícito também gera dever de indenizar; CC, arts. 188, II, 929 e 930); (d) o termo inicial é a ciência do dano (actio nata); (e) a denunciação da lide não é obrigatória.')

# ---------------- 6.1 D — atos legislativos, judiciais e casos especiais ----------------
q('3599465', '6.1D', 'Atos jurisdicionais, em regra, não geram responsabilidade do Estado (salvo erro judiciário e prisão além do tempo, CF, art. 5º, LXXV). Não se aplica a teoria da culpa administrativa como regra para eles.')
q('3202350', '6.1D', 'CF, art. 5º, LXXV: "o Estado indenizará o condenado por erro judiciário, assim como o que ficar preso além do tempo fixado na sentença". O trânsito em julgado não impede: a indenização não altera a coisa julgada (MSZ 15.7; CPP, art. 630).')
q('2339352', '6.1D', 'Atos administrativos praticados pelo Legislativo e pelo Judiciário (atividade-meio) seguem a regra geral do art. 37, § 6º: responsabilidade objetiva, sem exigir culpa (MSZ 15.7).',
  'Separe ato jurisdicional (em regra não indeniza) de ato administrativo do Judiciário (indeniza como qualquer ato administrativo).')
q('2498025', '6.1D', 'Correto para a banca. MSZ (15.6) adota a tese da responsabilidade por lei inconstitucional, desde que o vício seja declarado pelo STF e haja dano e nexo.',
  '"Plenamente admissível" foi aceito. Se o item disser que basta a declaração de inconstitucionalidade, sem dano, marque ERRADO (veja a questão da PM PA).')
q('1994117', '6.1D', 'Gabarito D. Há responsabilidade quando a lei declarada inconstitucional produz danos. (a) inverte: o dano vem da aplicação da lei; (b) e (e) negam a responsabilidade; (c) não se limita a atos do Executivo.')
q('2102124', '6.1D', 'Correto. Em regra, atos jurisdicionais não geram indenização (soberania, independência, coisa julgada). Exceções: erro judiciário, prisão além do tempo (CF, art. 5º, LXXV) e dolo ou fraude do juiz (CPC, art. 143). MSZ critica essa jurisprudência (15.7).')
q('2270085', '6.1D', 'Gabarito A. Sem nexo entre a lei inconstitucional e o dano não há responsabilidade. Não importa se a lei é genérica, se o vício é material ou formal, nem quem a promulgou; a declaração cabe ao Judiciário (STF).')
q('3384910', '6.1D', 'Gabarito E (só o IV). I: a responsabilidade é objetiva, pelo risco administrativo. II: culpa concorrente atenua. III: é objetiva também perante não usuários. IV: CF, art. 5º, LXXV.')
q('2732306', '6.1D', 'Gabarito B (só o I). I: atos de multidão são fato de terceiro; o Estado só responde se houver omissão (MSZ 15.4). II: suicídio de detento pode gerar responsabilidade (Tema 592), salvo se o Estado provar que não podia evitá-lo. III: a mera declaração de inconstitucionalidade não basta; é preciso dano e nexo.')
q('1119035', '6.1D', 'Gabarito B: mudança de política econômica não gera indenização, salvo quando o Estado se comprometeu antes (planejamento específico, confiança legítima). (a) cabe pagamento administrativo; (c) nomeação tardia só gera indenização em arbitrariedade flagrante (Tema 671); (d) objetiva para usuários e não usuários; (e) a responsabilidade subsidiária por encargos trabalhistas exige culpa na fiscalização (Tema 246); não é automática.')
q('3075570', '6.1D', 'Obra pública pode gerar indenização, inclusive quando lícita, se causar dano anormal e específico (MSZ 15.3: "danos decorrentes de obra pública, ainda que licitamente realizada").',
  'Interesse público não é excludente. Ato lícito também gera responsabilidade.')

# ---------------- 6.2 — ato comissivo ----------------
q('3361434', '6.2', 'Correto. Ato comissivo: responsabilidade objetiva, risco administrativo; provar conduta, dano e nexo causal.')
q('3284213', '6.2', 'Correto. São duas regras no art. 37, § 6º: responsabilidade objetiva do Estado e subjetiva do agente (MSZ 15.3).')
q('3495323', '6.2', 'Na responsabilidade objetiva basta conduta, dano e nexo; dolo ou culpa do servidor só interessa ao regresso.')
q('3597427', '6.2', 'Responsabilidade objetiva não é presunção absoluta de culpa nem obrigação de reparar "todo" dano: há excludentes (culpa exclusiva da vítima, força maior), e a culpa simplesmente não é examinada.',
  'Objetiva ≠ culpa presumida. Na objetiva, a culpa é irrelevante. Presunção de culpa é a tese de MSZ e Celso Antônio para a omissão (15.5).')
q('2817066', '6.2', 'Agência reguladora é autarquia (direito público): responde objetivamente. O terceiro não precisa provar culpa de Helena; isso só importa para o regresso.')
q('3954390', '6.2', 'Gabarito D: objetiva, risco administrativo, regresso se houver dolo ou culpa do agente. As alternativas erradas trocam o risco (integral) ou dispensam dolo ou culpa no regresso.')
q('4146968', '6.2', 'Gabarito C: a responsabilidade do Estado não depende de punir o agente; basta o dano decorrer de atividade estatal com nexo causal. (a) concessionárias estão no § 6º; (b) e (e) o regresso exige dolo ou culpa (qualquer grau); (d) culpa concorrente atenua; não afasta.')
q('2208321', '6.2', 'Correto. STF, RE 1.209.429 (Tema 1055): é objetiva a responsabilidade do Estado por profissional de imprensa ferido por policiais em manifestação com tumulto. Exclui-se só por culpa exclusiva da vítima, se o jornalista descumprir advertência ostensiva sobre área de grave risco.')
q('3103035', '6.2', 'Correto. Destruir coisa alheia para remover perigo iminente é ato lícito (CC, art. 188, II), mas o dono não culpado tem direito à indenização (art. 929), e quem indenizou tem regresso contra o terceiro culpado pelo perigo (art. 930). É o exemplo de MSZ (15.3) de ato lícito que gera responsabilidade do Estado.',
  'Culpa de terceiro (Carlos) aqui não exclui a responsabilidade do Estado perante Joana. Serve só para o regresso. É exceção à regra de que fato de terceiro é excludente.')
q('3206684', '6.2', 'Correto. Ato lícito gera responsabilidade quando causa dano anormal e específico, rompendo a igualdade perante os encargos sociais (MSZ 15.1 e 15.3).',
  '"Excepcionalmente" foi aceito. Em regra, no direito privado, só o ilícito gera dever de indenizar; no direito administrativo, o lícito também pode.')
q('3661477', '6.2', 'Correto. O fundamento da indenização por ato lícito é a isonomia (igualdade de todos perante os encargos sociais, repartição dos encargos), não a legalidade, que foi respeitada.')
q('4041964', '6.2', 'Gabarito C. Viatura em serviço: responsabilidade objetiva do DF; culpa concorrente de Pedro atenua (CC, art. 945). (a) não exige dolo ou culpa; (b) regresso exige dolo ou culpa; (d) risco administrativo; (e) falta o nexo causal.')

# ---------------- 6.3 — omissão ----------------
q('4085749', '6.3', 'Gabarito A. Posição clássica (e de MSZ): na omissão, responsabilidade subjetiva, por culpa anônima ou falta do serviço (não funcionou, funcionou mal, funcionou tarde), sem identificar o agente. (b) risco integral não é a regra; (c) força maior também exclui na omissão; (d) a banca não aceitou a tese de que omissão e ação têm o mesmo regime.',
  'A banca aceita as duas correntes conforme o comando: "em regra/doutrina clássica" → subjetiva; "dever específico, STF" → objetiva. Leia o comando antes da resposta.')
q('4148366', '6.3', 'O Estado responde por omissão (culpa do serviço ou dever específico de agir).')
q('4173794', '6.3', 'Com dever jurídico específico de agir, como a custódia de detento, o STF aplica a responsabilidade objetiva (Tema 592, RE 841.526). Não é preciso provar culpa da Administração.')
q('4193511', '6.3', 'STF, RE 608.880 (Tema 362): não há responsabilidade objetiva por crime de foragido quando não demonstrado nexo causal direto entre o momento da fuga e o crime. O item afirmou responsabilidade "dias após a fuga", sem nexo direto.',
  'O critério é o nexo direto (teoria do dano direto e imediato), não um número de dias. Fuga + crime imediato, durante a evasão = responsabilidade.')
q('3661480', '6.3', 'Correto. Síntese do que a banca espera: omissão em regra subjetiva (culpa do serviço); objetiva quando violado dever jurídico específico de agir, como a morte de detento sob custódia (Tema 592).')
q('2838966', '6.3', 'Gabarito A. Para o STF, omissão ligada a dever específico de agir gera responsabilidade objetiva, pelo risco administrativo (não pelo integral).')
q('3103038', '6.3', 'Atos lícitos geram responsabilidade na conduta comissiva; na omissão, ela tem de ser ilícita, isto é, descumprir dever de agir (MSZ 15.5: "a omissão tem que ser ilícita").',
  'Comissivo: lícito ou ilícito. Omissivo: só ilícito.')
q('3103043', '6.3', 'Não há consenso: MSZ, Celso Antônio, Cretella e Cahali defendem a subjetiva; MSZ reconhece que a maioria parece pender para a objetiva, e o STF tem acórdãos nos dois sentidos (15.5).',
  '"Posição consensual", "pacífico", "unânime" em tema controvertido = ERRADO.')
q('3202351', '6.3', 'Correto. Sem dever jurídico de agir não há omissão relevante. MSZ (15.5): é preciso o dever de agir e a possibilidade de agir (reserva do possível, razoabilidade).')
q('2367634', '6.3', 'Gabarito B. Antônio estava sob custódia do Estado (réu internado em hospital estadual): há dever específico de proteção, e a responsabilidade é objetiva. Estar acordado, acompanhado ou algemado não exclui; o homicídio por terceiro não rompe o nexo quando o Estado devia impedir.')
q('2367847', '6.3', 'O Estado responde por omissão.')
q('2722860', '6.3', 'Gabarito B. Para a banca, na omissão do delegatário a responsabilidade é subjetiva: provar fato administrativo (a omissão), dano, nexo e culpa (do serviço).')
q('2213196', '6.3', 'Via mal conservada é omissão genérica: exige culpa do serviço (o serviço não funcionou ou funcionou mal), além do dano e do nexo. Não bastam dano e nexo.',
  'Omissão genérica (buraco na rua, falta de policiamento comum, enchente) → subjetiva. Omissão específica (preso, aluno, paciente internado) → objetiva.')
q('3972221', '6.3', 'Dois erros: a CF não adota o risco integral; e a conduta omissiva do médico do SUS que deixa de atender não é caso de risco integral.')
q('2459852', '6.3', 'A responsabilidade pode decorrer de omissão e de ato de agente que não seja servidor em sentido estrito (particular em colaboração, agente político).',
  '"Sempre" + "ato comissivo" + "servidor público": três restrições que a CF não faz.')
q('3441737', '6.3', 'O STF aplica o risco administrativo também à omissão específica (Tema 592: morte de detento). Não se limita às condutas comissivas.')
q('2400419', '6.3', 'Anulada. Responsabilidade objetiva "em atos comissivos e omissivos, independentemente da licitude" entra na controvérsia da omissão (que, segundo MSZ, tem de ser ilícita). Sem posição pacífica, a banca anulou.')
q('2473275', '6.3', 'Gabarito D (III, IV e V). I: risco integral não é a regra. II: culpa exclusiva da vítima exclui. III: Tema 592. IV: Tema 362. V: Tema 940.',
  'Questão-modelo: três teses do STF numa mesma lista. Decore os números 592, 362 e 940.')
q('2450420', '6.3', 'Gabarito B: erro médico ligado a omissão (falta de atendimento) foi tratado como responsabilidade subjetiva. (a) venda clandestina de fogos sem conhecimento do poder público: não há responsabilidade, por falta de dever específico violado (Tema 366); (c) foragido: depende de nexo direto (Tema 362); (d) a prestadora responde diretamente; (e) concurso cancelado: o Estado responde subsidiariamente (Tema 512).')
q('1711621', '6.3', 'Gabarito B: basta nexo entre a ação estatal e o dano anormal e específico; o ato não precisa ser ilícito. (a) "sempre subjetiva" contraria o Tema 592; (c) não há solidariedade; o poder público responde subsidiariamente; (d) a reserva do possível não é "amplamente aceita" contra políticas previstas em lei; (e) suicídio de preso pode gerar responsabilidade.')
q('1439169', '6.3', 'A conclusão (Alípio deve ser indenizado, pelo dever de guarda do veículo retido) pode estar certa, mas o fundamento está errado: o furto por terceiro é dano por omissão no dever de guarda, não conduta comissiva. Além disso, quem responde é a concessionária, não "o Estado".',
  'Item com conclusão aceitável e justificativa errada = ERRADO. O Cebraspe corrige a frase inteira.')

# ---------------- 6.4 — requisitos ----------------
q('3815432', '6.4', 'Gabarito B. O Brasil adota a teoria do dano direto e imediato (interrupção do nexo causal; CC, art. 403; STF, RE 130.764). (a) há responsabilidade por omissão; (c) não existe "culpa integral"; (d) concorrente atenua; (e) a culpa da vítima é examinada, porque exclui ou atenua.')
q('4148379', '6.4', 'A teoria adotada é a do dano direto e imediato. Equivalência dos antecedentes (conditio sine qua non) é do direito penal; causalidade adequada é defendida por parte da doutrina civilista.',
  'Duas teorias corretas "em outro ramo" juntas no mesmo item. Em responsabilidade do Estado, a resposta do Cebraspe é dano direto e imediato.')
q('3495314', '6.4', 'Correto. Teoria do dano direto e imediato, mencionada em acórdão do STF citado por MSZ (15.5).')
q('2921881', '6.4', 'Anulada. Houve divergência: a teoria majoritária na jurisprudência é a do dano direto e imediato, mas a doutrina também invoca a causalidade adequada, e algumas alternativas se sobrepõem (causa mais eficiente). Em outras provas a banca confirmou "dano direto e imediato".')
q('2933925', '6.4', 'Correto. Sem nexo causal não há responsabilidade, objetiva ou subjetiva. As excludentes atacam justamente o nexo.')
q('2332184', '6.4', 'Gabarito E. (a) Tema 592 exige inobservância do dever de proteção: não é "sempre", o Estado pode provar que não podia evitar; (b) dano moral é indenizável sem reflexo patrimonial; (c) culpa da vítima só exclui se exclusiva; de terceiro, conforme o caso; (d) o nexo é exigido em toda responsabilidade; (e) a responsabilidade não é absoluta: admite excludentes.')
q('2414396', '6.4', 'Gabarito A. Nem todo dano ligado ao serviço gera responsabilidade: é preciso nexo e ausência de excludentes; para ato lícito, dano anormal e específico. (b) o elemento subjetivo é relevante para o regresso e para a culpa da vítima; (c) dano + elemento subjetivo sem nexo não bastam; (d) o dever de diligência pode decorrer de normas gerais, não só de norma específica para a situação.')
q('2013876', '6.4', 'Gabarito D. Para a responsabilidade objetiva é preciso confirmar o nexo entre o fato administrativo e o dano. (a) a ilicitude não é exigida; (b) improbidade não é crime; (c) o prazo quinquenal alcança as privadas prestadoras; (e) a ação de regresso por ilícito civil prescreve (STF, Tema 666); só o ressarcimento por improbidade dolosa é imprescritível (Tema 897).')
q('3883081', '6.4', 'Gabarito A. Prejuízo anormal e específico por conduta de agente obriga a indenizar. (b) danos por conduta lícita podem ser materiais e morais; (c) para o ato ilícito não se exige dano anormal e específico; esse filtro é do ato lícito; (d) a licitude é irrelevante; (e) não há solidariedade automática.',
  'Dano anormal e específico é exigência para o ato lícito. Para o ilícito basta o dano.')
q('1942600', '6.4', 'Gabarito D. Dano antijurídico, para MSZ, é o ilícito ou o lícito que cause dano anormal e específico. (a) e (c) trocam as definições: anormal = supera os inconvenientes normais da vida em sociedade; específico = atinge pessoas determinadas; (b) para MSZ, caso fortuito não exclui; (e) concausas não afastam a culpa concorrente.',
  'Troca de definições anormal/específico é pegadinha clássica. Anormal = intensidade. Específico = destinatário.')
q('2015210', '6.4', 'Gabarito D. A privada prestadora responde por ato comissivo ou omissivo de seu agente na prestação do serviço. (a) descreve a extracontratual; (b) nesses casos é objetiva, por risco integral; (c) não se prova culpa ou dolo na objetiva; (e) a culpa anônima dispensa individualizar o agente.')
q('4252944', '6.4', 'Correto. A objetiva dispensa culpa, mas não dispensa nexo causal.')
q('3284212', '6.4', 'O perito atendia em consultório particular, fora da função pública. O Estado só responde se o agente age "nessa qualidade" (MSZ 15.3, requisito 5).',
  'Ter a qualidade de agente não basta. É preciso estar no exercício da função (ou a pretexto de exercê-la).')
q('2498012', '6.4', 'Exorbitar dos poderes não gera responsabilidade exclusiva do agente: se agiu nessa qualidade, o Estado responde objetivamente e cobra em regresso. Abuso de poder no exercício da função continua imputável ao Estado.')
q('1939544', '6.4', 'Gabarito B. O delegado usou a carteira para lazer pessoal: não agia no exercício da função, e o art. 37, § 6º, não se aplica. Ele responde pessoalmente. (e) a "teoria da aparência" não foi aceita porque a finalidade era privada.',
  'Compare com o policial que, de folga, usa a arma da corporação: aí o STF costuma reconhecer a responsabilidade do Estado. O que decide é o vínculo com a função.')
q('3103046', '6.4', 'É requisito que o agente tenha agido nessa qualidade (art. 37, § 6º).')
q('1968181', '6.4', 'As instâncias civil, penal e administrativa são independentes. A responsabilidade civil do Estado não depende de processo penal ou disciplinar.')

# ---------------- 6.5 — excludentes e atenuantes ----------------
q('3883084', '6.5', 'Gabarito B. Força maior + omissão específica do serviço = responsabilidade por culpa do serviço (MSZ 15.4: a enchente que limpeza de bueiros teria evitado). (a) concorrência da vítima atenua; (c) fato exclusivo de terceiro exclui; (d) culpa exclusiva da vítima rompe o nexo; (e) a excludente não depende de culpa do agente.')
q('3972222', '6.5', 'Correto. "Compensação de culpas": havendo participação da vítima, a indenização é reduzida (CC, art. 945).',
  'A expressão "compensação de culpas" é usada pela banca como sinônimo de culpa concorrente atenuante.')
q('4145982', '6.5', 'Correto. Culpa concorrente atenua (MSZ 15.4; CC, art. 945).')
q('4148373', '6.5', 'Correto. Exclusiva → exclui; concorrente → atenua.')
q('3342053', '6.5', 'O erro está na culpa concorrente, que só atenua. Quanto a caso fortuito e força maior, a banca costuma tratá-los juntos como excludentes.')
q('3373952', '6.5', 'Correto. Culpa exclusiva da vítima: não há nexo entre a atuação estatal e o dano.')
q('3400492', '6.5', 'Gabarito E. (a) o ônus de provar a excludente é do Estado (STF, Tema 1237, para operações policiais); (b) culpa concorrente atenua, não rompe o nexo; (c) adota-se o dano direto e imediato; (d) diz que não existe excludente, o que é falso; (e) correta.',
  'Na alternativa D, "inexistindo causa excludente" pode ser lida como condição ou como afirmação. Em múltipla escolha, prefira a alternativa sem ambiguidade (a E).')
q('3441735', '6.5', 'Correto para a banca: caso fortuito e força maior rompem o nexo.',
  'MSZ (15.4) diverge: para ela só a força maior (evento da natureza) exclui; caso fortuito (ato humano ou falha da Administração, como o rompimento de adutora) não exclui. Em item genérico, o Cebraspe tem dado CERTO para "caso fortuito e força maior excluem".')
q('3495326', '6.5', 'Correto. Culpa exclusiva da vítima rompe o nexo.')
q('3683327', '6.5', 'Gabarito D. (a) o comportamento da vítima sempre se examina; (b) a força maior não exclui "automaticamente": se aliada à omissão, há responsabilidade; (c) sem relação com a atividade estatal não há responsabilidade; (e) a omissão não é "sempre" objetiva.')
q('2775369', '6.5', 'Correto. Risco administrativo; culpa concorrente da vítima reduz a indenização.')
q('2841458', '6.5', 'Correto para a banca: força maior e caso fortuito excluem a responsabilidade (rompem o nexo).',
  'Mesma divergência com MSZ. Saiba as duas posições e use o comando da questão: "segundo Maria Sylvia" → caso fortuito não exclui.')
q('3039372', '6.5', 'A árvore estava em péssimo estado de conservação: houve omissão do município. Força maior aliada à omissão do Poder Público não exclui a responsabilidade (MSZ 15.4).',
  'Sempre que o enunciado der um "detalhe" de má conservação, falta de manutenção ou aviso ignorado, a força maior deixa de excluir.')
q('3079248', '6.5', 'Correto. Força maior não exclui se o Estado contribuiu por omissão (bueiros entupidos, árvore podre).')
q('3103051', '6.5', 'Força maior é evento estranho à vontade das partes; se o evento vem de ato do poder público, não é excludente. MSZ: o que decorre de falha da Administração é caso fortuito, que não exclui.')
q('3202348', '6.5', 'Correto. Força maior é excludente (rompe o nexo).')
q('3206682', '6.5', 'Culpa concorrente atenua; não exclui.')
q('2304801', '6.5', 'Correto. Se o fato era evitável pelo Estado (omissão), não há força maior excludente.')
q('2690016', '6.5', 'Evento da natureza só exclui se o Estado não concorreu por omissão. A afirmação absoluta ("afasta a possibilidade") está errada.')
q('2722840', '6.5', 'Gabarito D. (a) só o dano causado na qualidade de agente; (b) ato normativo ilegal (regulamento) dispensa prévia declaração, e lei de efeitos concretos gera responsabilidade mesmo constitucional (MSZ 15.6); (c) atos lícitos geram responsabilidade; (d) correta: força maior + omissão; (e) fato de terceiro não obsta se houver omissão estatal.')
q('1937221', '6.5', 'Culpa concorrente só atenua.')
q('3078641', '6.5', 'O risco administrativo exige nexo e admite a culpa exclusiva da vítima como excludente.',
  '"Independe do nexo" está sempre errado. Nem o risco integral dispensa o vínculo com a atividade.')
q('3994522', '6.5', 'Gabarito A. Culpa concorrente mitiga a responsabilidade, que continua objetiva e é dividida com a vítima. (d) erra ao dizer que vira subjetiva.')
q('4085745', '6.5', 'Gabarito A. Conduta comissiva: objetiva; velocidade excessiva da vítima é culpa concorrente, que reduz proporcionalmente a indenização. (b) a contribuição não rompe "integralmente" o nexo; (c) não é subjetiva; (d) agente que extrapola atribuições no exercício da função também obriga o Estado.')
q('1796674', '6.5', 'Correto. Até no disparo de arma por policial, a culpa exclusiva da vítima exclui a responsabilidade, pelo risco administrativo.')
q('1989644', '6.5', 'Anulada. Pela MSZ (15.4), caso fortuito (falha humana ou do serviço) não exclui: alternativa A certa. Culpa exclusiva da vítima exclui: alternativa C também certa. E a força maior não é a única excludente, o que derruba a B. Duas alternativas corretas.',
  'A fiscalização do poder concedente não exclui nem atenua a responsabilidade da concessionária (Lei 8.987/95, art. 25; Lei 14.133/21, art. 120).')

# ---------------- Câmara dos Deputados 2012 (Cebraspe) ----------------
q('cd12-74', '6.1A', 'Gabarito oficial definitivo: CERTO, que contraria a doutrina. Para MSZ (15.3) e para a própria banca em 2022 (FUB: "a partir da CF/1946", CERTO), a responsabilidade objetiva foi adotada em 1946. A CF/88 só a estendeu às pessoas privadas prestadoras de serviço público.',
  'Em 2027, a resposta segura é 1946. Se o item disser "somente a partir da CF/88", tenda a ERRADO, mas saiba que em 2012 esta banca, nesta mesma casa, deu CERTO.')
q('cd12-75', '6.1B', 'Correto. Art. 37, § 6º: as pessoas privadas prestadoras de serviço público respondem objetivamente pelos danos que seus agentes, nessa qualidade, causarem a terceiros.')
q('cd12-76', '6.3', 'Gabarito oficial em 2012: ERRADO. O item falava em negligência (culpa), e a banca seguia a tese da culpa do serviço para a omissão. Em 2016 o STF fixou o Tema 592 (o Estado responde objetivamente pela morte de detento quando descumpre o dever específico de proteção). Hoje, o mesmo item tende a ser CERTO.',
  'A banca muda com o STF. Estude pelos temas de repercussão geral, não por gabaritos antigos.')
