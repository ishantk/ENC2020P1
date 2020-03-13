import cv2
import numpy as np
image = cv2.imread("ibis.jpg", 0)   # 0 Black and White

print(image)
# Use Numpy and rotate Image by 90 Degrees
rotatedImage1 = np.rot90(image)
rotatedImage2 = np.rot90(rotatedImage1)

print(image)
print(rotatedImage1)

cv2.imshow("AnyTitleForImage", rotatedImage2)
cv2.waitKey(0) # Take any keyboard input and then quit :)
# cv2.waitKey(5000)
cv2.destroyAllWindows()