import numpy as np

array1 = np.array([10, 20, 30])
array2 = np.array([[10, 20, 30], [30, 40, 50], [50, 60, 70], [70, 80, 90]])
array3 = np.array([[10, 20], [30, 40, 50, 60], [50, 60, 70]])

print(array1)
print(array1.shape)

print()

print(array2)
print(array2.shape)

print()
print(array3)
print(array3.shape)

print(len(array1))
print(len(array2))
print(len(array3))

print(array1[2])        # 30
print(array2[2][1])     # 60
print(array3[1])        # list([30, 40, 50, 60])
print(array3[1][1])     # 40