import pandas as pd
file = input()

df = pd.read_csv(file)
result = df[(df["Species"] == "Iris-versicolor") & (df["PetalWidthCm"] == 1.5)]
print(len(result))