import pandas as pd
import csv

df = pd.read_csv("final.csv")
del df["Luminosity"]
del df["Star_name"]
del df["Unnamed: 0.1"]
del df["Unnamed: 6"]
df.dropna()

df = df.rename({
    "Unnamed: 0":"Star_Name"
},axis="columns")

df.to_csv("cleaned.csv")