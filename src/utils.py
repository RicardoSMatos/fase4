"""
Funções utilitárias para sumarização de notícias.
"""

import re
from typing import List, Dict, Tuple
import numpy as np


def clean_generated_text(text: str, prompt: str = "") -> str:
    """
    Limpa e formata o texto gerado.
    
    Args:
        text: Texto gerado
        prompt: Prompt original (para remover se necessário)
        
    Returns:
        Texto limpo
    """
    # Remove prompt se ainda estiver no texto
    if prompt and text.startswith(prompt):
        text = text[len(prompt):].strip()
    
    # Remove espaços múltiplos
    text = re.sub(r'\s+', ' ', text)
    
    # Remove quebras de linha múltiplas
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()


def calculate_summary_quality(
    original_text: str,
    summary: str,
    reference_summary: str = None
) -> Dict[str, float]:
    """
    Calcula métricas de qualidade do resumo.
    
    Args:
        original_text: Texto original
        summary: Resumo gerado
        reference_summary: Resumo de referência (opcional)
        
    Returns:
        Dicionário com métricas de qualidade
    """
    palavras_orig = original_text.lower().split()
    palavras_sum = summary.lower().split()
    
    # Taxa de compressão
    compression = (1 - len(palavras_sum) / len(palavras_orig)) * 100 if len(palavras_orig) > 0 else 0
    
    # Cobertura de vocabulário
    palavras_orig_set = set(palavras_orig)
    palavras_sum_set = set(palavras_sum)
    overlap = len(palavras_orig_set.intersection(palavras_sum_set))
    coverage = (overlap / len(palavras_orig_set)) * 100 if len(palavras_orig_set) > 0 else 0
    
    metrics = {
        "original_words": len(palavras_orig),
        "summary_words": len(palavras_sum),
        "compression_rate": compression,
        "vocabulary_coverage": coverage,
        "unique_words_summary": len(palavras_sum_set)
    }
    
    # Se houver resumo de referência, calcula similaridade
    if reference_summary:
        palavras_ref = reference_summary.lower().split()
        palavras_ref_set = set(palavras_ref)
        similarity = len(palavras_sum_set.intersection(palavras_ref_set)) / len(palavras_ref_set.union(palavras_sum_set)) if palavras_ref_set else 0
        metrics["reference_similarity"] = similarity * 100
    
    return metrics


def format_summary_bullet_points(summary: str) -> List[str]:
    """
    Formata resumo em lista de bullet points.
    
    Args:
        summary: Texto do resumo
        
    Returns:
        Lista de frases/pontos principais
    """
    # Divide por pontos finais
    sentences = re.split(r'[.!?]', summary)
    
    # Limpa e filtra frases vazias
    bullets = []
    for sentence in sentences:
        cleaned = sentence.strip()
        if cleaned and len(cleaned) > 10:  # Ignora frases muito curtas
            bullets.append(cleaned)
    
    return bullets


def extract_key_entities(text: str) -> List[str]:
    """
    Extrai entidades-chave do texto (números, datas, nomes próprios).
    
    Args:
        text: Texto a analisar
        
    Returns:
        Lista de entidades encontradas
    """
    entities = []
    
    # Números com unidades (%, R$, etc)
    numbers = re.findall(r'\d+(?:[.,]\d+)?(?:\s*%|°C|km|kg|milhões?|bilhões?)?', text)
    entities.extend(numbers)
    
    # Datas
    dates = re.findall(r'\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4}', text)
    entities.extend(dates)
    
    # Palavras capitalizadas (possíveis nomes próprios)
    proper_nouns = re.findall(r'\b[A-Z][a-zà-ÿ]+(?:\s+[A-Z][a-zà-ÿ]+)*\b', text)
    entities.extend(proper_nouns[:5])  # Limita a 5
    
    return list(set(entities))


def calculate_diversity(texts: List[str]) -> Dict[str, float]:
    """
    Calcula métricas de diversidade para textos gerados.
    
    Args:
        texts: Lista de textos
        
    Returns:
        Dicionário com métricas de diversidade
    """
    if not texts:
        return {}
    
    all_words = []
    for text in texts:
        words = text.lower().split()
        all_words.extend(words)
    
    total_words = len(all_words)
    unique_words = len(set(all_words))
    
    metrics = {
        "total_words": total_words,
        "unique_words": unique_words,
        "lexical_diversity": unique_words / total_words if total_words > 0 else 0,
        "avg_text_length": np.mean([len(text) for text in texts]),
        "avg_word_length": np.mean([len(word) for word in all_words]) if all_words else 0
    }
    
    return metrics


def format_text_for_display(text: str, max_line_length: int = 80) -> str:
    """
    Formata texto para exibição melhorada.
    
    Args:
        text: Texto a formatar
        max_line_length: Comprimento máximo de linha
        
    Returns:
        Texto formatado
    """
    paragraphs = text.split('\n')
    formatted_paragraphs = []
    
    for paragraph in paragraphs:
        if not paragraph.strip():
            formatted_paragraphs.append("")
            continue
            
        words = paragraph.split()
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + 1 <= max_line_length:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                formatted_paragraphs.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            formatted_paragraphs.append(' '.join(current_line))
    
    return '\n'.join(formatted_paragraphs)


def extract_sentences(text: str, min_length: int = 10) -> List[str]:
    """
    Extrai sentenças de um texto.
    
    Args:
        text: Texto de entrada
        min_length: Comprimento mínimo de uma sentença
        
    Returns:
        Lista de sentenças
    """
    # Separadores de sentença
    sentences = re.split(r'[.!?]+', text)
    
    # Filtra sentenças muito curtas
    sentences = [s.strip() for s in sentences if len(s.strip()) >= min_length]
    
    return sentences


def compare_texts(text1: str, text2: str) -> Dict[str, float]:
    """
    Compara dois textos e retorna métricas de similaridade.
    
    Args:
        text1: Primeiro texto
        text2: Segundo texto
        
    Returns:
        Dicionário com métricas de comparação
    """
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    metrics = {
        "jaccard_similarity": len(intersection) / len(union) if union else 0,
        "common_words": len(intersection),
        "unique_to_text1": len(words1 - words2),
        "unique_to_text2": len(words2 - words1)
    }
    
    return metrics


def get_prompt_suggestions() -> List[str]:
    """
    Retorna sugestões de prompts para geração de texto.
    
    Returns:
        Lista de prompts sugeridos
    """
    prompts = [
        "Era uma vez em uma terra distante",
        "O dia começou de forma estranha quando",
        "Nas profundezas da floresta, havia",
        "A velha casa no topo da colina",
        "Ele nunca imaginou que aquele dia",
        "O segredo estava escondido há décadas",
        "Quando as estrelas se alinharam",
        "A carta chegou sem remetente",
        "No coração da cidade, um mistério",
        "A última pessoa que viu aquilo foi"
    ]
    return prompts
