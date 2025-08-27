import argparse, joblib, pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="models/saved/model.pkl")
    parser.add_argument("--data", type=str, default="data/processed/features.csv")
    args = parser.parse_args()

    model = joblib.load(args.model)
    df = pd.read_csv(args.data)

    X = df.drop(columns=["binding_affinity"])
    y = df["binding_affinity"]

    preds = model.predict(X)
    print(f"[INFO] Evaluation Results")
    print(f"MSE: {mean_squared_error(y, preds):.4f}")
    print(f"R²: {r2_score(y, preds):.4f}")
