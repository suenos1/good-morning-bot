import os
import requests

# این مقادیر از "Secrets" گیت‌هاب خوانده می‌شوند (امن هستند)
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("MAEDE_CHAT_ID")

# متن پیام صبح بخیر (هر چه دوست دارید اینجا بنویسید)
MESSAGE = "صبح بخیر مایدانامممم 💙\nاز طرف آغ ممد روز خوبی داشته باشییی دوستت دارممم!"

# آدرس API تلگرام برای ارسال پیام
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHAT_ID, "text": MESSAGE}

# ارسال درخواست به تلگرام
response = requests.post(url, data=payload)

if response.status_code == 200:
    print("✅ پیام صبح بخیر با موفقیت ارسال شد.")
else:
    print(f"❌ خطا در ارسال پیام: {response.text}")
