import numpy as np

arr=np.array([1,2,3,4,5,6])
x=arr.copy()
arr[0]=54
print(arr)
print(x)