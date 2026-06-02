from data import get_data
from features import add_features
from model import load_model, FEATURES
import numpy as np

model = load_model()

INITIAL_BALANCE = 1000
RISK_PER_TRADE = 0.02   # 2%

FUTURE_BARS = 4  # через скільки свічок вихід

def predict_prob(df):
    X = df[FEATURES].values
    return model.predict_proba(X)[:, 1]


def backtest(symbol):
    df = get_data(symbol, "1h", 1000)
    df = add_features(df)

    balance = INITIAL_BALANCE
    trades = []
    position = None

    probs = predict_prob(df)

    for i in range(100, len(df) - FUTURE_BARS):

        price = df["close"].iloc[i]
        prob = probs[i]

        # 📌 ENTRY RULE
        if position is None:
            if prob > 0.7:
                position = {
                    "type": "long",
                    "entry": price,
                    "entry_i": i
                }

        # 📌 EXIT RULE
        if position is not None:
            entry_price = position["entry"]

            exit_price = df["close"].iloc[i + FUTURE_BARS]

            change = (exit_price - entry_price) / entry_price

            # risk-based sizing
            trade_size = balance * RISK_PER_TRADE

            pnl = trade_size * change

            balance += pnl

            trades.append(pnl)

            position = None

    return {
        "symbol": symbol,
        "final_balance": round(balance, 2),
        "trades": len(trades),
        "avg_trade": round(np.mean(trades), 4) if trades else 0,
        "win_rate": round(len([t for t in trades if t > 0]) / len(trades) * 100, 2) if trades else 0
    }
