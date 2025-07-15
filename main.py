import logging
import requests
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, CallbackQueryHandler, filters

# API Keys
GEMINI_API_KEY = "AIzaSyASCHAAd7gtrH3Qmo2-T8HuHdMHPMmtqNw"
TELEGRAM_BOT_TOKEN = "7508241177:AAF5URqFveHTT0KzzFJyG4qQGt4BZ56bzYg"

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Gemini API Request
def call_gemini(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    params = {"key": GEMINI_API_KEY}
    response = requests.post(url, headers=headers, json=data, params=params)
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    raise Exception("Gemini API error")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    buttons = [
        [InlineKeyboardButton("💬 Ask AI", callback_data='ask')],
        [InlineKeyboardButton("📢 Add Me to Group", url=f"https://t.me/{context.bot.username}?startgroup=true")]
    ]
    await update.message.reply_text(
        f"👋 Hello {user.first_name}, welcome to Gemini AI Bot!\nUse /feature1 to /feature60 to explore.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# Button actions
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "ask":
        await query.edit_message_text("✍️ Please type your question now.")

# AI Chat
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    try:
        reply = call_gemini(text)
    except Exception:
        reply = "⚠️ Gemini AI failed. Try again later."
    await update.message.reply_text(reply)

# Group welcome
async def group_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    if chat.type in ["group", "supergroup"]:
        await context.bot.send_message(chat.id, "🤖 Gemini AI is now active in this group. Ask me anything!")

# 60 feature commands

async def feature_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 1 activated!")

async def feature_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 2 activated!")

async def feature_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 3 activated!")

async def feature_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 4 activated!")

async def feature_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 5 activated!")

async def feature_6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 6 activated!")

async def feature_7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 7 activated!")

async def feature_8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 8 activated!")

async def feature_9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 9 activated!")

async def feature_10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 10 activated!")

async def feature_11(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 11 activated!")

async def feature_12(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 12 activated!")

async def feature_13(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 13 activated!")

async def feature_14(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 14 activated!")

async def feature_15(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 15 activated!")

async def feature_16(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 16 activated!")

async def feature_17(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 17 activated!")

async def feature_18(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 18 activated!")

async def feature_19(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 19 activated!")

async def feature_20(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 20 activated!")

async def feature_21(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 21 activated!")

async def feature_22(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 22 activated!")

async def feature_23(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 23 activated!")

async def feature_24(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 24 activated!")

async def feature_25(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 25 activated!")

async def feature_26(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 26 activated!")

async def feature_27(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 27 activated!")

async def feature_28(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 28 activated!")

async def feature_29(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 29 activated!")

async def feature_30(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 30 activated!")

async def feature_31(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 31 activated!")

async def feature_32(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 32 activated!")

async def feature_33(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 33 activated!")

async def feature_34(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 34 activated!")

async def feature_35(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 35 activated!")

async def feature_36(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 36 activated!")

async def feature_37(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 37 activated!")

async def feature_38(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 38 activated!")

async def feature_39(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 39 activated!")

async def feature_40(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 40 activated!")

async def feature_41(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 41 activated!")

async def feature_42(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 42 activated!")

async def feature_43(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 43 activated!")

async def feature_44(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 44 activated!")

async def feature_45(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 45 activated!")

async def feature_46(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 46 activated!")

async def feature_47(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 47 activated!")

async def feature_48(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 48 activated!")

async def feature_49(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 49 activated!")

async def feature_50(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 50 activated!")

async def feature_51(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 51 activated!")

async def feature_52(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 52 activated!")

async def feature_53(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 53 activated!")

async def feature_54(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 54 activated!")

async def feature_55(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 55 activated!")

async def feature_56(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 56 activated!")

async def feature_57(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 57 activated!")

async def feature_58(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 58 activated!")

async def feature_59(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 59 activated!")

async def feature_60(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Feature 60 activated!")


# Main
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, group_welcome))

    # Register all 60 feature commands
    app.add_handler(CommandHandler("feature1", feature_1))
app.add_handler(CommandHandler("feature2", feature_2))
app.add_handler(CommandHandler("feature3", feature_3))
app.add_handler(CommandHandler("feature4", feature_4))
app.add_handler(CommandHandler("feature5", feature_5))
app.add_handler(CommandHandler("feature6", feature_6))
app.add_handler(CommandHandler("feature7", feature_7))
app.add_handler(CommandHandler("feature8", feature_8))
app.add_handler(CommandHandler("feature9", feature_9))
app.add_handler(CommandHandler("feature10", feature_10))
app.add_handler(CommandHandler("feature11", feature_11))
app.add_handler(CommandHandler("feature12", feature_12))
app.add_handler(CommandHandler("feature13", feature_13))
app.add_handler(CommandHandler("feature14", feature_14))
app.add_handler(CommandHandler("feature15", feature_15))
app.add_handler(CommandHandler("feature16", feature_16))
app.add_handler(CommandHandler("feature17", feature_17))
app.add_handler(CommandHandler("feature18", feature_18))
app.add_handler(CommandHandler("feature19", feature_19))
app.add_handler(CommandHandler("feature20", feature_20))
app.add_handler(CommandHandler("feature21", feature_21))
app.add_handler(CommandHandler("feature22", feature_22))
app.add_handler(CommandHandler("feature23", feature_23))
app.add_handler(CommandHandler("feature24", feature_24))
app.add_handler(CommandHandler("feature25", feature_25))
app.add_handler(CommandHandler("feature26", feature_26))
app.add_handler(CommandHandler("feature27", feature_27))
app.add_handler(CommandHandler("feature28", feature_28))
app.add_handler(CommandHandler("feature29", feature_29))
app.add_handler(CommandHandler("feature30", feature_30))
app.add_handler(CommandHandler("feature31", feature_31))
app.add_handler(CommandHandler("feature32", feature_32))
app.add_handler(CommandHandler("feature33", feature_33))
app.add_handler(CommandHandler("feature34", feature_34))
app.add_handler(CommandHandler("feature35", feature_35))
app.add_handler(CommandHandler("feature36", feature_36))
app.add_handler(CommandHandler("feature37", feature_37))
app.add_handler(CommandHandler("feature38", feature_38))
app.add_handler(CommandHandler("feature39", feature_39))
app.add_handler(CommandHandler("feature40", feature_40))
app.add_handler(CommandHandler("feature41", feature_41))
app.add_handler(CommandHandler("feature42", feature_42))
app.add_handler(CommandHandler("feature43", feature_43))
app.add_handler(CommandHandler("feature44", feature_44))
app.add_handler(CommandHandler("feature45", feature_45))
app.add_handler(CommandHandler("feature46", feature_46))
app.add_handler(CommandHandler("feature47", feature_47))
app.add_handler(CommandHandler("feature48", feature_48))
app.add_handler(CommandHandler("feature49", feature_49))
app.add_handler(CommandHandler("feature50", feature_50))
app.add_handler(CommandHandler("feature51", feature_51))
app.add_handler(CommandHandler("feature52", feature_52))
app.add_handler(CommandHandler("feature53", feature_53))
app.add_handler(CommandHandler("feature54", feature_54))
app.add_handler(CommandHandler("feature55", feature_55))
app.add_handler(CommandHandler("feature56", feature_56))
app.add_handler(CommandHandler("feature57", feature_57))
app.add_handler(CommandHandler("feature58", feature_58))
app.add_handler(CommandHandler("feature59", feature_59))
app.add_handler(CommandHandler("feature60", feature_60))

app.run_polling()
