import pandas as pd

df = pd.read_csv(
    "data/processed/performance_clean.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

filtered = df[
    df["risk_grade"]
    .str.contains(
        risk,
        case=False,
        na=False
    )
]

top3 = (
    filtered
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(
    top3[
        [
            "scheme_name",
            "sharpe_ratio",
            "return_3yr_pct",
            "risk_grade"
        ]
    ]
)