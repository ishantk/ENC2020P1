"""
    Execute the Code for ANN here :)
"""

from Session58 import DataSetHelper
from Session58A import ANN


def main():

    fileName = "seeds.csv"

    dsHelper = DataSetHelper()

    X, Y, numOfClasses = dsHelper.readCSVFile(file=fileName, target="y", noramlize=True)

    print(X)
    print(Y)
    print(numOfClasses)




if __name__ == '__main__':
    main()