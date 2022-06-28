import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

df=df.rename({'Star_name': "PStar_name", 
                'Distance': "PDistance", 
                'Mass': "PMass", 
                'Radius': "PRadius", 
                },axis="columns")

del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df=df.rename({'PStar_name': "Star_name", 
                'PDistance': "Distance", 
                'PMass': "Mass", 
                'PRadius': "Radius", 
                },axis="columns")


df.to_csv("CleanedStars.csv")     

print(list(df))