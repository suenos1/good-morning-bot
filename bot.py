import os
import json
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = int(os.environ.get("ADMIN_ID"))  # آیدی عددی خودت
DATA_FILE = "messages.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    await update.message.reply_text(
        "سلام محمد 👋\n\n"
        "دستورات:\n"
        "/add ساعت | متن پیام\n"
        "مثال:\n"
        "/add 09:30 | صبح بخیر مائده 🌸\n\n"
        "/list → لیست پیام‌ها\n"
        "/del شماره → حذف پیام"
    )

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    try:
        text = update.message.text.replace("/add", "").strip()
        time_part, message = text.split("|", 1)
        time_part = time_part.strip()
        message = message.strip()
        
        # اعتبارسنجی ساعت
        datetime.strptime(time_part, "%H:%M")
        
        data = load_data()
        data.append({
            "time": time_part,
            "message": message,
            "last_sent": None
        })
        save_data(data)
        await update.message.reply_text(f"✅ اضافه شد:\n⏰ {time_part}\n💬 {message}")
    except Exception as e:
        await update.message.reply_text(f"❌ خطا: {e}\nفرمت درست: /add 09:30 | متن پیام")

async def list_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    data = load_data()
    if not data:
        await update.message.reply_text("📭 هیچ پیامی ثبت نشده.")
        return
    text = "📋 لیست پیام‌ها:\n\n"
    for i, item in enumerate(data):
        text += f"{i}. ⏰ {item['time']}\n💬 {item['message']}\n\n"
    await update.message.reply_text(text)

async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    try:
        idx = int(context.args[0])
        data = load_data()
        removed = data.pop(idx)
        save_data(data)
        await update.message.reply_text(f"🗑️ حذف شد:\n{removed['message']}")
    except Exception as e:
        await update.message.reply_text(f"❌ خطا: {e}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("list", list_messages))
    app.add_handler(CommandHandler("del", delete))
    print("ربات مدیریت روشن شد...")
    app.run_polling()

if __name__ == "__main__":
    main()
