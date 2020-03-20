"""

    Unsupervised Learning
    We have data but no labels !!
    Classification will be numerically done by the model and we later name those classes
    Output is not known for observations in the dataset

    k-means clustering
    k here denotes number of classes we expect from model after classification

    ----------
    X   Y   P
    ----------
    1   1   A
    1   0   B
    0   2   C
    2   4   D
    3   5   E
    ----------

    we have above dataset as an example to work on 5 observations
    each observation has 2 data points
    But we don't know what class it belongs to

    We need to put the data points in clusters.
    But mathematically !!

    Step-1
    ------
    k -> represents number of classes
    k -> 2
    Assume any k i.e. 2 data points randomly from the given data set as CENTROIDS
    eg: A(1, 1) and C(0, 2)

    Step-2
    ------
    Calculate distance of each Point from CENTROIDS
    Eucilidean Distance Formula
    sqrt [ square(x2-x1) + square(y2-y1)]

    --------------------------------
    X   Y   P   C1(1, 1)    C2(0, 2)
                distance    distance
    --------------------------------
    1   1   A   0           1.4
    1   0   B   1           2.2
    0   2   C   1.4         0
    2   4   D   3.2         2.8
    3   5   E   4.5         4.2
    --------------------------------

    Step-3
    ------
    Arrange Points as per distance from Centroids
    P   Nearest To
    --------------
    A   C1
    B   C1
    C   C2
    D   C2
    E   C2

    Looking the data above:
    A and B who are nearest to C1, should be in one cluster
    C, D and E who are nearest to C2, should be in another cluster

    Even Now, we dont if above assumption is OK or not

    We need to be sure about our assumptions

    Step 4
    ------
    Re-Check Again with new centroids
    New Centroids shall be mean of previous clusters

    ---------------------
    X   Y   P   NearestTo
    ---------------------
    1   1   A   C1
    1   0   B   C1
    0   2   C   C2
    2   4   D   C2
    3   5   E   C2
    ---------------------

    C1 Mean = (1+1)/2, (1+0)/2
    C2 Mean = (0+2+3)/3, (2+4+5)/3

    C1Mean = (1, 0.5)
    C2Mean = (1.7, 3.7)

    --------------------------------
    X   Y   P   C1Mean(1, 0.5) C2Mean(1.7, 3.7)
                distance       distance
    --------------------------------
    1   1   A   0.5             2.7
    1   0   B   0.5             3.7
    0   2   C   1.8             2.4
    2   4   D   3.6             0.5
    3   5   E   4.9             1.9
    --------------------------------

    ---------------------
    X   Y   P   NearestTo
    ---------------------
    1   1   A   C1
    1   0   B   C1
    0   2   C   C1
    2   4   D   C2
    3   5   E   C2
    ---------------------

    From above observation 1 of the data points i.e. C
    has been shifted to C1 from C2

    For our assumptions from where we started to hold it true,
    if we get the same result twice we stop the computation further
                  -----------------

    NC1 Mean = (1+1+0)/3, (1+0+2)/3
    NC2 Mean = (2+3)/2, (4+5)/2

    NC1Mean = (0.7, 1)
    NC2Mean = (2.5, 4.5)

    Now, Calculate distance from these above centroids

    --------------------------------
    X   Y   P   NC1Mean(0.7, 1) NC2Mean(2.5, 4.5)
                distance        distance
    --------------------------------
    1   1   A   0.3             3.80
    1   0   B   1.04            4.74
    0   2   C   1.22            3.53
    2   4   D   3.26            0
    3   5   E   4.61            0.70
    --------------------------------


    ---------------------
    X   Y   P   NearestTo
    ---------------------
    1   1   A   C1
    1   0   B   C1
    0   2   C   C1
    2   4   D   C2
    3   5   E   C2
    ---------------------

    NOW, Algorithm Stops working
    We will finalize Cluster Centroids as
    (0.7, 1)        Class 1
    (2.5, 4.5)      Class 2

    Any UnObserved Data Point can now be computed
    that it is nearer to which cluster and hence, it will have that class

"""

import matplotlib.pyplot as plt
X = [1, 1, 0, 2, 3]
Y = [1, 0, 2, 4, 5]

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.scatter(X, Y)
plt.title("k-means clustering")
plt.show()

# Try writing above mathematical discussion as OOPS Program :)
class KMeans:

    def __init__(self, clusters=2):
        self.clusters = clusters
        print(">> KMeans Model Created")

    def fit(self, X, Y):
        pass

    def predict(self, X, Y):
        pass