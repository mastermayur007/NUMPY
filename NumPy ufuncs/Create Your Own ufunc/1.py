import numpy as np

def myval(x,y):
    return x+y

myval=np.frompyfunc(myval,2,1)
print(myval([1,2,3,4],[4,5,6,7]))