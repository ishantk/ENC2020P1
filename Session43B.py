from sklearn import datasets, svm

digits = datasets.load_digits()

# Images i.e. numpy array of rgb values which are gray scaled
# Input
X = digits.data

# Labels i.e. 0, 1, 2, ....
# Output
Y = digits.target

# Number of Classes
print(digits.target_names)

print(X[11])
print(Y[11])

# Create the Model
model = svm.SVC()

# Train the Model
model.fit(X, Y)

# Predict the Class
predictedClass = model.predict([X[11]])
print(predictedClass)