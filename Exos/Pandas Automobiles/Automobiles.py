import pandas as pd

numbers = {"two": 2,
"BuG": float("NaN"),
"twelve": 12,
"[four4": 4,
"five5": 5,
"six6": 6,
"three": 3,
"eight": 8}

df = pd.read_csv("Automobiles.csv", index_col="id")
df.count() / df.shape[0] * 100
df.drop(["average-mileage", "nbSeats", "wheel-base-style-circum-diam"], axis=1, inplace=True)
df["color"].value_counts()
df["color"].fillna("Unknown", inplace=True)
df.isnull().sum()

# COLOR
df["color"] = df["color"].apply(lambda x: x[6:] if "color-" in x else x )
df["color"] = df["color"].apply(lambda x: "black" if "blac" in x else x )

# Wheel_Base
df["length"] = df["length"].apply(lambda x: round(x, 1))

# Cylinders
df.rename({"num-of-cylinders" : "cylinders", "length": "wheel_base"}, inplace=True, axis=1)
print(df["cylinders"].value_counts())
df["cylinders"] = df["cylinders"].replace(numbers).astype('Int64')

#Afficher voiture toyota
print(df.loc[df["company"] == "Toyota"])

#Prix toute les voitures
print("Patrimony:  ", df["price"].sum())

#Couleur populaire
print("Popular color:  ", df["color"].value_counts().index[0], df["color"].value_counts()[0])

#Voiture la plus chère
print("La plus chère:   ", df.loc[df['price'] == df["price"].max()])

#Voitures par compagnies

print(df["company"].value_counts())

#Voiture chère par compagnie

print(df["company"].value_counts().keys().tolist())