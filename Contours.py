import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\monta\Desktop\Opencv\photos\ali.jpg')
cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank", blank)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("blur", blur)
# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny", canny)

ret, thresh = cv.threshold(
    gray, 125, 255, cv.THRESH_BINARY)  # ==> binary image
cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))


# -1 ==> all contours  2 thickness
cv.drawContours(blank, contours, -1, (0, 0, 255), 2)

cv.imshow('Contours Drawn', blank)
cv.waitKey(0)
