# Array Maths :)

import numpy as np

data = [
    (8, 9),
    (10, 12),
    (13, 14)
]

arr1 = np.array(data)
print(arr1)
print(arr1[0:2, 1])

print(arr1.min())
print(arr1.max())
print(arr1.sum())

print(arr1.min(axis=0))
print(arr1.max(axis=1))
print(arr1.sum(axis=0))     # Axis 0 -> Columns
print(arr1.sum(axis=1))     # Axis 1 -> Rows

print("==arr1==")
print(arr1)

print("==sqrt==")
print(np.sqrt(arr1))

print("==std==")
print(np.std(arr1))

a1 = np.array([(1, 2, 3), (3, 4, 5)])
a2 = np.array([(1, 2, 3), (3, 4, 5)])

print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)      # Floating Point Div
print(a1 // a2)     # Integral Div

a3 = a1 + a2
a3 = np.add(a1, a2)
print(a3)

print("=====Dot Product on 2D Array======")

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
z = np.dot(x, y)
print(z)

print("=====Dot Product on 1D Array======")

u = np.array([9, 10])
v = np.array([11, 12])
w = np.dot(u, v)
print(w)

# Validate the Answers by doing a practical maths :)
print(">> X:")
print(x)
print(">> X':")
print(x.T)
