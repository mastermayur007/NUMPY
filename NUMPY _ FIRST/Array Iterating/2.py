import numpy as np

# arr=np.array([[1,2,3,4],[5,6,7,8]])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in np.nditer(arr,flags=['buffered'],op_dtypes='S'):
    print(x)