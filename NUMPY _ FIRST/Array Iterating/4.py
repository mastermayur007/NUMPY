import numpy as np

arr=np.array([[1,2,3],[4,5,6]])

for idx,x in np.ndenumerate(arr):
    print(idx,x)