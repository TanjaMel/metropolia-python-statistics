import pandas as pd
file = input()
df = pd.read_csv(file, index_col='id')

cond_fare = df["fare"] > 60
cond_embarked = df["embarked"] == "C"

titles = ["Rev", "Mayor", "Col", "Dr", "Master"]
cond_titles = df["name"].str.contains("|".join(titles), case=False, na=False)

elite_passengers = df[(cond_fare & cond_embarked) | cond_titles]

print(elite_passengers)