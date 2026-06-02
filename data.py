import ccxt
import pandas as pd

exchange = ccxt.binance()

def get_data(symbol, tf="1h", limit=300):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=tf, limit=limit)
    df = pd.DataFrame(ohlcv, columns=["time","open","high","low","close","volume"])
    return df
