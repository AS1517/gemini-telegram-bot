import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ Your API keys
GEMINI_API_KEY = "AIzaSyASCHAAd7gtrH3Qmo2-T8HuHdMHPMmtqNw"
BOT_TOKEN = "7508241177:AAF5URqFveHTT0KzzFJyG4qQGt4BZ56bzYg"

# ✅ Gemini AI call function
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
        return "❌ Gemini API Error. Try again later."

# ✅ /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Gemini AI Bot!\nUse /ask <your question> or /feature1 to /feature5."
    )

# ✅ /ask command
async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("❗ Use like: /ask What is AI?")
        return
    reply = ask_gemini(question)
    await update.message.reply_text(reply)

# ✅ Create individual feature commands
def make_feature_command(n):
    async def feature(update: Update, context: ContextTypes.DEFAULT_TYPE):
        response = ask_gemini(f"Explain feature {n} in detail.")
        await update.message.reply_text(response)
    return feature

# ✅ Build and run app
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ask", ask))

# ✅ Add only 5 dynamic features (safe test)
for i in range(1, 6):
    app.add_handler(CommandHandler(f"feature{i}", make_feature_command(i)))

app.run_polling()