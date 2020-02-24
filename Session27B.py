import numpy as np
array = np.arange(10, 51, 2)

# For fetching based on indexes i.e. Filtering the data :)
slices = slice(1, 20, 2)

# with traditional list and range :)
indexes = list(range(1, 20, 2))

print(array)
print(array[0:7])
print(slices)

print(array[slices])
print(array[indexes])

