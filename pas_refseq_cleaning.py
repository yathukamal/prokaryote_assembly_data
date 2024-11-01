import pandas as pd
#read csv
df = pd.read_csv('pas_refseq.csv', dtype={34:str, 35:str, 36:str})
#get rid of scaffold or minor within the data
df1 = df[df["assembly_level"] != "Scaffold"]
df2 = df[df["release_type"] != "Minor"]

#drop any duplicates
df3 = df.drop_duplicates(subset=["organism_name"], keep = "last")

#make the cleaned data in a new csv file
df.to_csv("cleanedpas.csv")