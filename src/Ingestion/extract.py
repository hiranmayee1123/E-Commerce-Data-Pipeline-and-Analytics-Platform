import pandas as pd

def extract_data():
    df = pd.read_csv("data/raw_data.csv")
    df.to_csv("data/extracted_data.csv", index=False)
    print("✅ Data Extracted")
