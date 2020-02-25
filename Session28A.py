import pandas as pd
import numpy as np

numbers1 = [10, 20, 30, 40, 50]
numbers2 = np.arange(11, 51, 10)

series1 = pd.Series(numbers1)
print(series1)

print("------------")

series2 = pd.Series(numbers2)
print(series2)

print("------------")

employee = {"name": "John", "age": 22, "salary": 30000}
series3 = pd.Series(employee)
print(series3)

print("------Accessing Data in Series------")
# Access the data using indexing technique
print(series1[2])
print(series2[3])
print(series3["salary"])

# Apply Slicing
print("------Slicing Data in Series------")
print(series1[1:3])
print(series2[3:])
print("Slicing on Dictionary")
print(series3["name":"salary"])
print(series3["age":])

print("---Updating Data---")
series1[1] = 111
series2[2] = 222
series3["salary"] = 45000

print(series1)
print(series2)
print(series3)

print("--Deleting Data in Series--")

del series1[0]
print(series1)

print("--Appending Data in Series--")
# series1.append(77)
series1[50] = 77
print(series1)
print(series1[3:51])

series3["email"] = "john@example.com"
print(series3)
