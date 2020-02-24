"""
Broadcasting:
When we have to work with arrays of different shapes
"""

import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("x is:")
print(x)
print(x.shape)

print()

v = np.array([1, 0, 1])
print("v is:")
print(v)
print(v.shape)

# Create an Array of same Shape with some Garbage Values :)
y = np.empty_like(x)
print("y is:")
print(y)
print(y.shape)

print("************")

for i in range(4):
    y[i, :] = x[i, :] + v

print("y now is:")
print(y)
print(y.shape)