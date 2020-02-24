import numpy as np
array = np.loadtxt("data.txt", dtype=np.int)
print(array)

print()

arr1D = np.arange(10, 200, 10)
print(arr1D)
# np.savetxt("arrayData.txt", arr1D)
np.savetxt("arrayData1.txt", arr1D, fmt="%04d")
print("Data Saved")
