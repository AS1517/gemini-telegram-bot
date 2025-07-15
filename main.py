import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get your bot token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN", "7508241177:AAF5URqFveHTT0KzzFJyG4qQGt4BZ56bzYg")

# --- Define dummy feature functions ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Gemini AI Bot with 60 Features!")

for i in range(1, 61):
    exec(f"""
async def feature_{i}(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You called Feature {i}")
""")

# --- Build the app ---
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Add start command
app.add_handler(CommandHandler("start", start))

# Add feature handlers
for i in range(1, 61):
    exec(f'app.add_handler(CommandHandler("feature{i}", feature_{i}))')

# Run the bot
app.run_polling()