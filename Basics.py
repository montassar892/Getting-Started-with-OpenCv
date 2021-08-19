import cv2 as cv

img = cv.imread(r'C:\Users\monta\Desktop\Opencv\photos\ali.jpg')
cv.imshow('image', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('grayimg', gray)

# Blur images ==> thabbe
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


# Edge Cascade ==> detection od edges

canny = cv.Canny(blur, 100, 120)
cv.imshow("Canny Edges", canny)

# Dilating the image
dialated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dialated", dialated)


# Eroding
eroded = cv.erode(dialated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)


# resize
resized = cv.resize(img, (500, 500))
cv.imshow("Resized", resized)

# Crapping

cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)
