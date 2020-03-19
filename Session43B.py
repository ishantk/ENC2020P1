from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

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

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

# Create the Model
model = svm.SVC()

# Train the Model
model.fit(x_train, y_train)

# Predict the Class
y_pred = model.predict(x_test)
print(y_pred)

# Percentage Score :) How Accurate the Model IS ?
print(">> Accuracy Score:", metrics.accuracy_score(y_test, y_pred))

# Assignment for the day : Implement SVM ML Model on Cats and Dogs Image DataSet
# PreRequisite : Please change image into gray scale and into numpy Array. Create your own labels
# dataset will be available on github
