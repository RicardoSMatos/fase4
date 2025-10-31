"""
Exemplos de notícias para treinamento do modelo de sumarização.
Formato: Pares de notícia completa + resumo
"""

# Formato: (notícia_completa, resumo_esperado)
NEWS_EXAMPLES = [
    {
        "titulo": "Brasil atinge meta de vacinação contra COVID-19",
        "noticia": """O Ministério da Saúde anunciou nesta terça-feira que o Brasil atingiu 
        a meta de 90% da população adulta totalmente vacinada contra a COVID-19. O marco 
        representa um esforço nacional que durou quase dois anos, envolvendo mais de 
        200 mil profissionais de saúde. A campanha de vacinação começou em janeiro de 2021 
        e enfrentou diversos desafios, incluindo a logística de distribuição das doses e 
        o combate à desinformação. Segundo o ministro da Saúde, a conquista coloca o país 
        entre os mais bem-sucedidos em imunização na América Latina. Os especialistas 
        alertam, no entanto, que é necessário manter as doses de reforço em dia.""",
        "resumo": """Brasil alcançou 90% da população adulta vacinada contra COVID-19 após 
        dois anos de campanha. Ministério da Saúde destaca esforço de 200 mil profissionais, 
        mas especialistas reforçam necessidade de doses de reforço."""
    },
    {
        "titulo": "Inteligência Artificial revoluciona diagnóstico médico",
        "noticia": """Pesquisadores da Universidade de São Paulo desenvolveram um sistema 
        de inteligência artificial capaz de diagnosticar doenças raras com 95% de precisão. 
        A tecnologia analisa exames de imagem e histórico médico em segundos, auxiliando 
        médicos em decisões complexas. O sistema foi treinado com mais de 100 mil casos 
        clínicos e já está sendo testado em três hospitais públicos de São Paulo. A 
        ferramenta não substitui o médico, mas serve como uma segunda opinião valiosa, 
        especialmente em regiões com escassez de especialistas. O projeto recebeu 
        investimento de R$ 5 milhões e deve estar disponível gratuitamente pelo SUS 
        até o final de 2026.""",
        "resumo": """USP desenvolve IA com 95% de precisão para diagnosticar doenças raras. 
        Sistema analisa exames e histórico em segundos, já em testes em hospitais de SP. 
        Ferramenta será gratuita no SUS até 2026."""
    },
    {
        "titulo": "Desmatamento na Amazônia cai 40% em 2025",
        "noticia": """Dados do Instituto Nacional de Pesquisas Espaciais (INPE) mostram 
        que o desmatamento na Amazônia caiu 40% no primeiro semestre de 2025 em comparação 
        ao mesmo período do ano anterior. A redução é atribuída ao fortalecimento da 
        fiscalização ambiental e a programas de desenvolvimento sustentável. Foram 
        desmatados 3.500 km² de floresta, contra 5.800 km² em 2024. O ministro do Meio 
        Ambiente celebrou os números, mas alertou que o combate ao desmatamento ilegal 
        precisa ser contínuo. Organizações ambientais elogiaram o resultado mas pedem 
        mais investimento em fiscalização.""",
        "resumo": """Desmatamento na Amazônia cai 40% no primeiro semestre de 2025, segundo 
        INPE. Redução de 5.800 km² para 3.500 km² é atribuída a maior fiscalização e 
        programas sustentáveis."""
    },
    {
        "titulo": "Mercado financeiro projeta inflação de 4,5% para 2025",
        "noticia": """O boletim Focus, divulgado pelo Banco Central, mostrou que o mercado 
        financeiro elevou a projeção de inflação para 2025 de 4,2% para 4,5%. O aumento 
        reflete preocupações com a alta dos preços de alimentos e energia. Analistas 
        apontam que a seca prolongada afetou a produção agrícola e elevou os custos de 
        energia elétrica. O Banco Central sinalizou que pode elevar a taxa Selic se a 
        inflação continuar acelerando. Economistas recomendam cautela nas decisões de 
        investimento e consumo para o restante do ano.""",
        "resumo": """Mercado eleva projeção de inflação para 2025 de 4,2% para 4,5%, segundo 
        Boletim Focus. Alta reflete preços de alimentos e energia afetados por seca. BC 
        pode elevar Selic."""
    },
    
    """A floresta antiga guardava memórias de tempos imemoriais. Cada árvore era 
    uma biblioteca viva, e o vento que passava entre suas folhas contava histórias 
    dos que ali viveram.""",
    
    """No topo da montanha mais alta, onde o ar era rarefeito e o frio cortava como 
    uma lâmina, havia um templo. Diziam que quem chegasse lá encontraria as respostas 
    que procurava.""",
    
    """O relógio parou exatamente à meia-noite. Naquele momento, o tempo pareceu 
    congelar, e uma brecha se abriu entre os mundos. Foi então que eles chegaram.""",
    
    """A biblioteca proibida escondia mais que livros antigos. Entre suas prateleiras 
    empoeiradas, segredos esperavam por mentes curiosas o suficiente para desvendá-los.""",
    
    """Em uma pequena vila no interior, onde todos se conheciam, começou a acontecer 
    algo estranho. As pessoas começaram a ter os mesmos sonhos, noite após noite.""",
    
    """O artista pintava quadros que pareciam vivos. Quem olhasse fixamente para eles 
    por tempo suficiente jurava que as figuras se moviam quando ninguém estava olhando.""",
    
    """A música que tocava naquela caixa de música era diferente. Não era apenas som, 
    mas memórias cristalizadas que se espalhavam pelo ar como perfume.""",
    
    """O jardim secreto florescia mesmo no inverno mais rigoroso. Suas flores eram 
    de cores que não existiam na natureza, e seu perfume tinha o poder de curar 
    corações feridos.""",
    
    """A última pessoa a ver o farol aceso foi o velho pescador. Ele contava que 
    a luz não era feita de fogo, mas de esperança condensada.""",
    
    """No meio do deserto, onde não deveria haver nada além de areia, encontraram 
    um oásis. Mas esse não era um oásis comum - suas águas refletiam não o céu, 
    mas outros mundos.""",
    
    """A ponte que ligava as duas margens do rio tinha uma peculiaridade: dependendo 
    de quando você a cruzasse, chegava a lugares diferentes.""",
    
    """O mercador de sonhos chegava sempre ao entardecer. Trazia em sua carroça 
    frascos contendo os sonhos mais belos e também os pesadelos mais terríveis.""",
    
    """A criança que falava com os animais não era especial por ter esse dom, mas 
    por escolher ouvir o que eles tinham a dizer.""",
    
    """No sótão da velha mansão, encontraram um espelho que refletia não o presente, 
    mas possibilidades de futuros que poderiam ter sido.""",
    
    """O último guardião da chama eterna sabia que seu tempo estava chegando ao fim. 
    Mas antes de partir, precisava encontrar alguém digno de continuar sua missão.""",
]

def get_sample_texts(n=None):
    """
    Retorna textos de exemplo para treinamento.
    
    Args:
        n: Número de textos a retornar (None = todos)
        
    Returns:
        Lista de textos
    """
    if n is None:
        return CREATIVE_TEXTS
    return CREATIVE_TEXTS[:n]


def load_custom_dataset(file_path=None):
    """
    Carrega dataset customizado de arquivo.
    
    Args:
        file_path: Caminho para arquivo .txt com textos (um por linha)
        
    Returns:
        Lista de textos
    """
    if file_path is None:
        return CREATIVE_TEXTS
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            texts = [line.strip() for line in f if line.strip()]
        return texts
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return CREATIVE_TEXTS
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}")
        return CREATIVE_TEXTS


if __name__ == "__main__":
    # Testa as funções
    print(f"Total de textos de exemplo: {len(CREATIVE_TEXTS)}")
    print(f"\nPrimeiro texto:\n{CREATIVE_TEXTS[0]}")
    
    # Mostra estatísticas
    total_chars = sum(len(text) for text in CREATIVE_TEXTS)
    total_words = sum(len(text.split()) for text in CREATIVE_TEXTS)
    
    print(f"\n📊 Estatísticas:")
    print(f"  • Total de caracteres: {total_chars:,}")
    print(f"  • Total de palavras: {total_words:,}")
    print(f"  • Média de palavras por texto: {total_words / len(CREATIVE_TEXTS):.0f}")
