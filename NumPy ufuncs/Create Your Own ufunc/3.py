import numpy as np

if type(np.add)==np.ufunc:
    print("add is a ufunc")
else:
    print("add is not a ufunc")    