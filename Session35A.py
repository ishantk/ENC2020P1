import pandas as pd

import matplotlib.pyplot as plt

# https://seaborn.pydata.org/tutorial.html
import seaborn as sns

table = pd.read_csv("soccerdata.csv")
print(table)

print(table.head())

print(table.head(10))

# print(table["Name"])
print(table.Name)

# sns.countplot(y=table.Nationality, palette="Set2")
# sns.countplot(x="Age", data=table)
# sns.countplot(x="Nationality", data=table)

# plt.show()

# Case Study : Find the GoalKeeper who is best to stop the kicks :)
# Let us create some weights
w1 = 1
w2 = 2
w3 = 3
w4 = 4

table["BEST_GK"] = (w1*table.GK_Kicking + w2*table.GK_Diving + w3*table.GK_Positioning + w4*table.GK_Reflexes)
print(table["BEST_GK"])

sortedData = table.sort_values("BEST_GK")
print(sortedData)

print(sortedData.tail(10))