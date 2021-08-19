import os
import numpy as np
import cv2 as cv

p = []

DIR = r"C:\Users\monta\Desktop\Opencv\Faces\Train"
for i in os.listdir(r"C:\Users\monta\Desktop\Opencv\Faces\Train"):
    p.append(i)
print(p)

haar_cascade = cv.CascadeClassifier(
    r"C:\Users\monta\Desktop\Opencv\haar_face.xml")

features = []
labels = []


def create_train():
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print(f'Lenght of the features = {len(features)}')
print(f'Lenght of the labels = {len(labels)}')

print("Training is done")

# Converting to np arrays

features = np.array(features, dtype='object')
labels = np.array(labels)

# create the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the feautures list and the labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')

# Saving

np.save('features.npy', features)
np.save('labels.npy', labels)
