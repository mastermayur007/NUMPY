import numpy as np

arr1=np.array([1,2,3,4,5])
arr2=np.array([6,7,8,9,10])

newarr1=np.add(arr1,arr2)
newarr2=np.subtract(arr1,arr2)
newarr3=np.multiply(arr1,arr2)
newarr4=np.divide(arr1,arr2)
newarr5=np.power(arr1,arr2)
newarr6=np.mod(arr1,arr2)
newarr7=np.remainder(arr1,arr2)
newarr8=np.divmod(arr1,arr2)
newarr9=np.absolute(arr1,arr2)
print(newarr1,'\n',newarr2,'\n',newarr3,'\n',newarr4,'\n',newarr5,'\n',newarr6,'\n',newarr7,'\n',newarr8,'\n',newarr9)