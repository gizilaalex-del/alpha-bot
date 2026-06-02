import numpy as np
from data import get_data
from features import add_features
from model import load_model, FEATURES

COINS = [
    "BTC/USDT","ETH/USDT","BNB/USDT","SOL/USDT",
    "XRP/USDT","ADA/USDT","DOGE/USDT","AVAX/USDT",
    "DOT/USDT","MATIC/USDT"
]

model = load_model()

def market_filter(df):
    return df["atr"].iloc[-1] > df["atr"].mean()

def predict(df):
    X = df[FEATURES].iloc[-1:].values
    prob = model.predict_proba(X)[0][1]
    return prob * 100

def analyze_coin(symbol):
    df = add_features(get_data(symbol, "1h"))
    df4 = add_features(get_data(symbol, "4h"))
    df1d = add_features(get_data(symbol, "1d"))

    if not market_filter(df4) or not market_filter(df1d):
        return "NO TRADE", 0

    confidence = predict(df)

    if confidence > 70:
        return "BUY 📈", confidence
    elif confidence < 30:
        return "SELL 📉", confidence
    else:
        return "WAIT ⏳", confidence


def scan_market():
    results = []
    for coin in COINS:
        sig, conf = analyze_coin(coin)
        results.append((coin, sig, conf))

    return results

def scan_market():
    results = []
    for coin in COINS:
        sig, conf = analyze_coin(coin)
        results.append((coin, sig, conf))
    return results

    
