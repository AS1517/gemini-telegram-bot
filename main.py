import os
import logging
import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Get environment variables
BOT_TOKEN = os.getenv("7508241177:AAF5URqFveHTT0KzzFJyG4qQGt4BZ56bzYg")
GEMINI_API_KEY = os.getenv("AIzaSyASCHAAd7gtrH3Qmo2-T8HuHdMHPMmtqNw
")

# Function to call Gemini API
def ask_gemini(question):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [{"text": question}]
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"❌ Gemini error: {str(e)}"

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Gemini Bot! Type any command from /feature1 to /feature60.")

# Dynamic feature handlers
def make_feature_handler(number):
    async def feature(update: Update, context: ContextTypes.DEFAULT_TYPE):
        prompt = f"Please explain feature number {number} in detail:"
        reply = ask_gemini(prompt)
        await update.message.reply_text(reply)
    return feature

# Main app setup
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Register /start command
app.add_handler(CommandHandler("start", start))

# Register all 60 feature commands
for i in range(1, 61):
    app.add_handler(CommandHandler(f"feature{i}", make_feature_handler(i)))

# Run bot
app.run_polling()