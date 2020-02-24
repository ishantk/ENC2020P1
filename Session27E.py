import numpy as np
X = np.array([(1, 2, 3), (4, 5, 6)])
Y = np.array([(1, 2, 3), (4, 5, 6)])

print("X is:")
print(X)

print("Y is:")
print(Y)

print("VStack is:")
print(np.vstack((X, Y)))

print("HStack is:")
print(np.hstack((X, Y)))

# We can apply all the mathematical functions on our Arrays
Z = np.arange(1, 101, 10)
print(Z)
print(np.log10(Z))
print(np.sin(Z))
print(np.tan(Z))

# Execute this QuickStart Tutorial
# https://numpy.org/devdocs/user/quickstart.html
