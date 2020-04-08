"""
Explore skimage library
https://scikit-image.org/docs/dev/auto_examples/index.html
"""

import pandas as pd
from skimage import io
import os
import matplotlib.pyplot as plt


def showLandMarks(image, landMarks):

    plt.imshow(image)
    plt.scatter(landMarks[:, 0], landMarks[:, 1], s=100, marker='.', c='r')
    plt.show()


def main():

    landMarksDataSet = pd.read_csv("faces/face_landmarks.csv")
    print(landMarksDataSet)

    imageNum = 10
    imageName = landMarksDataSet.iloc[imageNum, 0]
    print(">> Image Name is:", imageName)

    # in the data set from 1 column till the last
    landMarks = landMarksDataSet.iloc[imageNum, 1:].to_numpy()
    print("Lanmarks:")
    print(landMarks)
    print(landMarks.shape)

    landMarks = landMarks.astype("float").reshape(-1, 2)
    print("ReShaped LandMarks Array")
    print(landMarks)
    print(landMarks.shape)

    showLandMarks(io.imread(os.path.join('faces/', imageName)), landMarks)

if __name__ == '__main__':
    main()
