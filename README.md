# Gerador de Histórias Interativas

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Transformers](https://img.shields.io/badge/Transformers-4.44-orange.svg)](https://huggingface.co/transformers/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38-red.svg)](https://streamlit.io/)

## Descrição do Projeto

Sistema de **geração criativa de histórias** usando modelos de linguagem generativos. Desenvolvi este projeto para criar histórias originais e envolventes a partir de elementos fornecidos pelo usuário, como gênero literário, personagens e cenários.

**Tech Challenge Fase 4 - FIAP | Machine Learning Engineering**

## Tema Escolhido

**Geração Criativa de Histórias em Português**

Escolhi este tema porque sempre gostei de narrativas e queria explorar como modelos generativos podem criar conteúdo literário original. O sistema oferece:
- Geração de histórias completas (500-1500 palavras)
- Múltiplos gêneros: Ficção Científica, Terror, Romance, Aventura, Fantasia
- Controle sobre elementos narrativos (personagens, cenário, tom)
- Interface interativa para experimentação
- Avaliação de criatividade e coerência narrativa

## Arquitetura do Sistema

### Modelo Base
Após pesquisar modelos de linguagem em português, escolhi o GPT-2 Portuguese:
- **Modelo**: GPT-2 Portuguese (`pierreguillou/gpt2-small-portuguese`)
- **Tipo**: Transformer Decoder-Only (arquitetura generativa)
- **Parâmetros**: aproximadamente 124M
- **Linguagem**: Português
- **Tarefa**: Geração de Texto Criativo (narrativas longas e coerentes)

### Componentes Principais
Durante o desenvolvimento, organizei o projeto em 4 componentes principais:

1. **Gerador de Histórias** - Motor de geração usando GPT-2 fine-tuned
2. **Sistema de Prompts** - Templates para diferentes gêneros literários
3. **Interface Interativa** - Aplicação Streamlit para criação de histórias
4. **Sistema de Avaliação** - Métricas de criatividade, coerência e originalidade

### Formato de Treinamento
Aprendi que o modelo funciona melhor com um formato estruturado:
```
Gênero: [gênero literário]
Personagens: [lista de personagens]
Cenário: [descrição do ambiente]

História: [texto completo da história gerada]
```

## Estrutura do Projeto

Organizei os arquivos da seguinte forma:

```
tech-challenge-fase-4/
│
├── app.py                      # Aplicação Streamlit principal
├── train_model.ipynb           # Notebook de fine-tuning
├── train_model_script.py       # Script de treinamento alternativo
├── evaluate_model.py           # Avaliação de qualidade
├── examples.py                 # Exemplos de uso
├── requirements.txt            # Dependências
├── README.md                   # Documentação principal
├── Dockerfile                  # Container Docker
│
├── src/
│   ├── __init__.py
│   ├── model.py               # Classe TextGenerator
│   ├── prompts.py             # Templates de gêneros
│   └── utils.py               # Funções utilitárias
│
├── data/
│   └── sample_stories.py      # Dataset de histórias para treino
│
├── models/
│   └── fine_tuned_gpt2_story_generator/  # Modelo treinado
│
└── docs/                       # Documentação completa
    ├── QUICKSTART.md          # Guia rápido
    ├── DEPLOYMENT.md          # Guia de deployment
    ├── ENTREGA.md             # Checklist de entrega
    ├── VIDEO_SCRIPT.md        # Roteiro do vídeo
    ├── PROJETO_COMPLETO.md    # Documentação detalhada
    └── INDEX.md               # Índice da documentação
```

## Início Rápido

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/tech-challenge-fase-4.git
cd tech-challenge-fase-4

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale dependências
pip install -r requirements.txt
```

### Execute a Aplicação

```bash
streamlit run app.py
```

Acesse: `http://localhost:8501`

## Como Usar

Implementei três modos de geração de histórias:

### Modo 1: Geração Guiada
A forma mais controlada de criar histórias:
1. Selecione o gênero literário (Ficção Científica, Terror, Romance, etc)
2. Defina personagens principais (nomes e características)
3. Descreva o cenário/ambiente
4. Escolha o tom narrativo (Aventuroso, Sombrio, Romântico, Humorístico)
5. Clique em "Gerar História"

### Modo 2: Continuação Criativa
Para co-criar com o modelo:
1. Escreva as primeiras frases da sua história
2. Configure o tamanho de continuação desejado
3. O modelo continua de forma criativa e surpreendente

### Modo 3: Geração Livre
Deixa o modelo criar tudo:
1. Apenas escolha o gênero
2. O modelo inventa personagens, cenário e trama
3. História completamente original a cada geração

## Métricas de Avaliação

Aprendi a avaliar histórias geradas com métricas específicas:

### Métricas de Criatividade
- **Diversidade Léxica**: Variedade de vocabulário usado
- **Originalidade**: Uso de combinações únicas de palavras
- **Complexidade Narrativa**: Estrutura da trama

### Métricas de Qualidade
- **Coerência**: A história faz sentido do início ao fim?
- **Perplexidade**: Indica a "surpresa" do modelo (menor = mais confiante)
- **Comprimento**: Histórias geradas têm tamanho adequado?

### Avaliação Humana
Também implementei sistema de feedback:
- Classificação de 1-5 estrelas
- Coerência narrativa
- Envolvimento emocional
- Criatividade percebida

### Executar Avaliação

Criei um script para avaliar o modelo:
```bash
python evaluate_model.py --model ./models/fine_tuned_gpt2_story_generator
```

## Treinamento do Modelo

Para treinar o modelo, desenvolvi um notebook Jupyter completo:

```bash
jupyter notebook train_model.ipynb
```

Etapas que segui no treinamento:
1. Carregamento do modelo base GPT-2 Portuguese
2. Preparação do dataset com histórias de diferentes gêneros
3. Fine-tuning usando formato estruturado com gênero, personagens e cenário
4. Avaliação comparando histórias geradas vs. modelo base
5. Ajuste de hiperparâmetros (temperature, top_p) para criatividade
6. Salvamento do modelo treinado para uso

## Dataset

Reuni um dataset diversificado para treinar o modelo:
- **Fonte**: Contos brasileiros de domínio público, literatura contemporânea
- **Gêneros**: Ficção Científica, Terror, Romance, Aventura, Fantasia, Mistério
- **Tamanho**: 50+ histórias completas para fine-tuning
- **Formato**: Cada história anotada com gênero, personagens e cenário

## Configurações Avançadas

Durante os testes, identifiquei os melhores parâmetros para criatividade:

| Parâmetro | Descrição | Valores para histórias |
|-----------|-----------|------------------------|
| `temperature` | Controla criatividade | 0.8-1.0 (mais criativo) |
| `max_length` | Tamanho da história | 500-1500 palavras |
| `top_p` | Nucleus sampling | 0.90-0.95 (diversidade) |
| `repetition_penalty` | Evita repetições | 1.2 (natural) |

## Deployment

Para disponibilizar o projeto online, planejei usar o Streamlit Cloud:

1. Fazer push do código para GitHub
2. Acessar [share.streamlit.io](https://share.streamlit.io)
3. Conectar o repositório
4. Configurar e fazer deploy automático

## Documentação

Organizei a documentação essencial na pasta `docs/`:

- [Guia Rápido](docs/QUICKSTART.md) - Para começar rapidamente
- [Guia de Deployment](docs/DEPLOYMENT.md) - Como fazer deploy no Streamlit Cloud
- [Roteiro do Vídeo](docs/VIDEO_SCRIPT.md) - Script da apresentação
- [Entrega do Projeto](docs/ENTREGA.md) - Checklist e links de entrega
- [Projeto Completo](docs/PROJETO_COMPLETO.md) - Documentação detalhada
- [Índice](docs/INDEX.md) - Navegação completa da documentação

## Exemplos de Histórias Geradas

### Ficção Científica
```
Personagens: Ana (cientista), ARIA (IA)
Cenário: Laboratório em Marte, 2089

[História gerada pelo modelo - 800 palavras]
```

### Terror
```
Personagens: Pedro (investigador)
Cenário: Casa abandonada em São Paulo

[História gerada pelo modelo - 600 palavras]
```

## Vídeo Demonstrativo

Preparei um vídeo de aproximadamente 7 minutos mostrando:
- Contextualização: por que geração criativa de histórias?
- Arquitetura e tecnologias utilizadas (GPT-2, Transformers, Streamlit)
- Demonstração prática gerando histórias em diferentes gêneros
- Processo de fine-tuning e desafios encontrados
- Métricas de criatividade e coerência
- Aprendizados e possíveis melhorias futuras

Link: [Em breve no YouTube]

## Autor

Ricardo Matos - FIAP Tech Challenge Fase 4

Desenvolvido como projeto final da disciplina de Machine Learning Engineering

---

**FIAP | Machine Learning Engineering**  
**Outubro 2025**

## 👨‍💻 Autor

Ricardo Matos - FIAP - Tech Challenge Fase 4

## 📝 Licença

Este projeto é desenvolvido para fins educacionais como parte do curso de Machine Learning Engineering da FIAP.
