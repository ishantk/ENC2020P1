import torch
print(torch.__version__)

# Always explore documentation for your learning part :)
# https://pytorch.org/tutorials/

# numpy, tensorflow and pytorch focuses on tensors i.e. n-Dimensional Arrays

A = torch.rand(5, 3)
print(A)

# class 'torch.Tensor'
print(type(A))

print()

B = torch.empty(5, 3)
print(B)

print()

# C = torch.zeros(5, 3)
# C = torch.zeros(5, 3, dtype=torch.int)
C = torch.zeros(5, 3, dtype=torch.long)
print(C)

print()

# Constructing tensor objects yourself with data
D = torch.tensor([10, 20, 30, 40, 50])
print(D)

print()

# Constructed an array of 1's from some existing array by manipulating the data in it :)
D = D.new_ones(5, 3, dtype=torch.double)
print(D)

print()

# E = torch.rand_like(D, dtype=torch.float)
E = torch.randn_like(D, dtype=torch.float)
print(E)

print(E.size())
print(E.shape)

F = torch.rand(5, 3)

# Use Operators to perform matrix operations
print(E + F)
print(torch.add(E, F))

result = torch.empty(5, 3)
torch.add(E, F, out=result)
print(result)

print()

# Its gonna add E to F and modify data in F
F.add_(E)
print("==F==")
print(F)

print()

# Indexing on Tensors
print("==F[:, 1]==")
print(F[:, 1]) # 1st Column in Tensor