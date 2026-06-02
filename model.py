from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import joblib

FEATURES = ["rsi","ema","macd","atr","return","vol_change"]

def train(df):
    X = df[FEATURES]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

    model = XGBClassifier(
        n_estimators=200,
        max_depth=5,
        learning_rate=0.05
    )

    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    print("Accuracy:", acc)

    joblib.dump(model, "model.pkl")

    return model


def load_model():
    return joblib.load("model.pkl")
