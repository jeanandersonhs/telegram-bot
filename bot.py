import logging
from telegram import Update

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


import os 
from dotenv import load_dotenv 


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
TOKEN = os.getenv("TOKEN-API-TELEGRAM")

# funcao processa a atualizacao
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="bem vindoooo ao bot"
    )


def main ():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))


    app.run_polling()
    print()





if __name__ == "__main__": 
    main()