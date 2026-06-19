import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

# ===== start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 أهلاً! NovaHub شغال 3 في 1")

# ===== help =====
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - تشغيل\n/help - مساعدة\n/ai - سؤال ذكي بسيط"
    )

# ===== AI بسيط =====
async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("اكتب سؤالك بعد /ai")
        return

    await update.message.reply_text(f"🤖 رد ذكي: {text[::-1]}")

# ===== تشغيل البوت =====
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(CommandHandler("ai", ai))

app.run_polling()
