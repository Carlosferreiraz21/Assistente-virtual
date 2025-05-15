def format_currency(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", ".")

def format_percentage(value: float) -> str:
    return f"{value:.1f}%" 