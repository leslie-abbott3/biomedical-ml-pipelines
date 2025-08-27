import pandas as pd, argparse, yaml, os, joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(config_path):
    with open(config_path) as f:
        cfg = yaml.safe_load(f)

    df = pd.read_csv(cfg["data"]["input_path"])
    X = df.drop(columns=[cfg["data"]["target_column"]])
    y = df[cfg["data"]["target_column"]]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=cfg["training"]["test_size"], random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=cfg["model"]["n_estimators"],
        max_depth=cfg["model"]["max_depth"],
        random_state=cfg["model"]["random_state"]
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    print(f"[INFO] Test MSE: {mse:.4f}")

    scores = cross_val_score(model, X, y, cv=cfg["training"]["cv_folds"])
    print(f"[INFO] CV Scores: {scores}")

    os.makedirs("models/saved", exist_ok=True)
    joblib.dump(model, "models/saved/model.pkl")
    print("[INFO] Model saved -> models/saved/model.pkl")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="config/config.yaml")
    args = parser.parse_args()
    train_model(args.config)
