import re
from unicodedata import normalize

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def extract_amount(text: str) -> float:
    matches = re.findall(r'R?\$?\s*(\d+(?:\.\d{1,2})?)', text)
    return float(matches[0]) if matches else 0.0 