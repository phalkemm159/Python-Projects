import time
from plyer import notification # pip install plyer

while True:
    print("Please Sip some water as Remainder to Drink water")
    notification.notify(title = "Please Drink Water 🥤", message = "Please Drink water to be feel hydrated💧", timeout=10,)
    time.sleep(30)