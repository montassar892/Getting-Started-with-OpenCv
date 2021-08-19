import cv2 as cv

img = cv.imread(r"C:\Users\monta\Desktop\Opencv\photos\man.jpg")
cv.imshow("Image", img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Gray", gray)


haar_cascade = cv.CascadeClassifier(
    r"C:\Users\monta\Desktop\Opencv\haar_face.xml")  # !!! really sincitive to the noise (pb of detecting 7 faces while the img contains only 5 )
# haar_cascade not very effective in detecting faces
faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.3, minNeighbors=5)   # minNeighbors

print(f"Number of faces found = {len(faces_rect)}")

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow("Detected faces", img)

cv.waitKey(0)
