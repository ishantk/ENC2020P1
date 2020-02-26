import matplotlib.pyplot as plt

X = list(range(1, 11))

# List Comprehension
Y1 = [n for n in X]
Y2 = [n**2 for n in X]
Y3 = [n**3 for n in X]

print(X)
print(Y1)
print(Y2)
print(Y3)

# plt.plot(X, Y1, "y")
# plt.plot(X, Y2, "m")
# plt.plot(X, Y3, "black")

# plt.plot(X, Y1, "o")
# plt.plot(X, Y2, "^")
# plt.plot(X, Y3, "D")

plt.plot(X, Y1, ".", color="black")
plt.plot(X, Y2, "-.")
plt.plot(X, Y3, ":")

plt.show()