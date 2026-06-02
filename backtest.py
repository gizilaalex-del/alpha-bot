from data import get_data
from features import add_features
from model import load_model, FEATURES
import numpy as np

model = load_model()

INITIAL_BALANCE = 1000
RISK_PER_TRADE = 0.02

FUTURE_BARS = 10

STOP_LOSS = -0.02     # -2%
TAKE_PROFIT = 0.04    # +4%


def predict_prob(df):
    X = df[FEATURES].values
    return model.predict_proba(X)[:, 1]


def backtest(symbol):
    df = get_data(symbol, "1h", 1000)
    df = add_features(df)

    balance = INITIAL_BALANCE
    trades = []

    probs = predict_prob(df)

    i = 100
    while i < len(df) - FUTURE_BARS:

        prob = probs[i]

        # 📌 ENTRY
        if prob > 0.7:

            entry_price = df["close"].iloc[i]
            trade_size = balance * RISK_PER_TRADE

            entry_i = i

            exit_price = None
            exit_reason = None

            # 📊 симуляція руху після входу
            for j in range(i + 1, i + FUTURE_BARS):

                price = df["close"].iloc[j]

                change = (price - entry_price) / entry_price

                # 🛑 STOP LOSS
                if change <= STOP_LOSS:
                    exit_price = price
                    exit_reason = "SL"
                    break

                # 🎯 TAKE PROFIT
                if change >= TAKE_PROFIT:
                    exit_price = price
                    exit_reason = "TP"
                    break

            # ⏱ якщо ні SL/TP — вихід по часу
            if exit_price is None:
                exit_price = df["close"].iloc[i + FUTURE_BARS]
                exit_reason = "TIME"

            # 💰 PnL
            change = (exit_price - entry_price) / entry_price
            pnl = trade_size * change

            balance += pnl
            trades.append({
                "pnl": pnl,
                "reason": exit_reason
            })

            i += FUTURE_BARS  # пропускаємо після угоди
        else:
            i += 1

    wins = [t for t in trades if t["pnl"] > 0]

    return {
        "symbol": symbol,
        "final_balance": round(balance, 2),
        "trades": len(trades),
        "win_rate": round(len(wins) / len(trades) * 100, 2) if trades else 0,
        "avg_pnl": round(np.mean([t["pnl"] for t in trades]), 4)
    }
