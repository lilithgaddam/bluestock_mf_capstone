import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print(df.columns)

if "transaction_date" in df.columns:
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])

if "amount" in df.columns:
    df = df[df["amount"] > 0]

if "transaction_type" in df.columns:
    df["transaction_type"] = df["transaction_type"].str.strip().str.title()

df = df.drop_duplicates()

df.to_csv("data/processed/transactions_clean.csv", index=False)

print("Transaction cleaning completed")