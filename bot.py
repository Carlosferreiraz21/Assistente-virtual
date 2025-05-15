import os
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

from handlers.finance_handlers import (
    register_income, 
    register_expense, 
    generate_report,
    show_net_profit,
    show_gross_profit,
    show_current_balance
)
from handlers.general_handlers import start, help_command
from handlers.registrar_entrada import registrar_entrada_handler
from handlers.registrar_saida import registrar_saida_handler
from nlp.intencao import interpretar_intencao
from services.ia_dicas import dica_inteligente
from database.registro import (
    registrar_usuario,
    registrar_entrada,
    registrar_saida,
    consultar_entradas,
    consultar_saidas,
    registrar_meta,
    consultar_metas
)
from utils.config import TELEGRAM_TOKEN

load_dotenv()

def get_main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("📈 Registrar Entrada", callback_data="registrar_entrada"),
            InlineKeyboardButton("📉 Registrar Saída", callback_data="registrar_saida")
        ],
        [
            InlineKeyboardButton("💰 Lucro Líquido", callback_data="mostrar_lucro_liquido"),
            InlineKeyboardButton("📊 Lucro Bruto", callback_data="mostrar_lucro_bruto")
        ],
        [
            InlineKeyboardButton("💵 Saldo Atual", callback_data="mostrar_saldo"),
            InlineKeyboardButton("📑 Relatório", callback_data="gerar_relatorio")
        ],
        [
            InlineKeyboardButton("💡 Dica Inteligente", callback_data="dica_ia")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start - registra o usuário e mostra mensagem de boas-vindas"""
    user = update.effective_user
    
    # Registra o usuário no banco de dados
    registrar_usuario(user.id, user.first_name)
    
    welcome_message = f"""
Olá {user.first_name}! 👋 
Sou seu assistente financeiro pessoal.
Estou aqui para ajudar você a controlar suas finanças de forma simples e inteligente!

Escolha uma das opções abaixo para começar:
    """
    await update.message.reply_text(welcome_message, reply_markup=get_main_keyboard())

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manipula os callbacks dos botões"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    
    if query.data == "registrar_entrada":
        await iniciar_registro(update, context)
        return
    
    elif query.data == "registrar_saida":
        await iniciar_registro_saida(update, context)
        return
    
    elif query.data == "mostrar_lucro_liquido":
        entradas = consultar_entradas(user_id)
        saidas = consultar_saidas(user_id)
        total_entradas = sum(e.valor for e in entradas)
        total_saidas = sum(s.valor for s in saidas)
        lucro_liquido = total_entradas - total_saidas
        await query.message.reply_text(f"💰 Seu lucro líquido é: R$ {lucro_liquido:.2f}")
    
    elif query.data == "mostrar_lucro_bruto":
        entradas = consultar_entradas(user_id)
        total_entradas = sum(e.valor for e in entradas)
        await query.message.reply_text(f"📊 Seu lucro bruto é: R$ {total_entradas:.2f}")
    
    elif query.data == "mostrar_saldo":
        entradas = consultar_entradas(user_id)
        saidas = consultar_saidas(user_id)
        saldo = sum(e.valor for e in entradas) - sum(s.valor for s in saidas)
        await query.message.reply_text(f"💵 Seu saldo atual é: R$ {saldo:.2f}")
    
    elif query.data == "gerar_relatorio":
        entradas = consultar_entradas(user_id)
        saidas = consultar_saidas(user_id)
        total_entradas = sum(e.valor for e in entradas)
        total_saidas = sum(s.valor for s in saidas)
        saldo = total_entradas - total_saidas
        
        report = f"""
📊 Relatório Financeiro:

Receitas Totais: R$ {total_entradas:.2f}
Despesas Totais: R$ {total_saidas:.2f}
Saldo Atual: R$ {saldo:.2f}

Últimas 5 entradas:
{"".join(f'• R$ {e.valor:.2f} - {e.categoria} ({e.data.strftime("%d/%m/%Y")})\n' for e in entradas[:5])}

Últimas 5 saídas:
{"".join(f'• R$ {s.valor:.2f} - {s.categoria} ({s.data.strftime("%d/%m/%Y")})\n' for s in saidas[:5])}
"""
        await query.message.reply_text(report)
    
    elif query.data == "dica_ia":
        # Obtém a dica personalizada do serviço de IA
        dica = dica_inteligente(user_id)
        await query.message.reply_text(dica)
    
    await query.message.reply_text("O que mais posso fazer por você?", reply_markup=get_main_keyboard())

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Processa mensagens normais do usuário"""
    message = update.message.text
    user_id = update.effective_user.id
    intencao = interpretar_intencao(message)
    
    # Extrai valor e categoria da mensagem (implementação básica)
    try:
        palavras = message.split()
        valor = float(palavras[1]) if len(palavras) > 1 else 0
        categoria = " ".join(palavras[2:]) if len(palavras) > 2 else "Geral"
    except (ValueError, IndexError):
        valor = 0
        categoria = "Geral"
    
    if intencao == "registrar_entrada":
        if registrar_entrada(user_id, valor, categoria):
            await update.message.reply_text(f"✅ Receita de R$ {valor:.2f} registrada com sucesso!")
        else:
            await update.message.reply_text("❌ Erro ao registrar receita. Tente novamente.")
    
    elif intencao == "registrar_saida":
        valor_registrado = registrar_saida(user_id, valor, categoria)
        if valor_registrado is not None:
            await update.message.reply_text(f"📝 Despesa de R$ {valor_registrado:.2f} registrada com sucesso!")
        else:
            await update.message.reply_text("❌ Erro ao registrar despesa. Tente novamente.")
    
    else:
        await update.message.reply_text(
            "Como posso ajudar você hoje?",
            reply_markup=get_main_keyboard()
        )

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Comandos
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    
    # Handlers de registro
    app.add_handler(registrar_entrada_handler)
    app.add_handler(registrar_saida_handler)
    
    # Callbacks dos botões
    app.add_handler(CallbackQueryHandler(handle_button))
    
    # Mensagens normais
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot iniciado! Pressione Ctrl+C para encerrar.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main() 