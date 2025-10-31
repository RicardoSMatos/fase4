"""
Templates de Prompts por Gênero
Tech Challenge Fase 4 - FIAP

Este arquivo contém templates específicos para cada gênero literário,
ajudando o modelo a manter consistência narrativa e estilo adequado.

Durante os testes, descobri que usar templates estruturados melhora
significativamente a qualidade e coerência das histórias geradas.
"""

# Templates por gênero
TEMPLATES_POR_GENERO = {
    "Ficção Científica": {
        "elementos_comuns": [
            "tecnologia avançada",
            "exploração espacial",
            "inteligência artificial",
            "viagem no tempo",
            "mundos futuros",
            "dilemas científicos"
        ],
        "tons_recomendados": ["Aventuroso", "Épico", "Sombrio"],
        "exemplo_inicio": "No ano {ano}, a humanidade finalmente {descoberta}. Mas nem tudo era como esperado...",
        "palavras_chave": ["nave", "computador", "robô", "planeta", "científico", "tecnologia", "futuro", "experimento"]
    },
    
    "Terror": {
        "elementos_comuns": [
            "suspense crescente",
            "atmosfera sombria",
            "elementos sobrenaturais",
            "isolamento",
            "medo do desconhecido",
            "reviravoltas inesperadas"
        ],
        "tons_recomendados": ["Sombrio", "Melancólico"],
        "exemplo_inicio": "A noite estava escura demais. {personagem} não deveria estar ali, mas {motivo}...",
        "palavras_chave": ["sombra", "escuro", "silêncio", "sussurro", "frio", "sangue", "medo", "noite"]
    },
    
    "Romance": {
        "elementos_comuns": [
            "desenvolvimento de relacionamento",
            "conflitos emocionais",
            "superação de obstáculos",
            "química entre personagens",
            "momentos íntimos",
            "dilemas do coração"
        ],
        "tons_recomendados": ["Romântico", "Melancólico", "Humorístico"],
        "exemplo_inicio": "{personagem1} não esperava encontrar {personagem2} naquele {lugar}. Mas às vezes o destino...",
        "palavras_chave": ["coração", "sentir", "olhar", "amor", "beijo", "toque", "sorriso", "emoção"]
    },
    
    "Aventura": {
        "elementos_comuns": [
            "jornada épica",
            "desafios e obstáculos",
            "descobertas",
            "ação e movimento",
            "exploração",
            "crescimento do herói"
        ],
        "tons_recomendados": ["Aventuroso", "Épico", "Humorístico"],
        "exemplo_inicio": "A missão parecia simples: {objetivo}. Mas {personagem} logo descobriria que...",
        "palavras_chave": ["explorar", "descobrir", "buscar", "perigo", "mistério", "tesouro", "mapa", "jornada"]
    },
    
    "Fantasia": {
        "elementos_comuns": [
            "magia e feitiços",
            "criaturas místicas",
            "mundos imaginários",
            "profecias antigas",
            "poderes especiais",
            "batalha entre bem e mal"
        ],
        "tons_recomendados": ["Épico", "Aventuroso", "Sombrio"],
        "exemplo_inicio": "Em {mundo}, onde a magia {caracteristica}, {personagem} descobriu seu verdadeiro destino...",
        "palavras_chave": ["magia", "feitiço", "dragão", "reino", "profecia", "poder", "místico", "encantamento"]
    },
    
    "Mistério": {
        "elementos_comuns": [
            "enigmas a resolver",
            "pistas e evidências",
            "reviravoltas surpreendentes",
            "investigação",
            "segredos revelados",
            "dedução lógica"
        ],
        "tons_recomendados": ["Sombrio", "Aventuroso", "Melancólico"],
        "exemplo_inicio": "O caso parecia impossível. {evidencia} não fazia sentido. Mas {personagem} sabia que...",
        "palavras_chave": ["investigar", "pista", "segredo", "enigma", "descobrir", "suspeito", "evidência", "resolver"]
    }
}

# Estruturas narrativas por ato
ESTRUTURA_TRES_ATOS = {
    "ato_1": {
        "nome": "Apresentação",
        "porcentagem": 25,
        "elementos": [
            "Introdução do protagonista",
            "Estabelecimento do mundo/cenário",
            "Evento incitante",
            "Primeiro conflito ou objetivo"
        ]
    },
    "ato_2": {
        "nome": "Confrontação",
        "porcentagem": 50,
        "elementos": [
            "Desenvolvimento de obstáculos",
            "Aprofundamento de personagens",
            "Complicações crescentes",
            "Momento de maior tensão"
        ]
    },
    "ato_3": {
        "nome": "Resolução",
        "porcentagem": 25,
        "elementos": [
            "Clímax da história",
            "Resolução do conflito principal",
            "Transformação dos personagens",
            "Conclusão satisfatória"
        ]
    }
}

# Dicas de escrita por tom
DICAS_POR_TOM = {
    "Aventuroso": {
        "ritmo": "Rápido e dinâmico",
        "foco": "Ação e descobertas",
        "linguagem": "Direta e envolvente",
        "evitar": "Descrições muito longas, digressões filosóficas"
    },
    "Sombrio": {
        "ritmo": "Tenso e controlado",
        "foco": "Atmosfera e suspense",
        "linguagem": "Evocativa e sensorial",
        "evitar": "Humor excessivo, finais muito felizes"
    },
    "Romântico": {
        "ritmo": "Variável com momentos íntimos",
        "foco": "Emoções e relacionamentos",
        "linguagem": "Emotiva e descritiva",
        "evitar": "Frieza emocional, diálogos mecânicos"
    },
    "Humorístico": {
        "ritmo": "Leve e variado",
        "foco": "Situações cômicas e diálogos espirituosos",
        "linguagem": "Criativa e surpreendente",
        "evitar": "Drama pesado demais, tons muito sérios"
    },
    "Épico": {
        "ritmo": "Grandioso e expansivo",
        "foco": "Grande escala e destinos importantes",
        "linguagem": "Elevada e poderosa",
        "evitar": "Banalidades, foco em detalhes triviais"
    },
    "Melancólico": {
        "ritmo": "Contemplativo e reflexivo",
        "foco": "Emoções complexas e memórias",
        "linguagem": "Poética e introspectiva",
        "evitar": "Ação frenética, otimismo exagerado"
    }
}

def construir_prompt_detalhado(genero, personagens="", cenario="", tom="", elementos_extras=None):
    """
    Constrói um prompt OTIMIZADO e detalhado para máxima qualidade narrativa.
    
    Args:
        genero: Gênero literário da história
        personagens: Descrição dos personagens (opcional)
        cenario: Descrição do cenário (opcional)
        tom: Tom narrativo desejado (opcional)
        elementos_extras: Dict com elementos adicionais (opcional)
    
    Returns:
        String com o prompt formatado e otimizado
    """
    template = TEMPLATES_POR_GENERO.get(genero, {})
    
    # Inicia com instrução clara ao modelo
    prompt = f"Você é um escritor criativo especializado em {genero}.\n\n"
    
    # Instrução de tarefa
    prompt += "TAREFA: Escreva uma história original, criativa e envolvente.\n\n"
    
    # Configuração da história
    prompt += "=== CONFIGURAÇÃO DA HISTÓRIA ===\n"
    prompt += f"Gênero: {genero}\n"
    
    # Elementos do gênero
    if template.get("elementos_comuns"):
        elementos = template["elementos_comuns"][:3]
        prompt += f"Elementos esperados: {', '.join(elementos)}\n"
    
    # Personagens com mais contexto
    if personagens:
        prompt += f"\nPersonagens principais:\n{personagens}\n"
        prompt += "Desenvolvimento: Mostre suas personalidades através de ações e diálogos.\n"
    
    # Cenário detalhado
    if cenario:
        prompt += f"\nCenário:\n{cenario}\n"
        prompt += "Descrição: Use detalhes sensoriais (visão, som, cheiro, tato).\n"
    
    # Tom e estilo
    if tom:
        prompt += f"\nTom narrativo: {tom}\n"
        dicas = DICAS_POR_TOM.get(tom, {})
        if dicas:
            prompt += f"Ritmo: {dicas.get('ritmo', 'Variável')}\n"
            prompt += f"Foco: {dicas.get('foco', 'Narrativa envolvente')}\n"
            prompt += f"Evite: {dicas.get('evitar', 'Clichês')}\n"
    
    # Estrutura narrativa
    prompt += "\n=== ESTRUTURA NARRATIVA ===\n"
    prompt += "1. INÍCIO: Apresente o contexto e personagens de forma envolvente\n"
    prompt += "2. DESENVOLVIMENTO: Construa tensão e conflito\n"
    prompt += "3. CLÍMAX: Momento de maior intensidade\n"
    prompt += "4. RESOLUÇÃO: Desfecho satisfatório\n"
    
    # Diretrizes de qualidade
    prompt += "\n=== DIRETRIZES DE QUALIDADE ===\n"
    prompt += "✓ Mantenha o foco no tema principal\n"
    prompt += "✓ Use diálogos naturais e autênticos\n"
    prompt += "✓ Mostre, não apenas conte (show, don't tell)\n"
    prompt += "✓ Crie imagens vívidas com descrições sensoriais\n"
    prompt += "✓ Mantenha coerência temporal e espacial\n"
    prompt += "✓ Evite repetições desnecessárias\n"
    
    # Palavras-chave do gênero
    if template.get("palavras_chave"):
        chaves = template["palavras_chave"][:5]
        prompt += f"\nVocabulário sugerido: {', '.join(chaves)}\n"
    
    # Elementos extras
    if elementos_extras:
        prompt += "\n=== ELEMENTOS ADICIONAIS ===\n"
        for chave, valor in elementos_extras.items():
            prompt += f"{chave.title()}: {valor}\n"
    
    # Início da história
    prompt += "\n=== COMECE A HISTÓRIA AGORA ===\n"
    prompt += "História:\n\n"
    
    return prompt

def get_sugestoes_genero(genero):
    """
    Retorna sugestões e dicas para um gênero específico
    
    Args:
        genero: Nome do gênero literário
    
    Returns:
        Dict com sugestões, elementos comuns, tons recomendados
    """
    return TEMPLATES_POR_GENERO.get(genero, {
        "elementos_comuns": [],
        "tons_recomendados": [],
        "exemplo_inicio": "",
        "palavras_chave": []
    })

def validar_combinacao(genero, tom):
    """
    Valida se a combinação de gênero e tom é recomendada
    
    Args:
        genero: Gênero literário
        tom: Tom narrativo
    
    Returns:
        Tuple (bool, str): (é_valido, mensagem)
    """
    template = TEMPLATES_POR_GENERO.get(genero)
    
    if not template:
        return False, f"Gênero '{genero}' não reconhecido"
    
    tons_recomendados = template.get("tons_recomendados", [])
    
    if tom in tons_recomendados:
        return True, "Combinação recomendada!"
    else:
        return True, f"Combinação possível. Tons mais comuns para {genero}: {', '.join(tons_recomendados)}"

def gerar_ideias_personagem(genero):
    """
    Gera sugestões de tipos de personagens para um gênero
    
    Args:
        genero: Gênero literário
    
    Returns:
        List de sugestões de personagens
    """
    ideias = {
        "Ficção Científica": [
            "Cientista visionário(a)",
            "Piloto de nave espacial",
            "Inteligência artificial consciente",
            "Engenheiro(a) de sistemas",
            "Explorador(a) interestelar"
        ],
        "Terror": [
            "Investigador(a) sobrenatural",
            "Sobrevivente traumatizado(a)",
            "Criança com habilidades estranhas",
            "Pesquisador(a) paranormal",
            "Morador(a) de local mal-assombrado"
        ],
        "Romance": [
            "Artista sensível",
            "Professor(a) dedicado(a)",
            "Médico(a) compassivo(a)",
            "Músico(a) talentoso(a)",
            "Escritor(a) em bloqueio criativo"
        ],
        "Aventura": [
            "Arqueólogo(a) destemido(a)",
            "Explorador(a) experiente",
            "Guia local conhecedor",
            "Aventureiro(a) buscando tesouros",
            "Capitão de expedição"
        ],
        "Fantasia": [
            "Feiticeiro(a) aprendiz",
            "Guerreiro(a) lendário(a)",
            "Elfo/Elfa sábio(a)",
            "Dragão ancestral",
            "Guardião(a) de antiga profecia"
        ],
        "Mistério": [
            "Detetive experiente",
            "Jornalista investigativo(a)",
            "Ex-policial aposentado(a)",
            "Psicólogo(a) criminal",
            "Testemunha acidental"
        ]
    }
    
    return ideias.get(genero, [
        "Protagonista carismático(a)",
        "Personagem com passado misterioso",
        "Pessoa comum em situação extraordinária"
    ])

def gerar_ideias_cenario(genero):
    """
    Gera sugestões de cenários para um gênero
    
    Args:
        genero: Gênero literário
    
    Returns:
        List de sugestões de cenários
    """
    ideias = {
        "Ficção Científica": [
            "Estação espacial orbital",
            "Colônia em planeta distante",
            "Laboratório de pesquisa futurista",
            "Nave geracional em viagem centenária",
            "Cidade cyberpunk ano 2100"
        ],
        "Terror": [
            "Casa abandonada com história sombria",
            "Hospital psiquiátrico desativado",
            "Floresta isolada à noite",
            "Cemitério antigo",
            "Mansão vitoriana mal-assombrada"
        ],
        "Romance": [
            "Café aconchegante em Paris",
            "Praia ao pôr do sol",
            "Livraria independente",
            "Pequena cidade do interior",
            "Ateliê de arte"
        ],
        "Aventura": [
            "Floresta amazônica inexplorada",
            "Ruínas de civilização perdida",
            "Ilha remota no Pacífico",
            "Montanhas do Himalaia",
            "Deserto do Saara"
        ],
        "Fantasia": [
            "Reino mágico ameaçado",
            "Floresta encantada",
            "Torre de feiticeiro nas nuvens",
            "Cavernas de cristal luminoso",
            "Cidade flutuante"
        ],
        "Mistério": [
            "Museu com artefatos raros",
            "Mansão de família rica",
            "Cidade pequena com segredos",
            "Biblioteca antiga",
            "Hotel histórico isolado"
        ]
    }
    
    return ideias.get(genero, [
        "Local comum com atmosfera especial",
        "Lugar isolado do mundo",
        "Ambiente urbano contemporâneo"
    ])

# Ajustes de parâmetros de geração por gênero
PARAMETROS_POR_GENERO = {
    "Ficção Científica": {
        "temperature": 0.9,
        "top_p": 0.95,
        "repetition_penalty": 1.2,
        "descricao": "Balanceado entre criatividade e coerência técnica"
    },
    "Terror": {
        "temperature": 1.0,
        "top_p": 0.92,
        "repetition_penalty": 1.3,
        "descricao": "Mais criativo para gerar situações inesperadas"
    },
    "Romance": {
        "temperature": 0.85,
        "top_p": 0.95,
        "repetition_penalty": 1.15,
        "descricao": "Mais focado em emoções e desenvolvimento gradual"
    },
    "Aventura": {
        "temperature": 0.95,
        "top_p": 0.93,
        "repetition_penalty": 1.2,
        "descricao": "Dinâmico e variado para ação constante"
    },
    "Fantasia": {
        "temperature": 1.05,
        "top_p": 0.95,
        "repetition_penalty": 1.25,
        "descricao": "Muito criativo para elementos mágicos únicos"
    },
    "Mistério": {
        "temperature": 0.88,
        "top_p": 0.94,
        "repetition_penalty": 1.2,
        "descricao": "Focado e lógico com reviravoltas controladas"
    }
}

def get_parametros_recomendados(genero):
    """
    Retorna parâmetros de geração recomendados para um gênero
    
    Args:
        genero: Gênero literário
    
    Returns:
        Dict com temperature, top_p, repetition_penalty e descrição
    """
    return PARAMETROS_POR_GENERO.get(genero, {
        "temperature": 0.9,
        "top_p": 0.95,
        "repetition_penalty": 1.2,
        "descricao": "Parâmetros padrão balanceados"
    })

if __name__ == "__main__":
    # Testes rápidos
    print("=== Templates de Prompts - Tech Challenge Fase 4 ===\n")
    
    # Teste 1: Construir prompt detalhado
    print("1. Prompt Detalhado (Ficção Científica):")
    print("-" * 60)
    prompt = construir_prompt_detalhado(
        "Ficção Científica",
        "Ana: cientista corajosa, ARIA: IA",
        "Estação espacial em Marte, 2089",
        "Aventuroso"
    )
    print(prompt)
    
    # Teste 2: Sugestões por gênero
    print("\n2. Sugestões para Terror:")
    print("-" * 60)
    sugestoes = get_sugestoes_genero("Terror")
    print(f"Elementos: {', '.join(sugestoes['elementos_comuns'][:3])}")
    print(f"Tons recomendados: {', '.join(sugestoes['tons_recomendados'])}")
    
    # Teste 3: Validar combinação
    print("\n3. Validação de Combinações:")
    print("-" * 60)
    valido, msg = validar_combinacao("Romance", "Romântico")
    print(f"Romance + Romântico: {msg}")
    valido, msg = validar_combinacao("Terror", "Humorístico")
    print(f"Terror + Humorístico: {msg}")
    
    # Teste 4: Ideias de personagens
    print("\n4. Sugestões de Personagens (Fantasia):")
    print("-" * 60)
    personagens = gerar_ideias_personagem("Fantasia")
    for i, p in enumerate(personagens[:3], 1):
        print(f"  {i}. {p}")
    
    # Teste 5: Ideias de cenários
    print("\n5. Sugestões de Cenários (Mistério):")
    print("-" * 60)
    cenarios = gerar_ideias_cenario("Mistério")
    for i, c in enumerate(cenarios[:3], 1):
        print(f"  {i}. {c}")
    
    # Teste 6: Parâmetros recomendados
    print("\n6. Parâmetros Recomendados (Terror):")
    print("-" * 60)
    params = get_parametros_recomendados("Terror")
    print(f"Temperature: {params['temperature']}")
    print(f"Top_p: {params['top_p']}")
    print(f"Repetition Penalty: {params['repetition_penalty']}")
    print(f"Descrição: {params['descricao']}")
