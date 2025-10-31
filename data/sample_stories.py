"""
Dataset de Histórias para Treinamento
Tech Challenge Fase 4 - FIAP

Este dataset contém histórias de exemplo em português para treinar
o modelo de geração criativa. Durante os testes, descobri que ter
exemplos diversos ajuda o modelo a aprender diferentes estilos narrativos.
"""

STORIES_DATASET = [
    # Ficção Científica
    {
        "id": 1,
        "genero": "Ficção Científica",
        "personagens": ["Ana: cientista corajosa", "ARIA: inteligência artificial"],
        "cenario": "Estação espacial em Marte, ano 2089",
        "tom": "Aventuroso",
        "historia": """Ana olhou pela janela transparente do laboratório. Marte estendia-se vermelho e silencioso abaixo dela, como sempre estivera nos últimos três anos. Mas hoje era diferente.

'ARIA, status dos experimentos do Setor 7', ela disse, tentando manter a voz calma.

A voz suave da inteligência artificial respondeu quase instantaneamente: 'Anomalia detectada. Sinais biológicos não catalogados. Padrões inconsistentes com qualquer forma de vida conhecida.'

O coração de Ana acelerou. Três anos coletando amostras, três anos de resultados negativos, e agora... agora tudo mudaria. Ela correu até o microscópio eletrônico. As imagens na tela mostravam estruturas que desafiavam toda a biologia terrestre.

'ARIA, isso é... vida marciana?'

Houve uma pausa. Imperceptível para a maioria, mas Ana conhecia cada nuance da IA. 'Análise em andamento. Mas Ana... há algo mais. Os organismos estão tentando se comunicar. Estão enviando padrões matemáticos.'

Ana sentou-se lentamente. A humanidade procurara por décadas. E agora, num laboratório solitário em Marte, com apenas uma IA como companhia, ela fizera a descoberta do século. Mas a pergunta que a assombrava era: será que eles queriam ser encontrados?"""
    },
    {
        "id": 2,
        "genero": "Ficção Científica",
        "personagens": ["Marcus: piloto de caça", "Zara: engenheira de sistemas"],
        "cenario": "Nave colonial, viagem interestelar",
        "tom": "Épico",
        "historia": """O alarme soou pela décima vez em uma hora. Marcus apertou os controles com força, desviando de mais um campo de asteroides. Atrás dele, no compartimento de engenharia, Zara trabalhava freneticamente nos reparos.

'Quanto tempo mais consegues me dar?' ele gritou pelo comunicador.

'Dois minutos! Talvez três se tivermos sorte!' A voz dela era tensa mas focada.

A nave colonial Esperança carregava mil e duzentas almas em criogenia. Famílias inteiras apostando tudo num novo começo em Proxima Centauri b. Mas o sistema de navegação tinha falhado no pior momento possível - no meio do Cinturão de Órion.

Marcus virou a nave bruscamente, sentindo os motores gemer sob o estresse. 'Não agora', ele murmurou. 'Não depois de vir tão longe.'

'Marcus! Consegui!' Zara irrompeu pelo comunicador. 'Tenho energia suficiente para um salto curto. Mas tem que ser agora!'

Ele nem hesitou. 'Coordenadas travadas. Saltando em três... dois...'

O espaço dobrou-se sobre si mesmo. Por um momento infinito e instantâneo, Marcus viu todas as possibilidades do universo. Depois, escuridão.

Quando despertou, a primeira coisa que viu foi o rosto aliviado de Zara. Pela janela, um planeta azul e verde girava serenamente. Proxima b. Tinham conseguido.

'Bem-vindo ao novo lar', ela sorriu."""
    },
    
    # Terror
    {
        "id": 3,
        "genero": "Terror",
        "personagens": ["Lucas: estudante de arquitetura", "Sombra: presença desconhecida"],
        "cenario": "Casa abandonada dos Almeida, noite de tempestade",
        "tom": "Sombrio",
        "historia": """O relâmpago iluminou brevemente a sala empoeirada. Lucas engoliu em seco, o celular tremendo em sua mão. Não deveria estar ali. Ninguém entrava na velha casa dos Almeida há décadas, desde que a família inteira... 'Não pense nisso', ele murmurou para si mesmo.

O desafio parecia tão simples algumas horas atrás: passar a noite na casa mal-assombrada e gravar tudo. Fácil. Rápido. Viral. Que idiota tinha sido.

Um som. Passos no andar de cima. Lentos. Deliberados. Indo em sua direção.

'É só a casa velha se acomodando', Lucas tentou se convencer. Mas casas velhas não respiram. E ele podia ouvir respiração. Pesada. Úmida. Logo atrás de onde estava.

Virou-se lentamente. Nada ali. Só sombras dançando com a luz vacilante da lanterna. Mas então viu. No canto, onde a escuridão era mais profunda, algo se movia. Algo que tinha formato mas não forma. Algo que o observava com olhos que não existiam.

Lucas correu. Atravessou a sala, o corredor, buscou desesperadamente a porta da frente. Trancada. Impossível. Ele a tinha deixado aberta. Tinha certeza.

Os passos desciam a escada agora. Um de cada vez. Cada um mais próximo. Cada um mais real.

'Por favor', ele chorou. 'Por favor, eu só quero ir embora.'

A respiração estava em seu pescoço agora. Gelada. Podre. Uma voz que vinha de lugar nenhum sussurrou em seu ouvido: 'Mas você pediu para ficar. Para sempre.'

O celular de Lucas foi encontrado três dias depois. Ainda gravando. Mas tudo que mostrava eram 47 horas de uma sala vazia e escura. E no fim, bem no fim, o som de alguém gritando."""
    },
    {
        "id": 4,
        "genero": "Terror",
        "personagens": ["Dr. Helena Carvalho: psiquiatra"],
        "cenario": "Instituto Psiquiátrico São Benedito, ala abandonada",
        "tom": "Sombrio",
        "historia": """A Dra. Helena Carvalho tinha tratado centenas de pacientes em seus vinte anos de carreira. Tinha ouvido todo tipo de história, todo tipo de delírio. Mas o caso de Isabella era diferente.

'Eles vêm à noite, doutora', Isabella repetia na última sessão. 'Todos os que morreram aqui. Eles querem que eu conte a verdade.'

Helena tinha arquivado o caso como psicose grave. Até encontrar os arquivos antigos do instituto. Os experimentos. As mortes não registradas. Os pacientes que simplesmente 'desapareceram' na década de 60.

Agora estava ali, sozinha na ala abandonada, com uma lanterna e as pastas antigas. Precisava saber a verdade. Por Isabella. Por todos eles.

A luz piscou. Uma vez. Duas. Depois apagou completamente.

No silêncio que se seguiu, Helena ouviu. Sussurros. Dezenas deles. Vozes sobrepostas, todas falando ao mesmo tempo, todas dizendo a mesma coisa: 'Finalmente. Finalmente alguém veio.'

Mãos geladas tocaram seus ombros. Seu rosto. Seu coração. Não com malícia, mas com desespero. Com súplica.

'Conte nossa história', as vozes imploravam. 'Não deixe que sejamos esquecidos.'

Helena foi encontrada na manhã seguinte, inconsciente mas viva, abraçada aos arquivos. Quando acordou, não conseguia parar de escrever. Nomes. Datas. Crimes. Tudo que os mortos tinham mostrado a ela.

E à noite, quando fecha os olhos, ainda pode ouvi-los sussurrando: 'Obrigado.'"""
    },
    
    # Romance
    {
        "id": 5,
        "genero": "Romance",
        "personagens": ["Júlia: professora de literatura", "Rafael: músico de rua"],
        "cenario": "Café parisiense, outono",
        "tom": "Romântico",
        "historia": """As folhas douradas dançavam no vento enquanto Júlia observava pela vidraça do café Au Petit Suisse. Cinco anos desde que havia deixado São Paulo. Cinco anos tentando esquecer. Tentando reconstruir.

Paris no outono era exatamente como nos filmes - romântico, melancólico, perfeito para quem queria se perder e se encontrar ao mesmo tempo. Ela sorvia o café au lait lentamente, saboreando cada momento de paz.

A campainha da porta tocou. Ela nem se virou. Até ouvir aquela voz. Impossível, mas inconfundível.

'Ainda toma café com leite e duas colheres de açúcar?'

O tempo parou. Júlia virou-se lentamente. Rafael estava ali, mais magro, com barba, segurando um violão gasto. Mas eram os mesmos olhos. Os mesmos olhos que a fizeram atravessar oceanos para fugir.

'O que... como você...' Palavras falharam.

Ele sorriu, aquele sorriso torto que ela tanto amara. 'Vim tocar nas ruas de Paris. Ironia, não? Você fugiu para cá e eu te persegui sem saber.'

'Você não está me perseguindo', ela disse, mais áspera do que pretendia.

'Não. Mas talvez... talvez o destino esteja.' Ele puxou uma cadeira sem pedir licença. 'Júlia, eu estraguei tudo há cinco anos. Eu sei. Mas todo dia, toda música que toco é pra você. E agora...'

'Agora?'

'Agora estamos aqui. No mesmo café. Na mesma cidade. Talvez seja a chance que eu não mereço mas que você talvez precise.'

Júlia olhou para a xícara. Para a janela. Para qualquer lugar menos para aqueles olhos. 'Uma xícara de café', ela finalmente disse. 'Você pode ficar por uma xícara de café. Nada mais.'

Mas quando ele sorriu, ela soube. Uma xícara se tornaria duas. Duas se tornariam jantar. E Paris, aquela cidade de recomeços, talvez lhes desse a segunda chance que ambos secretamente desejavam."""
    },
    {
        "id": 6,
        "genero": "Romance",
        "personagens": ["Marina: médica", "Diego: fotógrafo de guerra"],
        "cenario": "Hospital de campanha, zona de conflito",
        "tom": "Épico",
        "historia": """Marina costurava o décimo ferimento da noite quando o ouviu entrar na tenda. Não precisava olhar para saber quem era. Cinco semanas no mesmo hospital de campanha te ensina a reconhecer as pessoas pelo som dos passos.

'Trouxe mais três', Diego disse, a voz rouca de cansaço. Através da abertura da tenda, ela via os flashes ainda no horizonte. A guerra não dormia.

'Coloca ali', ela indicou com a cabeça, mãos ocupadas demais para apontar.

Ele obedeceu, depois ficou ali, parado, observando-a trabalhar. Era algo que fazia frequentemente. Marina tinha parado de se incomodar depois da segunda semana.

'Por que você nunca sai?' ela perguntou, terminando os pontos. 'Você tira as fotos, poderia ir embora.'

'Por que você fica?' ele respondeu com outra pergunta.

Ela finalmente olhou para ele. Magro, sujo, com aqueles olhos cinzentos que tinham visto horrores demais. 'Porque alguém precisa.'

'Exatamente.'

Foi tudo que disseram naquela noite. Mas duas noites depois, quando uma bomba caiu perigosamente perto, foi Diego quem a cobriu com o próprio corpo. E três noites depois disso, quando ele voltou ferido, foi para as mãos dela que ele confiou sua vida.

'Não morra aqui', Marina sussurrou, costurando o ferimento profundo em seu ombro. 'Não depois de ter me mostrado porque vale a pena ficar.'

Ele sorriu, mesmo na dor. 'Promessa. Mas só se você prometer também.'

'Prometo.'

Seis meses depois, quando o conflito finalmente cessou, eles caminharam juntos para fora do campo. Para um mundo que não conheciam mais. Mas pelo menos tinham um ao outro. E às vezes, nas guerras da vida, isso é tudo que importa."""
    },
    
    # Aventura
    {
        "id": 7,
        "genero": "Aventura",
        "personagens": ["Capitã Elena Rodrigues: arqueóloga", "Tom: guia local"],
        "cenario": "Floresta amazônica, cidade perdida",
        "tom": "Aventuroso",
        "historia": """O mapa estava errado. Ou estava certo demais. Elena não tinha certeza qual era pior.

'Tom!' ela chamou o guia. 'Quanto tempo ainda?'

'Duas horas. Talvez três.' Ele cortava a vegetação densa com o facão, abrindo caminho. 'Se sua teoria estiver certa.'

Se. A palavra que definira os últimos cinco anos de sua vida. Se a cidade perdida de Akahim realmente existia. Se o mapa do século XVI não era apenas uma fantasia. Se ela não estava desperdiçando sua carreira inteira perseguindo fantasmas.

O sol estava começando a se pôr quando viram. Entre as árvores, pedras que não eram pedras. Estruturas que não eram naturais. Pirâmides cobertas de séculos de vegetação, esperando pacientemente para serem redescobertas.

'Meus Deus', Elena sussurrou, caindo de joelhos. 'É real. É tudo real.'

Tom olhava ao redor com os olhos arregalados. 'Minha avó contava histórias. Sobre a cidade onde o sol nasceu. Eu pensava que era apenas lenda.'

Mas lendas não têm paredes de pedra decoradas com ouro. Lendas não têm inscrições em línguas mortas há mil anos. Elena correu de estrutura em estrutura, fotografando, medindo, catalogando. Cada descoberta era mais impressionante que a anterior.

Até encontrarem a câmara central. A porta era baixa, forçando-os a rastejar. Mas o que havia dentro roubou todo o ar de seus pulmões.

Uma biblioteca. Não de livros, mas de placas de metal gravadas. Milhares delas. Organizadas, preservadas, esperando. O conhecimento completo de uma civilização inteira.

'Isso vai mudar tudo', Tom murmurou.

Elena não conseguia falar. Tinha procurado por uma cidade. Tinha encontrado uma janela para um mundo perdido. E agora, agora tinha a responsabilidade de trazê-lo de volta à luz."""
    },
    {
        "id": 8,
        "genero": "Aventura",
        "personagens": ["Jake: surfista profissional", "Mika: biólogo marinho"],
        "cenario": "Ilha remota no Pacífico, recife inexplorado",
        "tom": "Aventuroso",
        "historia": """A onda perfeita não existe. Mas Jake estava começando a acreditar que estava errado.

'Você tem certeza disso?' Mika perguntou, verificando o equipamento de mergulho pela terceira vez.

'Olha o mapa. Olha as leituras do sonar.' Jake apontou para a tela. 'Há algo grande ali embaixo. Algo que cria ondas perfeitas.'

Eles tinham navegado por três dias até aquela ilha sem nome. Um pontinho no meio do Pacífico que nem aparecia na maioria dos mapas. Mas os dados não mentiam. Havia algo extraordinário nas águas ao redor.

O mergulho começou bem. Águas cristalinas, visibilidade perfeita. Mas conforme desciam, Mika começou a perceber. As formações de coral eram... organizadas. Simétricas. Impossíveis.

'Jake', ele falou no comunicador subaquático. 'Isso não é natural.'

'O quê?'

'O recife. Não é um recife. É uma estrutura. Alguém construiu isso.'

Chegaram ao fundo. E ali, preservado pela água e pelo tempo, estava um complexo inteiro. Templos. Casas. Praças. Uma cidade subaquática que não deveria existir.

'Quantos anos isso tem?' Jake sussurrou, reverente.

Mika examinava as pedras. 'Milhares. Talvez mais de dez mil. Isso é anterior a qualquer civilização conhecida.'

Mas não tinham muito tempo para maravilhas. A corrente estava mudando. As ondas acima ficando maiores. Perigosas. Precisavam subir.

'Voltamos', Mika decidiu.

'Voltamos', Jake concordou. Mas olhou para trás uma última vez. A cidade os observava com janelas vazias, guardando seus segredos por mais alguns séculos.

Na superfície, Jake surfou a maior onda de sua vida. Perfeita. Poderosa. Formada pelas ruínas de um mundo esquecido. E sorriu, porque agora sabia. A onda perfeita existe. Você só precisa mergulhar fundo o suficiente para encontrá-la."""
    },
    
    # Fantasia
    {
        "id": 9,
        "genero": "Fantasia",
        "personagens": ["Lyra: última feiticeira", "Corvus: corvo falante"],
        "cenario": "Reino de Aethermoor, após a Grande Purificação",
        "tom": "Épico",
        "historia": """A magia estava morrendo. Lyra sentia isso em cada feitiço que conjurava, cada encantamento que tentava manter. O mundo não queria mais magia. Preferia máquinas, lógica, ciência. E assim, lentamente, a magia definhava.

'Quanto tempo mais?' Corvus perguntou, empoleirado em seu ombro. O velho corvo era o último dos familiares, tão condenado quanto ela.

'Dias. Talvez semanas.' Lyra olhou para o grimório aberto à sua frente. As palavras estavam desaparecendo das páginas. Como se nunca tivessem existido.

'Então é isso? Depois de mil anos de tradição, simplesmente... acabou?'

Ela não respondeu. O que poderia dizer? Que tinha falhado? Que era a última de sua linhagem e não conseguira salvar nada?

Um estrondo na porta. Soldados. Vinham para queimar os últimos livros, prender a última feiticeira. O Reino de Aethermoor não tolerava mais 'superstições'.

'Vá', ela disse a Corvus. 'Voe para longe. Seja livre.'

'E você?'

Lyra sorriu tristemente. 'Eu faço o que feiticeiras sempre fizeram. Protejo o conhecimento.'

Começou o feitiço. Seu último. Seu mais poderoso. As palavras fluíam, antigas e poderosas, drenando toda sua força vital. O grimório brilhou, depois começou a se dissolver em luz pura.

'Não desapareço', ela murmurou. 'Apenas mudo. Me torno parte do mundo. Parte das histórias. E quando o mundo precisar de magia novamente, quando as crianças sonharem com feitiços e dragões, estarei ali. Esperando.'

A porta se abriu. Os soldados entraram. Mas só encontraram um corvo velho, uma pilha de cinzas, e a estranha sensação de que algo importante tinha acabado de mudar.

E nas noites seguintes, crianças por todo Aethermoor começaram a sonhar. Sonhos de magia. Sonhos de possibilidades. Sonhos de uma feiticeira que esperava, paciente como o tempo, para ser lembrada de novo."""
    },
    {
        "id": 10,
        "genero": "Fantasia",
        "personagens": ["Kael: ferreiro", "Lumina: espírito do fogo"],
        "cenario": "Forja nas Montanhas do Crepúsculo",
        "tom": "Aventuroso",
        "historia": """A espada quebrou pela quarta vez. Kael a atirou na pilha crescente de falhas e praguejou. Três meses tentando reforjar a lâmina lendária de Dawnbringer. Três meses falhando.

'Você está usando o metal errado.'

Ele girou. Ninguém deveria estar ali. Sua forja ficava no topo das Montanhas do Crepúsculo, dias de viagem da cidade mais próxima.

Mas ela estava ali mesmo assim. Uma mulher feita de chamas vivas, olhos como brasas, sorrindo como se soubesse um segredo.

'Lumina', ele sussurrou o nome antes mesmo de pensar. Espíritos do fogo eram lendas. Não podiam ser reais.

'Tão real quanto seu desespero, ferreiro.' Ela flutuou até a bigorna. 'Esta lâmina foi forjada com fogo comum. Precisa de algo mais.'

'O quê?'

'Meu fogo. Mas isso tem um preço.'

Kael sabia de histórias sobre espíritos. Sobre barganhas. Sobre preços que custavam mais do que ouro. Mas olhou para os fragmentos da espada - a última esperança de seu reino contra a escuridão que se aproximava - e sabia que não tinha escolha.

'Qual preço?'

'Sua solidão. Deixe-me ser seu aprendiz. Ensine-me sobre o mundo mortal, e eu empresto meu fogo.'

Era... inesperado. 'Só isso?'

'Solidão é a moeda mais valiosa que existe, ferreiro. E você nadou nela por anos.'

Ele não podia discutir. Então estendeu a mão. Ela a tocou. E chamas dançaram entre os dedos de ambos.

A reforja levou sete dias e sete noites. Kael trabalhava, e Lumina mantinha as chamas mais quentes que qualquer forja mortal. Conversavam. Riam. Compartilhavam histórias.

E quando a espada finalmente emergiu - perfeita, reluzente, imortal - Kael percebeu algo. O preço que ela pedira não fora pagamento. Fora cura.

'Obrigado', ele disse.

Lumina sorriu. 'É para isso que servem os aprendizes, mestre Kael. Para fazer você lembrar que não está sozinho.'"""
    },
    
    # Mistério
    {
        "id": 11,
        "genero": "Mistério",
        "personagens": ["Detetive Carla Mendes: investigadora", "Vítor: jornalista investigativo"],
        "cenario": "Museu Nacional, Rio de Janeiro",
        "tom": "Aventuroso",
        "historia": """O quadro estava ali ontem. Carla tinha certeza. Tinha passado por aquela sala pelo menos cinco vezes durante a vistoria de segurança. A 'Dama de Vermelho', obra-prima do século XIX, vale estimado em 50 milhões.

Agora, em seu lugar, havia apenas uma moldura vazia e um bilhete: 'Obrigado pela hospitalidade. Ela merecida um lar melhor.'

'Impossibilidade técnica', Vítor murmurou, analisando as câmeras de segurança com ela. 'Todas as filmagens mostram o quadro ainda no lugar. Até o último segundo antes de descobrirem o roubo.'

'Impossível não existe. Apenas muito improvável.' Carla examinou a moldura. Sem arranhões. Sem sinais de ferramentas. Como se o quadro simplesmente tivesse... desaparecido.

'Tem algo que preciso te mostrar', Vítor disse, hesitante. Puxou um arquivo antigo. 'Pesquisei. Não é o primeiro.'

Carla folheou os documentos. 1923 - estátua desaparecida do Louvre. 1967 - manuscrito sumido do British Museum. 1989 - vaso Ming evaporado de Shanghai. Sempre a mesma assinatura. Sempre a mesma impossibilidade.

'É a mesma pessoa?'

'Seria mais velho que cem anos.'

'Então é um grupo. Uma sociedade.'

'Ou', Vítor a encarou, 'algo que não é pessoa.'

Carla ia rir. Mas então viu. No canto da moldura, microscópico, um símbolo que não deveria existir. O mesmo símbolo que aparecia marginalmente nas fotos dos outros roubos.

'Precisamos descobrir o que isso significa.'

A investigação os levou por museus, bibliotecas antigas, e finalmente, uma galeria subterrânea que não constava em mapas oficiais. E ali, em paredes de pedra milenares, centenas de obras 'roubadas'. Preservadas. Protegidas.

Uma voz ecoou nas sombras. 'Bem-vindos. Esperávamos por investigadores dignos.'

Um homem velho emergiu. Muito velho. 'Não roubamos', ele explicou. 'Salvamos. Arte que a humanidade destruiria. Guerras. Incêndios. Negligência. Guardamos aqui até que o mundo esteja pronto para valorizá-la de novo.'

Carla deveria prendê-lo. Era seu trabalho. Mas olhou ao redor. Para tesouros que todos pensavam perdidos. Para história preservada em vez de destruída.

'Quanto tempo você faz isso?'

Ele sorriu. 'Desde sempre. Alguém precisa ser o guardião.'

E Carla teve uma escolha. Justiça ou verdade. Lei ou preservação. Às vezes, o mistério maior não é quem cometeu o crime. É decidir se realmente houve crime."""
    },
    {
        "id": 12,
        "genero": "Mistério",
        "personagens": ["Inspector Fábio Lima: policial aposentado"],
        "cenario": "Cidade litorânea, quarenta anos após o caso original",
        "tom": "Melancólico",
        "historia": """A carta chegou num envelope amarelado pelo tempo. Sem remetente. Apenas um endereço que Fábio não pensava há quarenta anos.

'O Caso dos Faróis', ele murmurou, sentindo o peso dos anos nas costas.

Tinha sido seu primeiro caso como inspector. Três faroleiros desaparecidos numa ilha remota. Sem sinais de luta. Sem corpos. Apenas um diário estranho, rabiscado às pressas, falando de luzes no mar e cantos que não deviam existir.

O caso nunca foi resolvido. Arquivado como 'desaparecimento inexplicável'. Mas Fábio nunca esqueceu.

A carta dizia apenas: 'Eu sei o que aconteceu. Encontre-me onde os faróis se encontram.'

Ele sabia o lugar. Uma pequena baía onde, em noites específicas, a luz de três faróis diferentes se cruzava na água. Os faroleiros chamavam de 'o triângulo'.

Fábio chegou ao amanhecer. E ela estava lá. Uma mulher que devia ter oitenta anos, mas cujos olhos lembravam o mar - antigos e profundos.

'Você é filha de um deles', ele afirmou, não perguntou.

'Do Roberto. O faroleiro mais velho.' Ela sorriu tristemente. 'Ele deixou um segundo diário. O real. Aquele que a polícia encontrou era... digamos, editado.'

'Por quê?'

'Porque a verdade é estranha demais. Eles não desapareceram, Inspector. Eles escolheram.'

Ela mostrou o diário. Páginas sobre um mundo subaquático. Sobre seres que não eram exatamente pessoas. Sobre um convite.

'Meu pai estava doente. Cancer terminal. Os outros também tinham suas razões. Aqueles seres ofereceram uma escolha - morrer lentamente, ou viver diferente. Sob as ondas. Transformados. Livres.'

'Isso é loucura.'

'É?' Ela apontou para a baía. 'Olhe. Exatamente onde os faróis se encontram.'

Fábio olhou. E viu. Por um segundo. Três figuras sob a água, acenando. Não humanas. Mas felizes.

'Eles queriam que você soubesse', ela disse. 'Não foi crime. Foi escolha. E às vezes, resolver um mistério é simplesmente aceitar que nem tudo precisa ter explicação que faça sentido.'

Fábio olhou para o diário em suas mãos. Depois para o oceano. E lentamente, sorriu. Quarenta anos carregando culpa. Quarenta anos procurando respostas.

E agora, finalmente, podia descansar.

'Obrigado', ele disse ao mar. E poderia jurar que as ondas sussurraram de volta."""
    }
]

# Metadados úteis
GENEROS_DISPONIVEIS = list(set(s["genero"] for s in STORIES_DATASET))
TONS_DISPONIVEIS = list(set(s["tom"] for s in STORIES_DATASET))

# Função auxiliar para treino
def format_story_for_training(story):
    """
    Formata uma história para o formato esperado pelo modelo
    
    Formato: Gênero: [genero]
             Personagens: [personagens]
             Cenário: [cenario]
             Tom: [tom]
             
             História: [historia]
    """
    personagens_str = ", ".join(story["personagens"]) if isinstance(story["personagens"], list) else story["personagens"]
    
    return f"""Gênero: {story['genero']}
Personagens: {personagens_str}
Cenário: {story['cenario']}
Tom: {story['tom']}

História: {story['historia']}"""

# Estatísticas do dataset
def get_dataset_stats():
    """Retorna estatísticas do dataset"""
    total = len(STORIES_DATASET)
    por_genero = {}
    por_tom = {}
    
    for story in STORIES_DATASET:
        genero = story["genero"]
        tom = story["tom"]
        
        por_genero[genero] = por_genero.get(genero, 0) + 1
        por_tom[tom] = por_tom.get(tom, 0) + 1
    
    return {
        "total": total,
        "por_genero": por_genero,
        "por_tom": por_tom,
        "generos": GENEROS_DISPONIVEIS,
        "tons": TONS_DISPONIVEIS
    }

if __name__ == "__main__":
    # Teste rápido
    print("Dataset de Histórias - Tech Challenge Fase 4")
    print("=" * 50)
    
    stats = get_dataset_stats()
    print(f"\nTotal de histórias: {stats['total']}")
    print(f"\nPor gênero:")
    for gen, count in stats['por_genero'].items():
        print(f"  - {gen}: {count}")
    
    print(f"\nPor tom:")
    for tom, count in stats['por_tom'].items():
        print(f"  - {tom}: {count}")
    
    print("\n" + "=" * 50)
    print("\nExemplo de história formatada para treino:")
    print("=" * 50)
    print(format_story_for_training(STORIES_DATASET[0]))
