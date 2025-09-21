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
plt.hist(iris["sepal_length"],bins=10,color=['orange'],edgecolor='black',alpha=0.7)
plt.xlabel("Species")
plt.ylabel("Sepal Length")
plt.title("Iris Sepal Length by Species")
plt.show()