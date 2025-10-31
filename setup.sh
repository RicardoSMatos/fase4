#!/bin/bash

# Script de configuração do projeto
# Tech Challenge Fase 4 - FIAP

echo "🚀 Iniciando setup do projeto..."
echo ""

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.8 ou superior."
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Cria ambiente virtual
echo "📦 Criando ambiente virtual..."
python3 -m venv venv

# Ativa ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

echo "✅ Ambiente virtual criado e ativado!"
echo ""

# Atualiza pip
echo "⬆️  Atualizando pip..."
pip install --upgrade pip

echo ""

# Instala dependências
echo "📚 Instalando dependências..."
echo "⏰ Isso pode levar alguns minutos..."
echo ""

pip install -r requirements.txt

echo ""
echo "✅ Dependências instaladas com sucesso!"
echo ""

# Cria diretórios necessários
echo "📁 Criando estrutura de diretórios..."
mkdir -p data/raw
mkdir -p data/processed
mkdir -p models/fine_tuned

echo "✅ Diretórios criados!"
echo ""

# Mensagem final
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                                                            ║"
echo "║  ✅  Setup concluído com sucesso!                         ║"
echo "║                                                            ║"
echo "║  📝  Próximos passos:                                     ║"
echo "║                                                            ║"
echo "║  1. Para treinar o modelo:                                ║"
echo "║     jupyter notebook train_model.ipynb                    ║"
echo "║                                                            ║"
echo "║  2. Para executar a aplicação:                            ║"
echo "║     streamlit run app.py                                  ║"
echo "║                                                            ║"
echo "║  3. Para avaliar o modelo:                                ║"
echo "║     python evaluate_model.py                              ║"
echo "║                                                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
