# 4 bitwise operators and or xor not
# we use it while working with masks
import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), np.uint8)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

# # Bitwise AND   --> intersecting regions

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND ", bitwise_and)

# # Bitwise OR    --> non-intersecting regions and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise_or", bitwise_or)

# # Bitwise XOR   --> non-intersecting regions

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise_xor", bitwise_xor)

# # Bitwise NOT

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Bitwise_not", bitwise_not)


cv.waitKey(0)
