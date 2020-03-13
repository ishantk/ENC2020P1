import cv2 as cv
import pytesseract

image = cv.imread("quote.jpg", 1)
text = pytesseract.image_to_string(image)
print(text)

