import numpy as np

arr=np.array([42,43,44,45,46,47,48,49,50])
filter_arr=arr%2==0
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)