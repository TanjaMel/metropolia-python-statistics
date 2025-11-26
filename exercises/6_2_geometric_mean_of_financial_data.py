import pandas as pd
file = input()
df1 = pd.read_csv(file)


df1["date"] = pd.to_datetime(df1["date"])


df1 = df1.sort_values("date")


df1["previous_close"] = df1["value"].shift(1)


df1["Factor"] = df1["value"] / df1["previous_close"]


df1 = df1.drop(columns=["previous_close"])


df1 = df1.set_index("date")


df = df1.loc["2015-01-01":"2024-01-01"]

factors = df["Factor"].dropna()
geometric_mean = factors.prod() ** (1 / len(factors))# Put your code here

print(f"Geometric Mean of Daily Close Factor change between 2015-01-01 and 2024-01-01: {geometric_mean:.6f}")
print("\n DataFrame head:")
print(df.head())
print("\n DataFrame tail:")
print(df.tail())