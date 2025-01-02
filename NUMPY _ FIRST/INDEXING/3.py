
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(f"Access the third element of the second array of the first array: {arr[0,1,2]}")

# Print the last element from the 2nd dim:

print(f"Print the last element from the 2nd dim:{arr[0,1,-1]}")