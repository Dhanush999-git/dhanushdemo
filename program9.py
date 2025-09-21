import pandas as pd 
import numpy as np
df=pd.read_csv("iris.csv")
md_value=df["sepal.length"].mode()[0]

print(md_value)

std_value=df["petal.length"].std()
print(std_value)