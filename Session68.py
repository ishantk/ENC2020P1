"""
    Face Detection with OpenCV and PreDefined Deep Learning Model from OpenCV
    CNN Architectures: LeNet, AlexNet, VGG, GoogLeNet, ResNet and many more

    Ref: https://github.com/opencv/opencv_extra/blob/master/testdata/dnn/download_models.py

    caffemodel with txt file having information of the model

"""
import numpy as np
import cv2

modelData = {
    "prototxt": "deploy.prototxt.txt",
    "model": "res10_300x300_ssd_iter_140000.caffemodel",
    "confidence": 0.5
}

# Load the Neural Network from the Pre-Defined Model
neuralNet = cv2.dnn.readNetFromCaffe(modelData["prototxt"], modelData["model"])

# Read the Image
# image = cv2.imread("ak.jpg")
image = cv2.imread("group-photo.jpg")
print(image)
print(image.shape)

# Dimensions of the Image
(h, w) = image.shape[:2]

# Converting Image into binary: As we need to feed this image to the Neural Network
# Pre-Processing and Noramlization of Image as Data for Neural Network
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300))
print(blob)

neuralNet.setInput(blob)

# predictions are the detectedFaces in the Image
predictions = neuralNet.forward()
print(predictions)
print(predictions.shape)

for i in range(0, predictions.shape[2]):

    # We are reading the confidence from the array
    confidence = predictions[0, 0, i, 2]

    if confidence < modelData["confidence"]:
        continue

    box =  predictions[0, 0, i, 3:7]  * np.array([w, h, w, h])
    (startX, startY, endX, endY) = box.astype("int")

    # text is confidence percentage upto 2 decimal places
    text = "{:.2f}%".format(confidence*100)

    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)

    y = startY-10 if startY-10 > 10 else startY + 10
    cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)


# Finally Show the Image with drawn rectangles over the faces with percentage
cv2.imshow("OUTCOME", image)
cv2.waitKey(0)

