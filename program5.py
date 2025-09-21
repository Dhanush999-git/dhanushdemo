import pandas as pd
df = pd.read_csv('IRIS.csv')
print(df.head())
#grouPING AND AGGREGATING EXAMPLE
print("\n1. average petal length by species:")
print(df.groupby("species").agg({"petal_length":["mean","max","min"]}))
p=df.pivot_table(values=["petal_length"], index=["species"], aggfunc=["mean","max","min"])
print(p)
#JOINING AND MERGING EXAMPLE
data1={"species": ["setosa", "versicolor", "virginica"],
        "sepal_length": [5.1, 7.0, 6.3],
        "sepal_width": [3.5, 3.2, 3.3]}
data2={"species": ["setosa", "versicolor", "virginica"],
        "petal_length": [1.4, 4.7, 6.0],
        "petal_width": [0.2, 1.4, 2.5]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print("\nDataFrame 1:")
print(df1)  
print("\nDataFrame 2:")
print(df2)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.columns)
print(df.values)
print(df.size)
print(df.index)
print(df.shape)
print(df.dtypes)
print(df['species'].unique())
print(df.iloc[5])
print(df.loc[5])
print(df[df["age"]>30])

md_value=df["sepal.length"].mode()[0]

print(md_value)

std_value=df["petal.length"].std()
print(std_value)