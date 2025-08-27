import pandas as pd, argparse, os
from sklearn.preprocessing import StandardScaler

def preprocess(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(os.path.join(input_dir, "raw_dataset.csv"))
    
    # Feature scaling
    scaler = StandardScaler()
    features = df.drop(columns=["binding_affinity"])
    scaled = scaler.fit_transform(features)
    
    df_scaled = pd.DataFrame(scaled, columns=features.columns)
    df_scaled["binding_affinity"] = df["binding_affinity"].values
    df_scaled.to_csv(os.path.join(output_dir, "features.csv"), index=False)
    print(f"[INFO] Preprocessed dataset saved -> {output_dir}/features.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="data/raw")
    parser.add_argument("--output", type=str, default="data/processed")
    args = parser.parse_args()
    preprocess(args.input, args.output)
