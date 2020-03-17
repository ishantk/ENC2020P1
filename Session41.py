# https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set

from sklearn.datasets import load_iris
from sklearn import tree

irisData = load_iris()
print("==IRIS DATASET==")
print(irisData)
print("Type of irisData is:", type(irisData))

print()

# Explore Features in DataSet
print("===IRIS DATA FEATURES===")
print(irisData.data)

print()

# Explore Target in DataSet
print("===IRIS DATA TARGET===")
print(irisData.target)

print()

# Explore Target NAMES in DataSet
print("===IRIS DATA TARGET NAMES===")
print(irisData.target_names)

# 1. Create the Model
model = tree.DecisionTreeClassifier()

# 2. Training the Model
model.fit(irisData.data, irisData.target)

# Lets Test The Model with a Sample Input
# inputData = [5.5, 2.3, 4.0,	1.3]
# predictedTarget = model.predict([inputData])
# print(predictedTarget)

inputData1 = [5.5, 2.3, 4.0, 1.3]
inputData2 = [5.43, 3.90, 1.15, 0.32]

predictedTargets = model.predict([inputData1, inputData2])
print(predictedTargets)

import graphviz
data = tree.export_graphviz(model, out_file=None)
graph = graphviz.Source(data)
graph.render("IRIS DATA SET DECISION TREE")
graph.view()

# Train the DecisionTreeClassifier with DataSet as in Session40
# Try looking for APIs to convert the string dataset into numbered dataset

