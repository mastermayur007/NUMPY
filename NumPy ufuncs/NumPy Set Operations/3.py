import numpy as np

arr1=np.array([1,2,3,4,5,1,1,1,2,2])
arr2=np.array([1,2,3,4,5,1,1,1,2,2,5,4,2,542,1,23,24,54,21])
newarr1=np.intersect1d(arr1,arr2,assume_unique=True)
newarr2=np.setdiff1d(arr1,arr2,assume_unique=True)
newarr3=np.setxor1d(arr1,arr2,assume_unique=True)
print(newarr1)
print(newarr2)
print(newarr3)
