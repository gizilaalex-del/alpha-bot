from data import get_data
from features import add_features
from model import train
import pandas as pd

COINS = [
    "BTC/USDT","ETH/USDT","BNB/USDT","SOL/USDT",
    "XRP/USDT","ADA/USDT","DOGE/USDT","AVAX/USDT",
    "DOT/USDT","MATIC/USDT"
]

# 📌 створюємо датасет з усіх монет
all_data = []

for coin in COINS:
    print(f"Loading {coin}...")

    df = get_data(coin, "1h", limit=500)

    df = add_features(df)

    # 🎯 target: ціна через 4 години
    df["future_price"] = df["close"].shift(-4)
    df["target"] = (df["future_price"] > df["close"]).astype(int)

    df = df.dropna()

    all_data.append(df)

# 📊 об’єднуємо всі монети
dataset = pd.concat(all_data, ignore_index=True)

print("Dataset size:", len(dataset))

# 🚀 тренуємо модель
model = train(dataset)

print("Model training completed ✅")
