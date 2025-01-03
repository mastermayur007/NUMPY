import numpy as np

arr1=np.array([1,2,3,4,5,1,1,1,2,2])
arr2=np.array([1,2,3,4,5,1,1,1,2,2,5,4,2,542,1,23,24,54,21])
newarr=np.union1d(arr1,arr2)
print(newarr)
