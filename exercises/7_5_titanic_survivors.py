import pandas as pd

file = input()
df = pd.read_csv(file)

result = df.groupby(["sex", "pclass"])["survived"].sum()
print(result)