import numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(50)
print(X)

plt.hist(X, 50)
plt.show()
