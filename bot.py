# bot.py
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from datetime import datetime
import os

load_dotenv() # Carga las variables del archivo .env
# Reemplaza con tu token de bot real
# Es mejor usar una variable de entorno para esto, especialmente si vas a subir a GitHub
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "") 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja el comando /start."""
    await update.message.reply_text('¡Hola! Soy tu bot de prueba. Usa /help para ver mis comandos.')
async def fecha(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja el comando /fecha."""
    #esto saca la fecha actual
    fecha_actual = datetime.now()
    #devulbe la fecha por pantalla
    await update.message.reply_text(fecha_actual.strftime("%d/%m/%Y"))


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja el comando /help."""
    help_message = (
        "¡Hola! Aquí tienes los comandos que puedes usar:\n\n"
        "/start - Inicia una conversación conmigo.\n"
        "/help - Muestra este mensaje de ayuda.\n"
        "/echo [texto] - Repite el texto que le digas."
    )
    await update.message.reply_text(help_message)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja el comando /echo."""
    if context.args:
        text_to_echo = " ".join(context.args)
        await update.message.reply_text(f"Dijiste: {text_to_echo}")
    else:
        await update.message.reply_text("Usa: /echo [tu texto]")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja cualquier mensaje de texto que no sea un comando."""
    if update.message.text:
        await update.message.reply_text(f"Recibí tu mensaje: '{update.message.text}'")

def main() -> None:
    """Inicia el bot."""
    application = Application.builder().token(TOKEN).build()

    # Registra los handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo))
    application.add.handler(CommandHandler("fecha", fecha))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)) # Para mensajes de texto que no son comandos

    print("Bot iniciado... Presiona Ctrl+C para detenerlo.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
