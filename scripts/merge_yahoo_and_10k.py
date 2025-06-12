# merge_yahoo_and_10k.py
import pandas as pd
from difflib import get_close_matches

def normalize_name(name):
    return name.lower().replace("inc.", "").replace("corporation", "").replace(",", "").strip()

def merge_datasets(yahoo_path, zero_shot_path, output_path="merged_results.csv"):
    yahoo_df = pd.read_csv(yahoo_path)
    sec_df = pd.read_csv(zero_shot_path)

    # Normalize names
    yahoo_df["name_norm"] = yahoo_df["Company"].apply(normalize_name)
    sec_df["name_norm"] = sec_df["Company"].apply(normalize_name)

    merged = []

    for _, sec_row in sec_df.iterrows():
        match = get_close_matches(sec_row["name_norm"], yahoo_df["name_norm"].tolist(), n=1, cutoff=0.85)
        if match:
            yahoo_row = yahoo_df[yahoo_df["name_norm"] == match[0]].iloc[0]
            combined = {**sec_row.to_dict(), **yahoo_row.to_dict()}
            merged.append(combined)
        else:
            print(f"🔍 No Yahoo match for {sec_row['Company']}")

    result_df = pd.DataFrame(merged)
    result_df.drop(columns=["name_norm"], inplace=True)
    result_df.to_csv(output_path, index=False)
    print(f"✅ Merged dataset saved to {output_path}")

# Example usage:
# merge_datasets("yahoo_finance_data.csv", "10k_aggregated_results.csv")
