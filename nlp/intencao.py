from transformers import pipeline
from typing import Dict, List
import re
from unicodedata import normalize

# Inicializa o pipeline de classificação usando BERT em português
classificador = pipeline(
    task="text-classification",
    model="neuralmind/bert-base-portuguese-cased",
    return_all_scores=True
)

# Mapeamento de palavras-chave para intenções
PALAVRAS_CHAVE: Dict[str, List[str]] = {
    "registrar_entrada": [
        "receita", "entrada", "ganho", "receber", "ganhar", "salário",
        "rendimento", "renda", "depósito", "recebimento"
    ],
    "registrar_saida": [
        "despesa", "gasto", "saída", "pagar", "pagamento", "conta",
        "débito", "compra", "custo", "desembolso"
    ],
    "mostrar_lucro_liquido": [
        "lucro líquido", "lucro real", "ganho líquido", "rendimento líquido"
    ],
    "mostrar_lucro_bruto": [
        "lucro bruto", "receita bruta", "ganho bruto", "rendimento bruto"
    ],
    "mostrar_saldo": [
        "saldo", "disponível", "conta", "carteira", "balanço", "total"
    ],
    "gerar_relatorio": [
        "relatório", "resumo", "extrato", "balanço", "histórico", "movimentações"
    ],
    "dica_ia": [
        "dica", "ajuda", "sugestão", "conselho", "recomendação", "orientação"
    ]
}

def preprocessar_texto(texto: str) -> str:
    """
    Prepara o texto para análise removendo acentos e caracteres especiais.
    
    Args:
        texto: Texto a ser preprocessado
        
    Returns:
        Texto normalizado em minúsculas e sem acentos
    """
    texto = texto.lower()
    texto = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    texto = re.sub(r'[^\w\s]', ' ', texto)
    return texto.strip()

def verificar_palavras_chave(texto: str) -> str:
    """
    Verifica se o texto contém palavras-chave conhecidas.
    
    Args:
        texto: Texto preprocessado para análise
        
    Returns:
        Intenção correspondente às palavras-chave ou None se não encontrar
    """
    texto_prep = preprocessar_texto(texto)
    
    for intencao, palavras in PALAVRAS_CHAVE.items():
        for palavra in palavras:
            if preprocessar_texto(palavra) in texto_prep:
                return intencao
    
    return None

def interpretar_intencao(texto: str) -> str:
    """
    Interpreta a intenção do usuário a partir do texto fornecido.
    
    O processo acontece em duas etapas:
    1. Busca por palavras-chave conhecidas
    2. Se não encontrar palavras-chave, usa o modelo BERT para classificação
    
    Args:
        texto: Mensagem do usuário
        
    Returns:
        String identificando a intenção detectada ou "intencao_desconhecida"
    """
    # Primeira tentativa: verificar palavras-chave
    intencao = verificar_palavras_chave(texto)
    if intencao:
        return intencao
        
    # Segunda tentativa: usar modelo BERT
    try:
        resultado = classificador(texto)
        scores = resultado[0]
        
        # Mapeia as classes do modelo para nossas intenções
        # Nota: Este mapeamento precisa ser ajustado de acordo com as classes
        # que seu modelo específico foi treinado para reconhecer
        classe = max(scores, key=lambda x: x['score'])['label']
        
        # Mapeamento de exemplo (ajuste conforme necessário)
        mapeamento_classes = {
            "LABEL_0": "registrar_entrada",
            "LABEL_1": "registrar_saida",
            "LABEL_2": "mostrar_saldo",
            "LABEL_3": "gerar_relatorio",
            "LABEL_4": "dica_ia"
        }
        
        return mapeamento_classes.get(classe, "intencao_desconhecida")
        
    except Exception as e:
        print(f"Erro ao classificar texto: {e}")
        return "intencao_desconhecida" 