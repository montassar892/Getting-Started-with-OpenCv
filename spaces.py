import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\monta\Desktop\Opencv\photos\ali.jpg")
#cv.imshow("Image", img)


plt.imshow(img)
plt.show()   # the difference between these to methods opencv displays bgr images matplotlib has no idea about bgr it will dispaly it as an rgb   "

# converting the image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


#  BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

plt.imshow(rgb)
plt.show()  # !!! matplotlib works with RGB !!!


# BGR to L*a*b

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# you cannot convert grayscale to hsv directly: grayscale  to bgr and then bgr to hsv

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv --> bgr", hsv_bgr)

cv.waitKey(0)
