
import pandas as pd

file = input()

df = pd.read_csv(file)
cleaned = df.dropna(subset=["cabin"])
count_passengers = len(cleaned)
count_survived = cleaned["survived"].sum()

print(f"Passengers with cabin numbers recoded: {count_passengers}")
print(f"Amount that survived: {count_survived}")
