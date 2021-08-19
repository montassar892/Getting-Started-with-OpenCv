import cv2 as cv
import numpy as np


img = cv.imread(r"C:\Users\monta\Desktop\Opencv\photos\ali.jpg")

cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


# Laplacian == pencil shading version of the edges of the image 


lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacien", lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel_X", sobelx)
cv.imshow("Sobel_Y", sobely)
cv.imshow("Combined_Sobel", combined_sobel) # Calculates the gradients on the  x and y 



canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)  

cv.waitKey(0)
