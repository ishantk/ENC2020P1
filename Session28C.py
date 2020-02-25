import pandas as pd
table = pd.read_csv("CityTemps.csv")
print(table)
print("--Fetching Only Year--")
print(table["Year"])

print("---iloc---")
print(table.iloc[3])

print("---Slicing with iloc---")
print(table.iloc[1:5])

print("---Head---")
print(table.head(5))

print("---Tail---")
print(table.tail(5))