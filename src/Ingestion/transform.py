import pandas as pd

def transform_data():
    df = pd.read_csv("data/extracted_data.csv")
    df.dropna(inplace=True)
    df["date"] = pd.to_datetime(df["date"])
    df.to_csv("data/transformed_data.csv", index=False)
    print("✅ Data Transformed")
