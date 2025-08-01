import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
print(original.shape)
cv.imshow('Original', original)

gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)

haar_classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

faces_rect = haar_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# print(faces_rect)
print(f"Number of faces: {len(faces_rect)}")

faces = original.copy()
for (x, y, width, height) in faces_rect:
    cv.rectangle(faces, (x, y), (x+width, y+height), color=(0, 0, 255), thickness=2)
cv.imshow('Faces', faces)

cv.waitKey(0)
