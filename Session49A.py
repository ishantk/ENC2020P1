"""
    Feature Selection or Dimensionality Reduction


    We need to optimize our dataset with only those features which are meaningful
    i.e. contain more information

    Variance: Quality of Being Different
    We shall remove all the features whose variance doesnt meet some threshold as specified by us
    eg: We have a dta set with boolean features, we wish to consider 80% of the samples

"""

from sklearn.feature_selection import VarianceThreshold

X = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 1],
        [0, 1, 0],
        [0, 1, 1]
    ]

print("X BEFORE")
print(X)

# Var[X] = p(1-p)
reduction = VarianceThreshold(.8 * (1-.8))
X = reduction.fit_transform(X)

print("X AFTER")
print(X)