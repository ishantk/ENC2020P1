import cv2
import  numpy as np

image = cv2.imread("ibis.jpg", 1)   # 1: Colored Image

print("===Original Image===")
print(image)

print("===Original Image Shape===")
shape = image.shape
print(shape)

resizedImage = cv2.resize(image, (shape[1]//2, shape[0]//2))
print("===Resized Image===")
print(resizedImage)

print("===Resized Image Shape===")
resizedShape = resizedImage.shape
print(resizedShape)
rotatedImage = np.rot90(resizedImage)

cv2.imshow("Resized Ibis", resizedImage)

cv2.imwrite("MyIbis.jpg", resizedImage)
cv2.imwrite("MyIbis90.jpg", rotatedImage)
print("MyIbis.jpg Saved")

cv2.waitKey(0) # Take any keyboard input and then quit :)
cv2.destroyAllWindows()


