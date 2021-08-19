import numpy as np
import cv2 as cv


haar_classifier = cv.CascadeClassifier(
    r"C:\Users\monta\Desktop\Opencv\haar_face.xml")

people = ["Elon Musk", "James Spader"]
features = np.load("features.npy", allow_pickle=True)
labels = np.load("labels.npy", allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')


img = cv.imread(
    r"C:\Users\monta\Desktop\Opencv\Faces\validation\Elon Musk\2.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)


# Detecting the face in the image

face_rect = haar_classifier.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in face_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidance = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidance of {confidance}')

    cv.putText(img, str(people[label]), (20, 20),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)
