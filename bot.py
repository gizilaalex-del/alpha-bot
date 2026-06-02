import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8851792706:AAEVK7MQWeM_jjDMIXQTSK8pWxc3cJU-q60"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 ALPHA BOT ONLINE")

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 BTCUSDT — LONG")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scan", scan))

    print("🚀 BOT STARTED")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())

async def help_command(update, context):
    text = """
📊 Крипто бот команди:

/start - запустити бота
/signal - отримати сигнали
/help - список команд

🔥 Аналізує 10 монет
⏱ Таймфрейми: 1h / 4h / 1d
    """
    await update.message.reply_text(text)
app.add_handler(CommandHandler("help", help_command))
