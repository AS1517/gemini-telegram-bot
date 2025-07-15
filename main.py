import logging
import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

# ✅ API KEYS
GEMINI_API_KEY = "AIzaSyASCHAAd7gtrH3Qmo2-T8HuHdMHPMmtqNw"
BOT_TOKEN = "7508241177:AAF5URqFveHTT0KzzFJyG4qQGt4BZ56bzYg"

# ✅ Gemini API Call
def ask_gemini(message):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": message}]}]
    }
    params = {"key": GEMINI_API_KEY}
    try:
        response = requests.post(url, headers=headers, params=params, json=data)
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"❌ Gemini API Error: {e}"

# ✅ /start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to DeepSeak Gemini AI Bot!\nUse /ask <your question>\nOr try /feature1 to /feature60.")

# ✅ /ask Command
async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("❗ Use like: /ask What is AI?")
        return
    reply = ask_gemini(question)
    await update.message.reply_text(reply)

# ✅ Dynamic Feature Commands
def make_feature_command(n):
    async def feature(update: Update, context: ContextTypes.DEFAULT_TYPE):
        prompt = f"Explain feature {n} in detail."
        response = ask_gemini(prompt)
        await update.message.reply_text(response)
    return feature

# ✅ Setup App
app = ApplicationBuilder().token(BOT_TOKEN).build()

# ✅ Register Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ask", ask))

for i in range(1, 61):
    app.add_handler(CommandHandler(f"feature{i}", make_feature_command(i)))

# ✅ Start Bot
if __name__ == "__main__":
    app.run_polling()