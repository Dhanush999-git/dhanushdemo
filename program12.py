import matplotlib.pyplot as plt
import numpy as np
arr1=np.array([1,2,3,4,5,5,6,5,4,3,2,1])
data=["A","B","C","D","E","F","G","H","I","J","K","L"]
plt.pie(arr1,explode=[0.4,0.5,0,0,0,0.1,0,0,0,0,0,0],labels=data,radius=1.2,shadow=True,startangle=90)
# plt.pie(arr1,labels=data)
plt.show()