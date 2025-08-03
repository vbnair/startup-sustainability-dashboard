import pandas as pd
import os

def load_and_prepare_data(dataset_path):
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Input file not found: {dataset_path}")
    
    df = pd.read_csv(dataset_path)
    df_complete = df[df['Data Completeness'] == 'Complete']
    incomplete_count = len(df) - len(df_complete)

    rev_split = df_complete["Revenue FY21–23 (INR Cr)"].str.split("/", expand=True)
    df_complete["Revenue_FY21"] = pd.to_numeric(rev_split[0], errors="coerce")
    df_complete["Revenue_FY22"] = pd.to_numeric(rev_split[1], errors="coerce")
    df_complete["Revenue_FY23"] = pd.to_numeric(rev_split[2], errors="coerce")

    return df_complete, incomplete_count

def generate_sector_summary(df_complete, output_sector_path):
    sector_summary = df_complete.groupby("Sector").agg({
        "Valuation (USD B)": "mean",
        "Funding (USD B)": "mean",
        "Revenue_FY23": "mean"
    }).reset_index()
    sector_summary.rename(columns={
        "Valuation (USD B)": "Avg Valuation (USD B)",
        "Funding (USD B)": "Avg Funding (USD B)",
        "Revenue_FY23": "Avg Revenue FY23 (INR Cr)"
    }, inplace=True)
    sector_summary.to_csv(output_sector_path, index=False)
