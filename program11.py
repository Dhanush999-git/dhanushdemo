import matplotlib.pyplot as plt
import numpy as np
arr1=np.array([1,2,3,4,5,5,6,5,4,3,2,1])
data=["A","B","c","D"]
plt.pie(arr1,labels=data)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(axis='x')
plt.show()