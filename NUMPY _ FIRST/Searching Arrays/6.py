import numpy as np

arr=np.array([1,2,3,2,2,3,3,4,4,55,6,6,7,4,3,2])
# x=arr.sort()
# print(x)
x=np.searchsorted(arr,[2,3,4])
print(x)