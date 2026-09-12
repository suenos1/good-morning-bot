import os
import json
import requests
from datetime import datetime, timedelta

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("MAEDE_CHAT_ID")
DATA_FILE = "messages.json"

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    return response.status_code == 200

def main():
    # ساعت ایران (UTC+3:30)
    iran_time = datetime.utcnow() + timedelta(hours=3, minutes=30)
    now = iran_time.strftime("%H:%M")
    today = iran_time.strftime("%Y-%m-%d")

    data = load_data()
    sent_any = False

    for item in data:
        # اگه ساعت پیام با الان مطابقت داشت و امروز فرستاده نشده
        if item["time"] == now and item.get("last_sent") != today:
            if send_message(item["message"]):
                item["last_sent"] = today
                sent_any = True
                print(f"✅ ارسال شد: {item['message']}")
            else:
                print(f"❌ خطا در ارسال: {item['message']}")

    if sent_any:
        save_data(data)
        print("💾 فایل messages.json آپدیت شد.")
    else:
        print(f"⏳ الان ساعت {now} هست، پیامی برای ارسال نیست.")

if __name__ == "__main__":
    main()
