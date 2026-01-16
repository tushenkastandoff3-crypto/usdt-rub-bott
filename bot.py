import requests
import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL")

bot = Bot(token=BOT_TOKEN)

def get_price():
    url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
    payload = {
        "asset": "USDT",
        "fiat": "RUB",
        "tradeType": "BUY",
        "page": 1,
        "rows": 1
    }
    r = requests.post(url, json=payload)
    return r.json()["data"][0]["adv"]["price"]

price = get_price()
bot.send_message(
    chat_id=CHANNEL,
    text=f"💵 USDT → RUB\n1 USDT = {price} ₽"
)
