import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print(df.columns)

for col in df.columns:
    if "return" in col.lower():
        df[col] = pd.to_numeric(df[col], errors="coerce")

if "expense_ratio_pct" in df.columns:
    anomalies = df[
        (df["expense_ratio_pct"] < 0.1)
        | (df["expense_ratio_pct"] > 2.5)
    ]

    print("Expense Ratio Anomalies")
    print(anomalies)

df.to_csv(
    "data/processed/performance_clean.csv",
    index=False
)

print("Performance cleaning completed")