#!/usr/bin/env python3
"""
Script de treinamento do modelo GPT-2 para geração de histórias
Alternativa ao notebook train_model.ipynb
"""

import sys
from pathlib import Path

print("="*80)
print("TREINAMENTO GPT-2 PARA GERAÇÃO DE HISTÓRIAS")
print("Tech Challenge Fase 4 - FIAP")
print("="*80 + "\n")

# Verifica lzma
print("🔍 Verificando ambiente...")
try:
    import lzma
    print("✅ Módulo lzma disponível")
except ImportError:
    print("❌ ERRO: Módulo lzma não encontrado!")
    print("\nSoluções:")
    print("1. Use Python do Homebrew:")
    print("   brew install python@3.11")
    print("   /opt/homebrew/bin/python3.11 train_model_script.py")
    print("\n2. Use Google Colab (mais fácil)")
    sys.exit(1)

# Verifica e instala pacotes
print("\n📦 Verificando dependências...")
pacotes_necessarios = {
    'transformers': 'transformers',
    'datasets': 'datasets',
    'accelerate': 'accelerate',
    'torch': 'torch',
    'pandas': 'pandas',
    'matplotlib': 'matplotlib',
    'seaborn': 'seaborn',
    'tqdm': 'tqdm',
    'sklearn': 'scikit-learn'
}

pacotes_faltando = []
for modulo, pacote_pip in pacotes_necessarios.items():
    try:
        __import__(modulo)
    except ImportError:
        pacotes_faltando.append(pacote_pip)

if pacotes_faltando:
    print(f"❌ Faltam pacotes: {', '.join(pacotes_faltando)}")
    print(f"\nInstale com: pip install {' '.join(pacotes_faltando)}")
    sys.exit(1)

print("✅ Todas as dependências instaladas\n")

# Imports
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    DataCollatorForLanguageModeling
)
from datasets import Dataset

sys.path.append(str(Path.cwd()))
from data.sample_stories import STORIES_DATASET, format_story_for_training

# Configurações
MODEL_NAME = "pierreguillou/gpt2-small-portuguese"
OUTPUT_DIR = "./models/fine_tuned_gpt2_story_generator"
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"🖥️ Dispositivo: {device}")
if device == "cpu":
    print("⚠️  Treino sem GPU vai demorar ~1-3 horas")
    print("💡 Dica: Use Google Colab para GPU gratuita\n")

# Carrega modelo
print(f"📥 Carregando modelo: {MODEL_NAME}")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = model.config.eos_token_id

model.to(device)
print(f"✅ Modelo carregado ({model.num_parameters():,} parâmetros)\n")

# Prepara dataset
print(f"📚 Preparando dataset ({len(STORIES_DATASET)} histórias)...")
formatted_stories = [{'text': format_story_for_training(s)} for s in STORIES_DATASET]
dataset = Dataset.from_list(formatted_stories)
dataset = dataset.train_test_split(test_size=0.2, seed=42)

def tokenize_function(examples):
    return tokenizer(
        examples['text'],
        truncation=True,
        max_length=1024,
        padding='max_length',
        return_tensors='pt'
    )

tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=['text'])
print(f"✅ Dataset pronto (treino: {len(dataset['train'])}, validação: {len(dataset['test'])})\n")

# Configuração de treino
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=5,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=5e-5,
    warmup_steps=500,
    logging_dir='./logs',
    logging_steps=50,
    eval_strategy="steps",
    eval_steps=200,
    save_strategy="steps",
    save_steps=200,
    save_total_limit=3,
    fp16=True if device == "cuda" else False,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    report_to="none",
    seed=42
)

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['test'],
    data_collator=data_collator,
)

# Treina
print("🚀 Iniciando treinamento...")
print("⏰ Tempo estimado: 5-15 min (GPU) ou 1-3h (CPU)\n")

train_result = trainer.train()

print("\n" + "="*80)
print("✅ TREINO CONCLUÍDO!")
print("="*80)
print(f"Loss final: {train_result.training_loss:.4f}\n")

# Avalia
print("📊 Avaliando modelo...")
eval_results = trainer.evaluate()
for key, value in eval_results.items():
    print(f"  • {key}: {value:.4f}")

# Salva
print(f"\n💾 Salvando modelo em: {OUTPUT_DIR}")
model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print("✅ Modelo salvo com sucesso!")

# Teste rápido
print("\n🧪 Teste rápido de geração:")
prompt = """Gênero: Ficção Científica
Personagens: Dr. Silva
Cenário: Estação espacial
Tom: Aventuroso

História: """

inputs = tokenizer(prompt, return_tensors='pt').to(device)
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_length=len(inputs['input_ids'][0]) + 200,
        temperature=0.9,
        do_sample=True
    )
historia = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(historia[:300] + "...\n")

print("="*80)
print("🎉 PROCESSO COMPLETO!")
print(f"Modelo salvo em: {OUTPUT_DIR}")
print("="*80)
