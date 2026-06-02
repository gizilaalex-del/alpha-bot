import ta

def add_features(df):
    df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()
    df["ema"] = ta.trend.EMAIndicator(df["close"], 20).ema_indicator()
    df["macd"] = ta.trend.MACD(df["close"]).macd()
    df["atr"] = ta.volatility.AverageTrueRange(
        df["high"], df["low"], df["close"]
    ).average_true_range()

    df["return"] = df["close"].pct_change()
    df["vol_change"] = df["volume"].pct_change()

    return df.dropna()
