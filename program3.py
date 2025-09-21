import pandas as pd
import numpy as np
#  Load iris.csv
df=pd.read_csv("iris.csv")

print(df.head())

# grouping and Aggregation Examples
print("\n1. Average SepalLength by Species:")
print(sdf.groupby("Species")["SepalLength"].mean())