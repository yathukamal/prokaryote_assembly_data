import pandas as pd

df = pd.read_csv('pas_refseq.csv', dtype={34:str, 35:str, 36:str})

df1 = df[df["assembly_level"] != "Scaffold"]
df2 = df[df["release_type"] != "Minor"]


df3 = df.drop_duplicates(subset=["organism_name"], keep = "last")


df.to_csv("cleanedpas.csv")