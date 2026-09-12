import os
import requests

# این مقادیر از "Secrets" گیت‌هاب خوانده می‌شوند (امن هستند)
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("MAEDE_CHAT_ID")

# متن پیام صبح بخیر (هر چه دوست دارید اینجا بنویسید)
MESSAGE = "صبح بخیر مائده 🌸\nاز طرف محمد. امروز روز خوبی داشته باشی و بدرخشی!"

# آدرس API تلگرام برای ارسال پیام
url = f"https://api.telegram.org/bot{7582935127:AAGL6LWmylMp6UkyG-X7HPfu7N1huACEnoA}/sendMessage"
payload = {"chat_id": 7089406628, "text": MESSAGE}

# ارسال درخواست به تلگرام
response = requests.post(url, data=payload)

if response.status_code == 200:
    print("✅ پیام صبح بخیر با موفقیت ارسال شد.")
else:
    print(f"❌ خطا در ارسال پیام: {response.text}")
