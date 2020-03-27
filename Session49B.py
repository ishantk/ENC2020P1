from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

X, Y = load_iris(return_X_y=True)
# print(X)
# print(Y)

print(X.shape)

kBest = SelectKBest(chi2, k=2)
X1 = kBest.fit_transform(X, Y)

print(X1.shape)
print(X1)