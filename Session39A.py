import cv2, time

video = cv2.VideoCapture(0)

check, frame = video.read()

print("==check==")
print(check)

print("==frame==")
print(frame)

# Program will halt gor 5 seconds on line num 14
time.sleep(5)

print("Releasing Video")
video.release()

cv2.imshow("MyFrame", frame)
cv2.waitKey(0) # Take any keyboard input and then quit :)
cv2.destroyAllWindows()