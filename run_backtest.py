from backtest import backtest

COINS = [
    "BTC/USDT","ETH/USDT","BNB/USDT","SOL/USDT",
    "XRP/USDT","ADA/USDT","DOGE/USDT","AVAX/USDT",
    "DOT/USDT","MATIC/USDT"
]

results = []

for coin in COINS:
    print(f"Testing {coin}...")
    res = backtest(coin)
    results.append(res)

# 📊 summary
for r in results:
    print("\n", r)
