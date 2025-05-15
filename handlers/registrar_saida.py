from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler
)

from database.registro import registrar_saida

# Estados da conversa
ESPERANDO_VALOR = 1

async def iniciar_registro_saida(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Inicia o modo de registro de saídas."""
    mensagem = "Ok! Vamos registrar suas despesas. Envie o valor e a categoria.\nEx: 50 mercado. Digite 'sair' para encerrar."
    
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.message.reply_text(mensagem)
    else:
        await update.message.reply_text(mensagem)
    
    return ESPERANDO_VALOR

async def processar_saida(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Processa cada mensagem de saída do usuário."""
    texto = update.message.text.lower()
    
    if texto == 'sair':
        await update.message.reply_text("Saindo do modo de registro de despesas.")
        return ConversationHandler.END
    
    try:
        # Divide a mensagem em valor e categoria
        partes = texto.split(maxsplit=1)
        if len(partes) != 2:
            raise ValueError("Formato inválido")
        
        valor = float(partes[0].replace(',', '.'))
        categoria = partes[1].strip()
        
        # Registra no banco de dados
        valor_registrado = registrar_saida(
            usuario_id=update.effective_user.id,
            valor=valor,
            categoria=categoria
        )
        
        if valor_registrado is not None:
            await update.message.reply_text(
                f"✅ Despesa de R${valor:.2f} registrada na categoria '{categoria}'. "
                "Envie mais uma ou digite 'sair'."
            )
        else:
            await update.message.reply_text(
                "❌ Erro ao registrar despesa. Tente novamente ou digite 'sair'."
            )
            
    except ValueError:
        await update.message.reply_text(
            "❌ Formato inválido! Use: valor categoria\n"
            "Exemplo: 50 mercado\n"
            "Digite 'sair' para encerrar."
        )
    
    return ESPERANDO_VALOR

async def cancelar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancela o registro de saídas."""
    await update.message.reply_text("Registro de despesas cancelado.")
    return ConversationHandler.END

# Handler principal para registro de saídas
registrar_saida_handler = ConversationHandler(
    entry_points=[
        CommandHandler('registrar_saida', iniciar_registro_saida),
        CallbackQueryHandler(iniciar_registro_saida, pattern='^registrar_saida$')
    ],
    states={
        ESPERANDO_VALOR: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, processar_saida)
        ]
    },
    fallbacks=[CommandHandler('cancelar', cancelar)]
) 