import pandas as pd
import numpy as np

file = input()
df = pd.read_csv(file)

numeric_cols = df.select_dtypes(include=[np.number]).columns
numeric_cols = numeric_cols.drop("Id")

z_scores = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()

mask = (np.abs(z_scores) <= 2).all(axis=1)

filtered_df = df[mask]

print(filtered_df)