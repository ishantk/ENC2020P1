import pandas as pd
import numpy as np

data = np.random.randn(5, 4)
# print(data)

# Labeling the Columns :)
table = pd.DataFrame(data, columns=["COL1", "COL2", "COL3", "COL4"])

print(table)

print("~~~~~COL2 Data~~~~~")

print(table["COL2"])

print("~~~~~COL3 Data~~~~~")

print(table.COL3)

print(">> Iterating in DataFrame 1")
# iteritems -> Iterate Column Wise
# Iterate in DataFrame
for key, value in table.iteritems():
    print(key)
    print("^^^^^^^^^^^^")
    print(value)
    print("~~~~~~~~~~~~~~~~~~")

print()

print(">> Iterating in DataFrame 2")
# iteritems -> Iterate Row Wise
# Iterate in DataFrame
for key, value in table.iterrows():
    print(key)
    print("^^^^^^^^^^^^")
    print(value)
    print("~~~~~~~~~~~~~~~~~~")

print()

print(">> Iterating in DataFrame 3")
# iteritems -> Iterate as Tuples
# Iterate in DataFrame
for row in table.itertuples():
    print(row)
    print("^^^^^^^^^^^^")


