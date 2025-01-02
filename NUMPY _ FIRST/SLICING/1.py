# Slice elements from index 1 to index 5 from the following array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(f"elements from index 1 to index 5{arr[1:5]}")


# Slice elements from index 4 to the end of the array:

print(f"Slice elements from index 4 to the end of the array:{arr[4:]}")
# Slice elements from the beginning to index 4 (not included):
print(f"Slice elements from the beginning to index 4 (not included):{arr[:4]}")
# Slice from the index 3 from the end to index 1 from the end:
print(f"Slice from the index 3 from the end to index 1 from the end:{arr[-3:-1]}")
# Return every other element from index 1 to index 5:
print(f"Return every other element from index 1 to index 5:{arr[0:6:2]}")
print(f"Return every other element from index 1 to index 5:{arr[::2]}")