from transformers import pipeline
from utils.text_processing import preprocess_text

classifier = pipeline(
    "text-classification",
    model="neuralmind/bert-base-portuguese-cased",
    return_all_scores=True
)

INTENT_MAPPINGS = {
    "receita": "income",
    "entrada": "income",
    "ganho": "income",
    "despesa": "expense",
    "gasto": "expense",
    "pagamento": "expense"
}

def classify_intent(text: str) -> str:
    text = preprocess_text(text)
    
    for keyword, intent in INTENT_MAPPINGS.items():
        if keyword in text.lower():
            return intent
            
    # Fallback para classificação com BERT quando não há palavras-chave
    results = classifier(text)
    scores = results[0]
    return max(scores, key=lambda x: x['score'])['label'] 