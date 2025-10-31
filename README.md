# Gerador de Histórias Interativas

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Transformers](https://img.shields.io/badge/Transformers-4.44-orange.svg)](https://huggingface.co/transformers/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38-red.svg)](https://streamlit.io/)

**Tech Challenge Fase 4 - FIAP | Machine Learning Engineering**

## 📖 Sobre o Projeto

Sistema de **geração criativa de histórias em português** utilizando modelos de linguagem generativos (GPT-2 e BLOOM). A aplicação permite criar narrativas originais e envolventes em diversos gêneros literários através de uma interface interativa.

### Funcionalidades

- 📚 **Múltiplos gêneros**: Ficção Científica, Terror, Romance, Aventura, Fantasia, Mistério
- 🎭 **Modos de geração**: Guiada (com controle), Continuação Criativa, Geração Livre
- 🤖 **Modelos disponíveis**: Fine-tuned GPT-2, BLOOM 560M, BLOOM 1B1, mGPT
- ⚙️ **Configurações ajustáveis**: Temperature, tamanho, tom narrativo
- 📊 **Avaliação de qualidade**: Métricas de criatividade e coerência

## 🚀 Início Rápido

### Instalação

```bash
# Clone o repositório
git clone https://github.com/RicardoSMatos/fiap-fase-4.git
cd fiap-fase-4

# Crie ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt
```

### Executar Aplicação

```bash
streamlit run app.py
```

Acesse: `http://localhost:8501`

## 📁 Estrutura do Projeto

```
fiap-fase-4/
├── app.py                    # Aplicação Streamlit
├── train_model_script.py     # Script de treinamento
├── evaluate_model.py         # Avaliação do modelo
├── src/                      # Módulos principais
│   ├── model.py             # Classe TextGenerator
│   ├── prompts.py           # Templates otimizados
│   └── utils.py
├── data/                     # Dataset de histórias
└── docs/                     # Documentação completa
```

## 🎯 Como Usar

### 1. Geração Guiada
Controle total sobre personagens, cenário e tom narrativo.

### 2. Continuação Criativa
Escreva o início e o modelo continua a história.

### 3. Geração Livre
O modelo cria tudo: personagens, cenário e trama.

## 🤖 Modelos Disponíveis

| Modelo | Parâmetros | Qualidade | Velocidade |
|--------|-----------|-----------|-----------|
| Fine-tuned GPT-2 | 124M | ⭐⭐⭐⭐⭐ | 🚀🚀🚀 |
| BLOOM 560M | 560M | ⭐⭐⭐⭐ | 🚀🚀 |
| BLOOM 1B1 | 1.1B | ⭐⭐⭐⭐⭐ | 🚀 |
| mGPT | 1.3B | ⭐⭐⭐⭐ | 🚀 |

## 📚 Documentação

Para mais informações, consulte a [documentação completa](docs/):

- [Guia Rápido](docs/QUICKSTART.md)
- [Deployment](docs/DEPLOYMENT.md)
- [Informações de Entrega](docs/ENTREGA.md)

## 👨‍💻 Autor

**Ricardo Matos**  
FIAP - Machine Learning Engineering - Fase 4  
Outubro 2025

## 📝 Licença

Projeto desenvolvido para fins educacionais como parte do curso de Machine Learning Engineering da FIAP.
