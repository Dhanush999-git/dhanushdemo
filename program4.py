import pandas as pd
import numpy as np
#  Load iris.csv
df=pd.read_csv("iris.csv")
print(df.head())
# grouping and Aggregation Examples
print("\n1. Average SepalLength by Species:")
print(df.groupby("species")["sepal_length"].mean())
#aggregation
print(  df.groupby("variety").agg({"sepal_length":["mean","max","min"]}))
#pivoting
p=df.pivot_table(values=["sepal_length","petal_length"], index="variety", aggfunc="mean")
#joning and merging
species_info=pd.DataFrame({
    "variety":["Sentosa","Versicolor","Virgincia"],
})