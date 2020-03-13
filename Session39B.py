import cv2
import numpy as np

video = cv2.VideoCapture(0)

frameCount = 0
while True:

    check, frame = video.read()
    frameCount += 1
    print(frame)
    cv2.imshow("MyVideo", frame)
    # cv2.imshow("MyVideo", np.rot90(frame))

    key = cv2.waitKey(1) # 1 is 1 milli second

    if key == ord('q'):
        break

print(">> Total Frames Captured:", frameCount)
video.release()
cv2.destroyAllWindows()

# Assignment : Use OpenCV API and covert list of frames as video and save it :)
# Explore OpenCV : https://docs.opencv.org/master/d9/df8/tutorial_root.html

