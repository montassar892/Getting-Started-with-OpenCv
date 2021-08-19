import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread(r"C:\Users\monta\Desktop\Opencv\photos\ali.jpg")
cv.imshow('img', img)


# grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale", grayscale)

blank = np.zeros(img.shape[:2], np.uint8)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("circle", circle)

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow("Mask", mask)


# Grayscale histogram
#gray_hist = cv.calcHist([grayscale], [0], mask, [256], [0, 256])

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel('Bins')
# plt.ylabel(" # of pixels ")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()


# Color histogram
plt.figure()
plt.title("color Histogram")
plt.xlabel('Bins')
plt.ylabel(" # of pixels ")

plt.xlim([0, 256])
plt.show()

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calculHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)


# incomplete
