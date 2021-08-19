import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)
img = cv.imread(r'C:\Users\monta\Desktop\Opencv\photos\beach.jpg')
cv.imshow('Image', img)
Paint an image with certain color
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Green', blank)


# Draw a rectangle
cv.rectangle(blank, (0, 0),
             (blank.shape[0]//2, blank.shape[1]//2), (0, 255, 0), thickness=-1)
cv.imshow('Rectange', blank)

# Draw a circle
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2),
          40, (0, 0, 255), thickness=-1)

cv.imshow('Circle', blank)

# draw a line

cv.line(blank, (0, 0),
        (blank.shape[0]//2, blank.shape[1]//2), (255, 255, 255), thickness=2)
cv.imshow('Line', blank)

# Write text

cv.putText(blank, 'Hello World', (225, 255),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("hello", blank)

cv.waitKey(0)
