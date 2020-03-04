import pandas as pd
import numpy as np

array1 = np.arange(1, 101, 2)
array2 = list(range(1, 101, 2))

print(array1)
print(array2)

S1 = pd.Series(array2)
print(S1)

print("--------")
print(S1.axes)

print("--------")

values = S1.values
print(values)
print(type(values))

print("--------")
print(S1.head(5))

print("--------")
print(S1.tail(5))