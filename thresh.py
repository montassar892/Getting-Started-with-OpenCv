import cv2 as cv

img = cv.imread(r"C:\Users\monta\Desktop\Opencv\photos\ali.jpg")

cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


# Simple Threshold ==> binarising the image

# returns thresh the image and threshold  is 150
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Threshold_inv", thresh_inv)


# Adaptative Thresholding
adaptative_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow("Adaptative_thresh", adaptative_thresh)

adaptative_thresh_inv = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow("Adaptative_thresh_inv", adaptative_thresh_inv)

adaptative_thresh_gaussian = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow("Adaptative_thresh_gaussian", adaptative_thresh_gaussian)


cv.waitKey(0)
