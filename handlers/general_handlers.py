from telegram import Update
from telegram.ext import ContextTypes
from responses.messages import WELCOME_MESSAGE, HELP_MESSAGE

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_MESSAGE) 