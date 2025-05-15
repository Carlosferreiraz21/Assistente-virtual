from typing import Tuple
from database.registro import consultar_entradas, consultar_saidas

def calcular_totais(usuario_id: int) -> Tuple[float, float]:
    """
    Calcula os totais de entradas e saídas do usuário.
    
    Args:
        usuario_id: ID do usuário no Telegram
        
    Returns:
        Tuple[float, float]: Total de entradas e total de saídas
    """
    entradas = consultar_entradas(usuario_id)
    saidas = consultar_saidas(usuario_id)
    
    total_entradas = sum(e.valor for e in entradas) if entradas else 0
    total_saidas = sum(s.valor for s in saidas) if saidas else 0
    
    return total_entradas, total_saidas

def dica_inteligente(usuario_id: int) -> str:
    """
    Analisa os dados financeiros do usuário e gera uma dica personalizada
    baseada na margem de lucro.
    
    A margem de lucro é calculada como:
    margem = ((entradas - saídas) / entradas) * 100
    
    Args:
        usuario_id: ID do usuário no Telegram
        
    Returns:
        str: Mensagem com a dica personalizada baseada na análise
    """
    # Obtém os totais de entradas e saídas
    total_entradas, total_saidas = calcular_totais(usuario_id)
    
    # Se não houver entradas, retorna mensagem padrão
    if total_entradas == 0:
        return ("💡 Ainda não há registros suficientes para análise. "
                "Comece registrando suas entradas e saídas!")
    
    # Calcula a margem de lucro
    margem = ((total_entradas - total_saidas) / total_entradas) * 100
    
    # Formata os valores para exibição
    margem_formatada = f"{margem:.1f}%"
    entradas_formatadas = f"R$ {total_entradas:.2f}"
    saidas_formatadas = f"R$ {total_saidas:.2f}"
    
    # Define a dica com base na margem
    if margem < 10:
        dica = (
            f"⚠️ Sua margem de lucro está em {margem_formatada}, abaixo de 10%. "
            "Isso é um sinal de risco. Reveja seus custos e busque reduzir gastos desnecessários."
        )
    elif margem <= 25:
        dica = (
            f"🔎 Sua margem de lucro está em {margem_formatada}, entre 10% e 25%. "
            "Isso é aceitável, mas ainda pode melhorar. Foque em aumentar suas entradas "
            "ou renegociar despesas."
        )
    else:
        dica = (
            f"🎉 Excelente! Sua margem está em {margem_formatada}, acima de 25%. "
            "Isso indica uma boa saúde financeira. Continue nesse ritmo e invista com cautela."
        )
    
    # Monta o relatório completo
    return f"""
📊 Análise Financeira:
▪️ Total de Entradas: {entradas_formatadas}
▪️ Total de Saídas: {saidas_formatadas}
▪️ Margem de Lucro: {margem_formatada}

{dica}
""" 