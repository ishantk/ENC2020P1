from sklearn.datasets import load_iris
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel


X, Y = load_iris(return_X_y=True)
print(X.shape)

model = ExtraTreesClassifier(n_estimators=50)
model.fit(X, Y)
print(model.feature_importances_)

sfModel = SelectFromModel(model, prefit=True)
X1 = sfModel.transform(X)
print(X1.shape)
print(X1)