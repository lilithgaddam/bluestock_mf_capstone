import pandas as pd
import os

folder = "data/raw"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

for file in files:
    print("=" * 50)
    print("Dataset:", file)

    df = pd.read_csv(os.path.join(folder, file))

    print("Shape:", df.shape)
    print(df.dtypes)
    print(df.head())