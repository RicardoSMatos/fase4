"""
Classe para carregar e gerenciar o modelo de geração de texto.
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from typing import Optional
import os


class TextGenerator:
    """
    Classe para gerenciar o modelo de geração de texto.
    """
    
    def __init__(
        self, 
        model_name: Optional[str] = None,
        device: Optional[str] = None
    ):
        """
        Inicializa o gerador de texto.
        
        Args:
            model_name: Nome ou caminho do modelo (None = auto-detecta)
            device: Dispositivo para executar o modelo (cuda/cpu)
        """
        # Auto-detecta melhor modelo disponível
        if model_name is None:
            model_name = self._detect_best_model()
        
        self.model_name = model_name
        
        # Determina o dispositivo
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
            
        print(f"🚀 Carregando modelo: {model_name}")
        print(f"💻 Dispositivo: {self.device}")
        
        # Carrega tokenizer e modelo
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()
        
        # Configura pad token se não existir
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
            
        print("✅ Modelo carregado com sucesso!")
    
    @staticmethod
    def _detect_best_model() -> str:
        """
        Detecta o melhor modelo disponível.
        
        Prioridade:
        1. Modelo fine-tuned local (se existir)
        2. BLOOM 560M (melhor para geração criativa multilíngue)
        3. GPT-2 Portuguese Small (fallback rápido)
        
        Returns:
            Nome ou caminho do modelo
        """
        # Verifica se existe modelo fine-tuned local
        local_model = "./models/fine_tuned_gpt2_story_generator"
        if os.path.exists(local_model) and os.path.isdir(local_model):
            config_file = os.path.join(local_model, "config.json")
            if os.path.exists(config_file):
                print(f"🎯 Modelo fine-tuned encontrado: {local_model}")
                return local_model
        
        # Usa BLOOM por padrão (melhor que GPT-2 Small)
        print("⚠️ Modelo fine-tuned não encontrado. Usando modelo pré-treinado...")
        
        # BLOOM 560M - melhor balanço qualidade/velocidade
        default_model = "bigscience/bloom-560m"
        
        print(f"📥 Usando modelo: {default_model}")
        print("💡 BLOOM é um modelo multilíngue de alta qualidade treinado pela BigScience")
        print("   Suporta português e é melhor para geração criativa que GPT-2 Small")
        return default_model
    
    @staticmethod
    def get_available_models():
        """
        Retorna lista de modelos disponíveis para seleção.
        
        Returns:
            Dict com modelos disponíveis e validados
        """
        models = {}
        
        # Verifica modelo fine-tuned
        local_model = "./models/fine_tuned_gpt2_story_generator"
        if os.path.exists(local_model) and os.path.isdir(local_model):
            config_file = os.path.join(local_model, "config.json")
            if os.path.exists(config_file):
                models["🎯 Fine-tuned GPT-2 (Treinado em Histórias) - MELHOR"] = local_model
        
        # Modelos VALIDADOS do HuggingFace para geração criativa
        
        # GPT-2 Portuguese Small (baseline)
        models["📝 GPT-2 Portuguese Small (124M) - Rápido"] = "pierreguillou/gpt2-small-portuguese"
        
        # BLOOM - Modelo grande multilíngue com português (RECOMENDADO)
        models["🌸 BLOOM 560M (Multilíngue) - Melhor Qualidade"] = "bigscience/bloom-560m"
        
        # BLOOM maior
        models["� BLOOM 1B1 (Multilíngue) - Alta Qualidade (Lento)"] = "bigscience/bloom-1b1"
        
        # Alternativa: mGPT (multilíngue incluindo português)
        models["🌍 mGPT 1.3B (Multilíngue) - Boa Qualidade"] = "ai-forever/mGPT"
        
        return models
    
    def generate(
        self,
        prompt: str,
        max_length: int = 200,
        temperature: float = 0.9,
        top_k: int = 50,
        top_p: float = 0.95,
        repetition_penalty: float = 1.3,
        num_return_sequences: int = 1,
        do_sample: bool = True,
        no_repeat_ngram_size: int = 3
    ) -> list:
        """
        Gera texto a partir de um prompt.
        
        Args:
            prompt: Texto inicial
            max_length: Comprimento máximo do texto gerado
            temperature: Controla a aleatoriedade (maior = mais criativo) [0.8-1.1 ideal]
            top_k: Número de tokens candidatos [40-60 ideal]
            top_p: Probabilidade acumulada (nucleus sampling) [0.90-0.95 ideal]
            repetition_penalty: Penalidade para repetições [1.2-1.5 ideal]
            num_return_sequences: Número de sequências a gerar
            do_sample: Se True, usa amostragem; se False, usa greedy decoding
            no_repeat_ngram_size: Evita repetição de n-gramas (3 = trigrams)
            
        Returns:
            Lista de textos gerados
        """
        # Tokeniza o prompt
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512
        ).to(self.device)
        
        # Gera o texto
        with torch.no_grad():
            outputs = self.model.generate(
                inputs.input_ids,
                max_length=max_length,
                temperature=temperature,
                top_k=top_k,
                top_p=top_p,
                repetition_penalty=repetition_penalty,
                num_return_sequences=num_return_sequences,
                do_sample=do_sample,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
                attention_mask=inputs.attention_mask,
                no_repeat_ngram_size=no_repeat_ngram_size
            )
        
        # Decodifica os resultados
        generated_texts = []
        for output in outputs:
            text = self.tokenizer.decode(output, skip_special_tokens=True)
            generated_texts.append(text)
        
        return generated_texts
    
    def save_model(self, output_dir: str):
        """
        Salva o modelo e tokenizer.
        
        Args:
            output_dir: Diretório de saída
        """
        os.makedirs(output_dir, exist_ok=True)
        self.model.save_pretrained(output_dir)
        self.tokenizer.save_pretrained(output_dir)
        print(f"✅ Modelo salvo em: {output_dir}")
    
    @classmethod
    def from_pretrained(cls, model_path: str, device: Optional[str] = None):
        """
        Carrega um modelo salvo localmente.
        
        Args:
            model_path: Caminho do modelo
            device: Dispositivo para executar o modelo
            
        Returns:
            Instância de TextGenerator
        """
        return cls(model_name=model_path, device=device)
