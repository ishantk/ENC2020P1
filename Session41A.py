import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# DataSet Description
# 1. Number of times pregnant
# 2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
# 3. Diastolic blood pressure (mm Hg)
# 4. Triceps skin fold thickness (mm)
# 5. 2-Hour serum insulin (mu U/ml)
# 6. Body mass index (weight in kg/(height in m)^2)
# 7. Diabetes pedigree function
# 8. Age (years)
# 9. Class variable (0 or 1)

diabetesDataSet = pd.read_csv("pima-indians-diabetes.csv")
print(diabetesDataSet)

featureColumns = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']

X = diabetesDataSet[featureColumns]
# Y = diabetesDataSet['label']
Y = diabetesDataSet.label

print("~~~~~~~~~FEATURES~~~~~~~~~~")
print(X)
print("~~~~~~~~~LABELS~~~~~~~~")
print(Y)

# DataSet Division -> Training and Testing
# As we have dataset, we will not train model with all of our dataset
# we will train the model with random dataset observations.
# 70% shall be used to train and 30% for the testing
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

# Model Creation
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)

# Percentage Score :) How Accurate the Model IS ?
print(">> Accuracy Score:", metrics.accuracy_score(y_test, y_pred))