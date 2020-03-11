# import Session37 as S37
from Session37 import LinearRegressionModel

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]
model = LinearRegressionModel()

# Model Training
model.fit(X, Y)

predictedOutput = model.predict(6)
print(">> Predicted Output for 6 is:", predictedOutput)
