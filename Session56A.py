import torch
X = torch.randn(5, 5)
print(X)

# 2D Array converted to 1 D Array
Y = X.view(25)
print(Y)

# 2D Array converted to Array of 1 D Array
Z = X.view(-1, 25)
print(Z)

print(X.shape)
print(Y.shape)
print(Z.shape)

# item works where we have only 1 value in tensor :)
P = torch.randn(1)
print(P)
print(P.item())

