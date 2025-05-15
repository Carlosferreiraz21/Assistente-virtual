WELCOME_MESSAGE = """
Olá! Eu sou seu assistente financeiro pessoal. 
Posso ajudar você a controlar suas finanças de forma simples e eficiente.

Use os comandos:
/receita VALOR DESCRIÇÃO - Para registrar uma receita
/despesa VALOR DESCRIÇÃO - Para registrar uma despesa
/relatorio - Para ver seu relatório financeiro
/help - Para ver esta mensagem novamente

Ou use os botões abaixo para acessar as funcionalidades! 👇
"""

HELP_MESSAGE = WELCOME_MESSAGE

INCOME_REGISTERED = "✅ Receita de R$ {amount:.2f} registrada com sucesso!"

EXPENSE_REGISTERED = "📝 Despesa de R$ {amount:.2f} registrada com sucesso!"

REPORT_GENERATED = """
📊 Relatório Financeiro:

Receitas Totais: {report[total_income]}
Despesas Totais: {report[total_expenses]}
Saldo Atual: {report[balance]}
"""

NET_PROFIT_MESSAGE = """
💰 Lucro Líquido:
{profit}

Este é seu lucro após descontar todas as despesas!
"""

GROSS_PROFIT_MESSAGE = """
📈 Lucro Bruto:
{profit}

Este é o total de suas receitas, sem descontar as despesas.
"""

CURRENT_BALANCE_MESSAGE = """
💵 Saldo Atual:
{balance}

Este é o saldo disponível em sua conta.
""" 