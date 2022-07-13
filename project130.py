import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Starname"]
del df["dist"]
del df["rad"]
del df["mass"]
del df["Luminosity"]

df.to_csv('staars.csv') 