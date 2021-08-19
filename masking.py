# masking ==> focusing on smth
import cv2 as cv
import numpy as np


img = cv.imread(r"C:\Users\monta\Desktop\Opencv\photos\ali.jpg")
cv.imshow("Image", img)

blank = np.zeros(img.shape[:2], dtype=np.uint8)
cv.imshow('Blank Image', blank)

mask1 = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2),
                     (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)
cv.imshow("mask1", mask1)

masked_img = cv.bitwise_and(img, img, mask=mask1)
cv.imshow("masked_img", masked_img)

mask = cv.circle(
    blank, (img.shape[1]//2 + 45, img.shape[0]//2 + 45), 100, 255, -1)
cv.imshow("Mask", mask)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Image", masked)


# weird shaped mask
circle = cv.circle(
    blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

masked = cv.bitwise_and(circle, rectangle)
cv.imshow("masked1", masked)


maskk = cv.bitwise_and(img, img, mask=masked)
cv.imshow("maskk", maskk)


# size of the mask = size of the image !!!!!!!!!!!

cv.waitKey(0)
