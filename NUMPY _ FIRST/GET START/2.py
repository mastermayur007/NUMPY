# one dimentions
import numpy as np

a=np.array([1,2,3,5,6,7,8])
print(a)
print("=========================================================")
# two dimentions
b=np.array([[12,14,15],[54,23,64]])
print(b)
# three dimentions
print("=========================================================")
c=np.array([[12,14,15],[54,23,64],[77,5,7]])
print(c)
print("=========================================================")



arr=np.array([1,2,4,5,6,7],ndmin=5)
print(arr)
print(f"the number of dimentions is {arr.ndim}")