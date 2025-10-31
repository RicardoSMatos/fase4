"""
Aplicação Streamlit - Gerador de Histórias Interativas
Tech Challenge Fase 4 - FIAP
"""

import streamlit as st
import sys
from pathlib import Path
import random

sys.path.append(str(Path(__file__).parent))

from src.model import TextGenerator

# Dados de exemplo (serão movidos para sample_stories.py depois)
GENEROS = ["Ficção Científica", "Terror", "Romance", "Aventura", "Fantasia", "Mistério"]
TONS = ["Aventuroso", "Sombrio", "Romântico", "Humorístico", "Épico", "Melancólico"]

st.set_page_config(
    page_title="Gerador de Histórias",
    page_icon="�",
    layout="wide"
)

st.markdown("""
<style>
.main-header {font-size: 3rem; color: #FF4B4B; text-align: center;}
.story-card {background: #f0f2f6; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #FF4B4B;}
.story-box {background: #e3f2fd; padding: 2rem; border-radius: 10px; border-left: 5px solid #2196F3; line-height: 1.8;}
.prompt-box {background: #fff3e0; padding: 1rem; border-radius: 8px; border-left: 4px solid #ff9800;}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model(model_choice=None):
    """Carrega o modelo selecionado"""
    try:
        if model_choice:
            return TextGenerator(model_choice), None
        else:
            # Auto-detecta melhor modelo
            return TextGenerator(), None
    except Exception as e:
        return None, str(e)

def get_available_models():
    """Retorna modelos disponíveis"""
    return TextGenerator.get_available_models()

def construir_prompt(genero, personagens, cenario, tom):
    """Constrói o prompt otimizado para geração de história"""
    
    # Início com instrução clara
    prompt = f"Você é um escritor criativo especializado em {genero}.\n\n"
    
    prompt += "Escreva uma história original e envolvente com:\n\n"
    
    prompt += f"GÊNERO: {genero}\n"
    
    if personagens:
        prompt += f"PERSONAGENS: {personagens}\n"
        prompt += "→ Desenvolva suas personalidades através de ações e diálogos.\n"
    
    if cenario:
        prompt += f"\nCENÁRIO: {cenario}\n"
        prompt += "→ Descreva o ambiente com detalhes sensoriais.\n"
    
    if tom:
        prompt += f"\nTOM: {tom}\n"
        prompt += "→ Mantenha este tom consistente ao longo da narrativa.\n"
    
    prompt += "\nREGRAS:\n"
    prompt += "✓ Mantenha foco no tema\n"
    prompt += "✓ Use diálogos naturais\n"
    prompt += "✓ Mostre, não apenas conte\n"
    prompt += "✓ Evite repetições\n"
    prompt += "✓ Crie tensão narrativa\n"
    
    prompt += "\n---\n\nHistória:\n\n"
    
    return prompt

def gerar_historia(generator, genero, personagens="", cenario="", tom="", tamanho="media", temp=0.9, inicio=""):
    """Gera história baseada nos parâmetros fornecidos"""
    tamanhos = {"curta": 300, "media": 600, "longa": 900}
    max_len = tamanhos.get(tamanho, 600)
    
    if inicio:
        # Modo continuação MELHORADO
        prompt = f"Você é um escritor criativo especializado em {genero}.\n\n"
        prompt += "TAREFA: Continue esta história de forma criativa e coerente.\n\n"
        prompt += f"GÊNERO: {genero}\n"
        if tom:
            prompt += f"TOM: {tom}\n"
        prompt += "\nREGRAS:\n"
        prompt += "✓ Mantenha o estilo e contexto do início\n"
        prompt += "✓ Desenvolva a trama naturalmente\n"
        prompt += "✓ Adicione elementos do gênero\n"
        prompt += "✓ Evite repetir o que já foi dito\n"
        prompt += "✓ Crie tensão e interesse\n\n"
        prompt += f"---\n\nINÍCIO DA HISTÓRIA:\n{inicio}\n\n"
        prompt += "CONTINUE A HISTÓRIA:\n\n"
    else:
        # Modo guiado
        prompt = construir_prompt(genero, personagens, cenario, tom)
    
    historias = generator.generate(
        prompt=prompt,
        max_length=len(prompt.split()) + max_len,
        temperature=temp,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.3,
        no_repeat_ngram_size=3,
        num_return_sequences=1
    )
    
    historia = historias[0]
    
    # Extrai apenas a história gerada
    if "História:" in historia:
        historia = historia.split("História:")[-1].strip()
    else:
        historia = historia[len(prompt):].strip()
    
    return historia

def main():
    st.markdown('<h1 class="main-header">📚 Gerador de Histórias Interativas</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#666;">GPT-2 Portuguese | FIAP Tech Challenge Fase 4</p>', unsafe_allow_html=True)
    
    # Obtém modelos disponíveis
    available_models = get_available_models()
    
    # Seletor de modelo na sidebar (inicializado antes do carregamento)
    with st.sidebar:
        st.header("🤖 Seleção de Modelo")
        
        model_names = list(available_models.keys())
        selected_model_name = st.selectbox(
            "Escolha o modelo:",
            model_names,
            help="Fine-tuned = treinado com suas histórias (melhor) | GPT-2 = modelo base"
        )
        selected_model_path = available_models[selected_model_name]
        
        # Mostra informações do modelo selecionado
        if "Fine-tuned" in selected_model_name:
            st.success("✅ Usando modelo personalizado!")
            st.caption("Este modelo foi treinado especificamente com histórias criativas.")
        else:
            st.warning("⚠️ Usando modelo base")
            st.caption("Para melhores resultados, treine o modelo com: `python train_model_script.py`")
        
        st.markdown("---")
    
    # Carrega modelo selecionado
    with st.spinner(f"Carregando {selected_model_name}..."):
        generator, error = load_model(selected_model_path)
    
    if error:
        st.error(f"Erro ao carregar modelo: {error}")
        st.info("💡 Certifique-se de que o modelo está instalado: `pip install transformers torch`")
        return
    
    st.success(f"✨ {selected_model_name} carregado! Pronto para criar histórias incríveis.")
    
    with st.sidebar:
        st.header("⚙️ Configurações")
        
        tamanho = st.select_slider(
            "📏 Tamanho da História", 
            ["curta", "media", "longa"], 
            value="media",
            help="Curta: ~500 palavras | Média: ~1000 palavras | Longa: ~1500 palavras"
        )
        
        with st.expander("🎨 Configurações Avançadas de Criatividade"):
            temp = st.slider(
                "🌡️ Temperature (Criatividade)", 
                0.5, 1.3, 0.9, 0.05,
                help="🔥 Maior = mais surpreendente e criativo | ❄️ Menor = mais previsível e coerente"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if temp < 0.7:
                    st.caption("❄️ Conservador")
                elif temp < 0.9:
                    st.caption("⚖️ Balanceado")
                elif temp < 1.1:
                    st.caption("✨ Criativo")
                else:
                    st.caption("🔥 Muito Criativo")
            
            with col2:
                st.caption("💡 Recomendado: 0.85-0.95")
            
            st.markdown("---")
            
            st.markdown("**Dicas por gênero:**")
            st.caption("• Ficção Científica: 0.90-1.0 (mais criativo)")
            st.caption("• Terror: 0.85-0.95 (balanceado)")
            st.caption("• Romance: 0.80-0.90 (mais focado)")
            st.caption("• Aventura: 0.90-1.0 (mais criativo)")
        
        st.markdown("---")
        
        # Info dinâmica baseada no modelo
        if "Fine-tuned" in selected_model_name or "🎯" in selected_model_name:
            st.success("**✅ Modelo Otimizado para Histórias**")
            st.caption("Fine-tuned especializado em narrativas criativas")
        elif "BLOOM" in selected_model_name or "🌸" in selected_model_name or "🌺" in selected_model_name:
            st.info("**🌸 BLOOM - Modelo Multilíngue de Alta Qualidade**")
            if "560M" in selected_model_name:
                st.caption("560M parâmetros | Ótimo balanço qualidade/velocidade")
            else:
                st.caption("1.1B parâmetros | Máxima qualidade (mais lento)")
        elif "mGPT" in selected_model_name or "🌍" in selected_model_name:
            st.info("**🌍 mGPT - Modelo Multilíngue**")
            st.caption("1.3B parâmetros | Boa qualidade para português")
        else:
            st.warning("**📝 GPT-2 Portuguese Small**")
            st.caption("124M parâmetros | Rápido mas qualidade limitada")
            st.caption("⚠️ Recomendado: Use BLOOM ou treine fine-tuned")
        
        if st.button("🗑️ Limpar Tudo"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    tab1, tab2, tab3 = st.tabs(["✨ Criar História", "📚 Exemplos", "📊 Estatísticas"])
    
    with tab1:
        modo = st.radio(
            "Como deseja criar sua história?", 
            ["🎯 Geração Guiada", "✍️ Continuação Criativa", "🎲 Geração Livre"], 
            horizontal=True,
            help="Guiada: Controle total | Continuação: Co-crie com o modelo | Livre: Surpresa total"
        )
        
        st.markdown("---")
        
        if modo == "🎯 Geração Guiada":
            st.markdown("### Defina os elementos da sua história")
            
            col1, col2 = st.columns(2)
            
            with col1:
                genero = st.selectbox(
                    "📚 Gênero Literário",
                    GENEROS,
                    help="Escolha o gênero que define o estilo da história"
                )
                
                personagens = st.text_area(
                    "👥 Personagens (opcional)",
                    placeholder="Ex: Ana: cientista corajosa, Pedro: piloto experiente",
                    height=100,
                    help="Descreva os personagens principais e suas características"
                )
            
            with col2:
                tom = st.selectbox(
                    "🎭 Tom da Narrativa",
                    TONS,
                    help="Define a atmosfera e o sentimento da história"
                )
                
                cenario = st.text_area(
                    "🌍 Cenário (opcional)",
                    placeholder="Ex: Estação espacial abandonada em 2089, Floresta amazônica à noite",
                    height=100,
                    help="Descreva onde e quando a história acontece"
                )
            
            st.markdown("---")
            
            # Preview do prompt
            with st.expander("👁️ Ver Prompt que será usado"):
                preview_prompt = construir_prompt(genero, personagens or "Personagens surpresa", cenario or "Cenário surpresa", tom)
                st.markdown(f'<div class="prompt-box"><pre>{preview_prompt}</pre></div>', unsafe_allow_html=True)
            
            if st.button("✨ Gerar História", type="primary", key="gerar_guiada"):
                if not genero:
                    st.warning("⚠️ Selecione pelo menos um gênero!")
                else:
                    with st.spinner("📝 Criando sua história... Isso pode levar alguns segundos."):
                        try:
                            historia = gerar_historia(
                                generator, 
                                genero, 
                                personagens, 
                                cenario, 
                                tom, 
                                tamanho, 
                                temp
                            )
                            
                            st.session_state.historia_atual = {
                                'genero': genero,
                                'personagens': personagens,
                                'cenario': cenario,
                                'tom': tom,
                                'historia': historia,
                                'prompt': construir_prompt(genero, personagens, cenario, tom)
                            }
                            st.session_state.total_historias = st.session_state.get('total_historias', 0) + 1
                            st.success("✅ História gerada com sucesso!")
                        except Exception as e:
                            st.error(f"❌ Erro ao gerar história: {e}")
        
        elif modo == "✍️ Continuação Criativa":
            st.markdown("### Comece a história e o modelo continua")
            
            genero = st.selectbox(
                "📚 Gênero",
                GENEROS,
                help="Ajuda o modelo a entender o estilo"
            )
            
            inicio = st.text_area(
                "✍️ Escreva o início da história",
                placeholder="Era uma vez, em uma cidade que nunca dormia...",
                height=150,
                help="Escreva as primeiras frases. O modelo continuará de forma criativa!"
            )
            
            if st.button("🚀 Continuar História", type="primary", key="gerar_continuacao"):
                if not inicio or len(inicio) < 20:
                    st.warning("⚠️ Escreva pelo menos algumas frases para começar!")
                else:
                    with st.spinner("📝 Continuando sua história..."):
                        try:
                            historia = gerar_historia(
                                generator,
                                genero,
                                inicio=inicio,
                                tamanho=tamanho,
                                temp=temp
                            )
                            
                            st.session_state.historia_atual = {
                                'genero': genero,
                                'inicio': inicio,
                                'historia': historia,
                                'modo': 'continuacao'
                            }
                            st.session_state.total_historias = st.session_state.get('total_historias', 0) + 1
                            st.success("✅ História continuada!")
                        except Exception as e:
                            st.error(f"❌ Erro: {e}")
        
        else:  # Geração Livre
            st.markdown("### Deixe o modelo criar tudo")
            st.info("🎲 O modelo escolherá personagens, cenário e desenvolvimento aleatoriamente!")
            
            genero = st.selectbox(
                "📚 Apenas escolha o gênero",
                GENEROS
            )
            
            # Opção de tema opcional
            tema_livre = st.text_input(
                "🎨 Tema ou palavra-chave (opcional)",
                placeholder="Ex: robôs, oceano, família, mistério...",
                help="Deixe em branco para total liberdade criativa"
            )
            
            if st.button("🎲 Gerar História Aleatória", type="primary", key="gerar_livre"):
                with st.spinner("🎨 Criando algo completamente novo..."):
                    try:
                        # Cria prompt para geração livre
                        prompt_livre = f"Você é um escritor criativo especializado em {genero}.\n\n"
                        prompt_livre += f"TAREFA: Escreva uma história original e surpreendente de {genero}.\n\n"
                        
                        if tema_livre:
                            prompt_livre += f"TEMA SUGERIDO: {tema_livre}\n\n"
                        
                        prompt_livre += "DIRETRIZES:\n"
                        prompt_livre += "✓ Invente personagens únicos e interessantes\n"
                        prompt_livre += "✓ Crie um cenário vívido e original\n"
                        prompt_livre += "✓ Desenvolva uma trama envolvente\n"
                        prompt_livre += "✓ Use elementos típicos do gênero\n"
                        prompt_livre += "✓ Seja criativo e surpreendente\n"
                        prompt_livre += "✓ Mantenha coerência narrativa\n\n"
                        prompt_livre += "---\n\nHistória:\n\n"
                        
                        # Gera com prompt otimizado
                        historias = generator.generate(
                            prompt=prompt_livre,
                            max_length=len(prompt_livre.split()) + 600,
                            temperature=temp,
                            top_k=50,
                            top_p=0.95,
                            repetition_penalty=1.3,
                            no_repeat_ngram_size=3,
                            num_return_sequences=1
                        )
                        
                        historia = historias[0]
                        
                        # Extrai apenas a história
                        if "História:" in historia:
                            historia = historia.split("História:")[-1].strip()
                        else:
                            historia = historia[len(prompt_livre):].strip()
                        
                        st.session_state.historia_atual = {
                            'genero': genero,
                            'tema': tema_livre if tema_livre else "Livre",
                            'historia': historia,
                            'modo': 'livre'
                        }
                        st.session_state.total_historias = st.session_state.get('total_historias', 0) + 1
                        st.success("✅ História criada!")
                    except Exception as e:
                        st.error(f"❌ Erro: {e}")
        
        # Exibir história gerada
        if 'historia_atual' in st.session_state:
            h = st.session_state.historia_atual
            
            st.markdown("---")
            st.markdown("## � Sua História")
            
            # Metadados
            col1, col2, col3 = st.columns(3)
            col1.metric("📚 Gênero", h.get('genero', 'N/A'))
            
            if h.get('tom'):
                col2.metric("🎭 Tom", h['tom'])
            
            palavras = len(h['historia'].split())
            col3.metric("📝 Palavras", palavras)
            
            # Se tiver prompt detalhado
            if h.get('prompt'):
                with st.expander("ℹ️ Elementos da História"):
                    if h.get('personagens'):
                        st.markdown(f"**👥 Personagens:** {h['personagens']}")
                    if h.get('cenario'):
                        st.markdown(f"**🌍 Cenário:** {h['cenario']}")
                    if h.get('tom'):
                        st.markdown(f"**🎭 Tom:** {h['tom']}")
            
            # História
            st.markdown(f'<div class="story-box">{h["historia"]}</div>', unsafe_allow_html=True)
            
            # Ações
            col1, col2, col3 = st.columns([2, 2, 1])
            
            with col1:
                st.download_button(
                    "💾 Baixar História",
                    f"Gênero: {h.get('genero')}\n\n{h['historia']}",
                    "minha_historia.txt",
                    mime="text/plain"
                )
            
            with col2:
                feedback = st.radio(
                    "Como ficou?",
                    ["⭐ Excelente", "👍 Boa", "😐 Regular", "👎 Ruim"],
                    horizontal=True,
                    key="feedback_historia"
                )
                
                if feedback:
                    if 'feedbacks' not in st.session_state:
                        st.session_state.feedbacks = []
                    st.session_state.feedbacks.append(feedback)
    
    with tab2:
        st.markdown("### � Histórias de Exemplo")
        st.info("Em breve: Exemplos de histórias geradas em diferentes gêneros")
        
        # Exemplos temporários
        exemplos = [
            {
                "genero": "Ficção Científica",
                "personagens": "Ana (cientista), ARIA (IA)",
                "cenario": "Estação espacial em Marte, 2089",
                "historia": "Ana olhou pela janela transparente do laboratório. Marte estendia-se vermelho e silencioso abaixo dela. 'ARIA, status dos experimentos', ela disse. A voz suave da inteligência artificial respondeu: 'Anomalia detectada no Setor 7. Sinais de vida microbiana não catalogada.' O coração de Ana acelerou. Após três anos em Marte, finalmente..."
            },
            {
                "genero": "Terror",
                "personagens": "Lucas (estudante)",
                "cenario": "Casa abandonada, noite chuvosa",
                "historia": "O relâmpago iluminou brevemente a sala empoeirada. Lucas engoliu em seco. Não deveria estar ali. A velha casa dos Almeida estava abandonada há décadas, desde que... 'Não pense nisso', ele murmurou. O som de passos no andar de cima o fez congelar. Impossível. Estava sozinho... não estava?"
            },
            {
                "genero": "Romance",
                "personagens": "Júlia (professora), Rafael (músico)",
                "cenario": "Café parisiense, outono",
                "historia": "As folhas douradas dançavam no vento enquanto Júlia observava pela vidraça do café. Cinco anos desde que havia deixado São Paulo. Cinco anos tentando esquecer. A campainha tocou. Ela nem se virou. Até ouvir aquela voz conhecida: 'Ainda toma café com leite e duas colheres de açúcar?'"
            }
        ]
        
        for i, ex in enumerate(exemplos):
            with st.expander(f"📖 {ex['genero']} - {ex.get('personagens', 'Personagens variados')}"):
                st.markdown(f"**Gênero:** {ex['genero']}")
                if ex.get('personagens'):
                    st.markdown(f"**Personagens:** {ex['personagens']}")
                if ex.get('cenario'):
                    st.markdown(f"**Cenário:** {ex['cenario']}")
                st.markdown("---")
                st.markdown(ex['historia'])
    
    with tab3:
        st.markdown("### 📊 Estatísticas de Uso")
        
        total = st.session_state.get('total_historias', 0)
        
        if total > 0:
            col1, col2, col3 = st.columns(3)
            col1.metric("📖 Histórias Geradas", total)
            
            if 'historia_atual' in st.session_state:
                palavras_total = len(st.session_state.historia_atual['historia'].split())
                col2.metric("📝 Palavras na Última História", palavras_total)
                tempo_leitura = palavras_total // 200  # ~200 palavras/min
                col3.metric("⏱️ Tempo de Leitura", f"~{tempo_leitura} min")
            
            st.markdown("---")
            
            if 'feedbacks' in st.session_state and st.session_state.feedbacks:
                st.markdown("### 🌟 Feedback das Histórias")
                feedback_counts = {}
                for f in st.session_state.feedbacks:
                    feedback_counts[f] = feedback_counts.get(f, 0) + 1
                
                for feedback, count in feedback_counts.items():
                    st.markdown(f"{feedback}: {count}")
        else:
            st.info("👆 Crie sua primeira história para ver as estatísticas!")
        
        st.markdown("---")
        st.markdown("### 💡 Dicas")
        st.markdown("""
        - **Seja específico** nos personagens para histórias mais interessantes
        - **Temperature maior** (1.1-1.3) = mais criativo, mas pode perder coerência
        - **Temperature menor** (0.7-0.9) = mais focado e coerente
        - **Modo Continuação** é ótimo para desenvolver suas próprias ideias
        - **Geração Livre** te surpreende com combinações inesperadas!
        """)
    
    st.markdown("---")
    st.markdown("<div style='text-align:center;color:#666;'><p>🎓 Tech Challenge Fase 4 - FIAP | ML Engineering</p></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    if 'total_historias' not in st.session_state:
        st.session_state.total_historias = 0
    main()
