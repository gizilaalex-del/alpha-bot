import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


# ---------- COMMANDS ----------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 ALPHA BOT ONLINE")


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 TEST SIGNAL\n\nBTCUSDT — LONG\nStrength: 8.2/10"
    )


# ---------- MAIN BOT SETUP ----------

def create_app():
    if not TOKEN:
        
        raise RuntimeError("BOT_TOKEN is not set!")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scan", scan))

    return app


# ---------- SAFE ASYNC START ----------

async def main():
    app = create_app()

    await app.initialize()
    await app.start()

    # запускаємо polling без run_polling (це прибирає твою помилку)
    await app.updater.start_polling()

    print("🚀 ALPHA BOT STARTED")

    # тримаємо процес живим
    await app.updater.idle()


if __name__ == "__main__":
    asyncio.run(main())
