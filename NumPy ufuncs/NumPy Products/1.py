import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([5,4,3,6,7])
x=np.cumprod([arr1,arr2])
print(x)