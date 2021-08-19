import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\monta\Desktop\Opencv\photos\ali.jpg")
cv.imshow("Image", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("red", red)
cv.imshow("green", green)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

cv.waitKey(0)
