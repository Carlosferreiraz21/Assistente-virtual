from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler
)

from database.registro import registrar_entrada

# Estados da conversa
ESPERANDO_VALOR = 1

async def iniciar_registro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Inicia o modo de registro de entradas."""
    mensagem = "Ok! Vamos registrar suas entradas. Envie o valor e a categoria.\nEx: 200 vendas. Digite 'sair' para encerrar."
    
    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.message.reply_text(mensagem)
    else:
        await update.message.reply_text(mensagem)
    
    return ESPERANDO_VALOR

async def processar_entrada(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Processa cada mensagem de entrada do usuário."""
    texto = update.message.text.lower()
    
    if texto == 'sair':
        await update.message.reply_text("Saindo do modo de entrada.")
        return ConversationHandler.END
    
    try:
        # Divide a mensagem em valor e categoria
        partes = texto.split(maxsplit=1)
        if len(partes) != 2:
            raise ValueError("Formato inválido")
        
        valor = float(partes[0].replace(',', '.'))
        categoria = partes[1].strip()
        
        # Registra no banco de dados
        if registrar_entrada(
            usuario_id=update.effective_user.id,
            valor=valor,
            categoria=categoria
        ):
            await update.message.reply_text(
                f"✅ Entrada de R${valor:.2f} registrada na categoria '{categoria}'. "
                "Envie mais uma ou digite 'sair'."
            )
        else:
            await update.message.reply_text(
                "❌ Erro ao registrar entrada. Tente novamente ou digite 'sair'."
            )
            
    except ValueError:
        await update.message.reply_text(
            "❌ Formato inválido! Use: valor categoria\n"
            "Exemplo: 200 vendas\n"
            "Digite 'sair' para encerrar."
        )
    
    return ESPERANDO_VALOR

async def cancelar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancela o registro de entradas."""
    await update.message.reply_text("Registro de entradas cancelado.")
    return ConversationHandler.END

# Handler principal para registro de entradas
registrar_entrada_handler = ConversationHandler(
    entry_points=[
        CommandHandler('registrar_entrada', iniciar_registro),
        CallbackQueryHandler(iniciar_registro, pattern='^registrar_entrada$')
    ],
    states={
        ESPERANDO_VALOR: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, processar_entrada)
        ]
    },
    fallbacks=[CommandHandler('cancelar', cancelar)]
) 