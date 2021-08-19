import cv2 as cv

img = cv.imread(r"C:\Users\monta\Desktop\Opencv\photos\ali.jpg")

cv.imshow("img", img)

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow("average blur", average)


# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)  # standard_diviation = 0
cv.imshow("gauss", gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow("Median", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)
