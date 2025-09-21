import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
iris=pd.read_csv("iris.csv")
print(iris.head())
print(iris.tail())
# plt.plot(iris["petal_length"],'*',color='red',ms=5)
# plt.plot(iris["petal_width"],'0',color='blue',ms=8)
# plt.plot(iris["sepal_length"],'s',color='green',ms=10)
# plt.plot(iris["sepal_length"],'+',color='orange',ms=12)
# plt.legend(['petal','sepal'])
# plt.xlabel("Sepal Length")
# plt.ylabel("Sepal width")
# plt.title("Iris Petal Length vs Width")
# plt.show()

#histogram
plt.pie(iris["species"],value_counts(),labels=iris["species"].unique(),autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title("Iris Species Distribution")
plt.show()