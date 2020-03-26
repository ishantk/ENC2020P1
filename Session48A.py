from sklearn.neighbors import KNeighborsClassifier
# from sklearn.neighbors import KNeighborsRegressor

#   Vehicle Classification  : Weight, Engine
trainingData = [
                    [100, 100],
                    [150, 110],
                    [180, 150],
                    [200, 180],
                    [800, 1000],
                    [1000, 1200],
                    [1200, 1300],
                    [1500, 1500]
               ]

# Labels
bike = 0
car = 1

# Names
labelNames = ["Bike", "Car"]

trainingLabels = [bike, bike, bike, bike, car, car, car, car]


testingData = [
                    [110, 105],
                    [1011, 1101],
                    [190, 160],
                    [911, 1213],
                    [160, 90],
                    [220, 170],
                    [1397, 1260],
                    [1475, 1300]
              ]
# k is 3 i.e. consider 3 nearest data point to perform classification
model = KNeighborsClassifier(n_neighbors=3)
model.fit(trainingData, trainingLabels)

# sampleInput = [213, 110]
# predictedClass = model.predict([sampleInput])
# print(">> PredictedClass for", sampleInput, "is:", labelNames[predictedClass[0]])

predictedClasses = model.predict(testingData)
print(predictedClasses)

# Assignments:
# Please solve classification problem using digits dataset from sklearn
# Please solve regression problem using covid19 dataset as shared yesterday
