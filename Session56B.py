"""
    Pytorch and Numpy
    Bridging between pytorch and numpy
"""


import torch
import numpy as np

# Torch to numpy
print("======Torch to numpy======")
X = torch.ones(5)
print(X, type(X))

Y = X.numpy()
print(Y, type(Y))

# Adding 1 to elements of X
X.add_(1)

print(X)
print(Y)

print("=====numpy to Torch====")

# numpy to Torch
A = np.ones(5)
B = torch.from_numpy(A)
print(A)
print(B)

np.add(A, 1, out=A)

print(A)
print(B)