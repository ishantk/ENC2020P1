"""
    numpy -> Library for Scientific, Mathematical Computing
    specially based on Arrays
    High Performance Library for Multi Dim Arrays :)

"""

import numpy as np

a1 = np.array(list(range(10, 21)))

a2 = np.arange(10, 21)

# With Step
a3 = np.arange(10, 21, 3)

print(a1)
print(a2)
print(a3)

print()

# a4 = np.ones((3, 3, 3))
a4 = np.ones((3, 3, 3), dtype=np.int)
print(a4)

a5 = np.linspace(0, 21, 5)
print(a5)
a4 = np.ones((3, 3, 3))


