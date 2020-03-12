from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# Initial Data
X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

# Lienar Regression : 1 Line of Code :)
data = stats.linregress(X, Y)
print(">> Slope is:", data[0])
print(">> Interceptor is:", data[1])
print(">> Equation of Line: y = {} + {} * x".format(data[1], data[0]))
maxX = np.max(X) + 10
minY = np.min(Y) - 10

print("maxX:", maxX)
print("minY:", minY)

# Data Points for Linear Regression. Instead of 5, we got 100
x = np.linspace(minY, maxX, 100)
y = data[1] + data[0] * x

print(x)
print("----------")
print(y)

plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.plot(x, y, color="red", label="Regression Line")
plt.scatter(X, Y, color="blue", label="Data Points")
plt.legend()
plt.show()





