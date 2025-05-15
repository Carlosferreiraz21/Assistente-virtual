from telegram import Update
from telegram.ext import ContextTypes
from services.finance_service import FinanceService
from responses.messages import (
    INCOME_REGISTERED, 
    EXPENSE_REGISTERED, 
    REPORT_GENERATED,
    NET_PROFIT_MESSAGE,
    GROSS_PROFIT_MESSAGE,
    CURRENT_BALANCE_MESSAGE
)

finance_service = FinanceService()

async def register_income(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = float(context.args[0])
        description = " ".join(context.args[1:]) if len(context.args) > 1 else "Receita"
        finance_service.register_income(amount, description)
        await update.message.reply_text(INCOME_REGISTERED.format(amount=amount))
    except (IndexError, ValueError):
        await update.message.reply_text("Por favor, use o formato: /receita VALOR DESCRIÇÃO")

async def register_expense(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = float(context.args[0])
        description = " ".join(context.args[1:]) if len(context.args) > 1 else "Despesa"
        finance_service.register_expense(amount, description)
        await update.message.reply_text(EXPENSE_REGISTERED.format(amount=amount))
    except (IndexError, ValueError):
        await update.message.reply_text("Por favor, use o formato: /despesa VALOR DESCRIÇÃO")

async def generate_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report = finance_service.generate_report()
    await update.message.reply_text(REPORT_GENERATED.format(report=report))

async def show_net_profit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    net_profit = finance_service.calculate_net_profit()
    await update.message.reply_text(NET_PROFIT_MESSAGE.format(profit=net_profit))

async def show_gross_profit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gross_profit = finance_service.calculate_gross_profit()
    await update.message.reply_text(GROSS_PROFIT_MESSAGE.format(profit=gross_profit))

async def show_current_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    balance = finance_service.get_current_balance()
    await update.message.reply_text(CURRENT_BALANCE_MESSAGE.format(balance=balance)) 