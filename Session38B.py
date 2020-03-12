import cv2
print(cv2.__version__)

image = cv2.imread("ibis.jpg", 1) # 1 value specifies read image as colored image, 0 is BW
print("==Image==")
print(image)

print("===Image Shape===")
print(image.shape)

print("===Image Shape 0th Index===")
print(image.shape)
print(image.shape[0])

print("===Image 0th Index===")
print(image[0])

print("===Length of Image===")
print(len(image))
