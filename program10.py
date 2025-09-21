import pandas as pd
import numpy as np
df=pd.read_csv("IRIS.csv")
print(df.head())
print("\n1.Average sepalLength by Species:")
print(df.groupby("species")["sepal_length"].mean())
print(df.groupby("species").agg({"sepal_length":["mean","max","min"],"petal_length":["mean","max","min"]}))
p=df.pivot_table(values=["sepal_length","petal_length"],index="species",aggfunc="mean")
print(p)
md_value=df["petal_length"].mode()[0]
print(md_value)
std_value=df["petal_length"].std()
print(std_value)