from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os, asyncio
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ALPHA BOT OK")

def run_web():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 ALPHA BOT ONLINE")

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 BTCUSDT — LONG\nStrength: 8.2/10")

Thread(target=run_web, daemon=True).start()

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("scan", scan))

app.run_polling(close_loop=False)

