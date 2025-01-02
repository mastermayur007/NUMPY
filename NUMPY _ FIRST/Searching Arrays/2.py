import numpy as np

arr=np.array([1,2,3,2,2,3,3,4,4,55,6,6,7,4,3,2])
x=np.where(arr%2==0)
print(x)