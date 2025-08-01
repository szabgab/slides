import cv2 as cv
import sys
import numpy as np


def get_faces(filename, haar_calssifier):
    original = cv.imread(filename)
    gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
    faces_rect = haar_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    faces = []
    for face in faces_rect:
        (x, y, width, height) = face
        faces.append({"img": gray[].copy()[y:y+height, x:x+width], "loc": face})
    return faces

def collect_data(directory):
    haar_classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Have a bunch of pictures in each picture one person with a mapping of the name of the person.
    # Run image detection on each file and crop the recognized part.

    features = [] # list of cropped faces
    labels = [] # list of the corresponding names
    # for each subdirectory in directory (we assume it is the name of the person)
    #    for each image in the subdirectory
    #    features.append(crop(path_to_iamge)["img"])
    #    labels.append(name_of_person)

    features = np.array(features, dtype='object')
    labels = np.array(labels, dtype='object')
    np.save('features.npy', features)
    np.save('labels.npy', labels)

def create_recognizer():
    featurs = np.load('features.npy')
    labesl = np.save('labels.npy')

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.train(features, labels)
    face_recognizer.save("face_trained.yml")


def recognize_image(filename):
    original = cv.imread(filename)

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read("face_trained.yml")

    # get the cropped faces from an image
    faces = get_faces(filename)
    for face in faces:
        label, confidence = face_recognizer.predict(face["img"])
        print(f"This image is {label} with a confidence of {confidence}") # location: face["loc"]
        cv.putText(original, text=str(label), org=(20, 20), fontFace=cv.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0, 0, 255), thickness=2)
    cv.imshow('Faces', original)
    cv.waitKey(0)

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} DIRECTORY")

directory = sys.argv[1]
filename = sys.argv[2]
collect_data(directory)
create_recognizer()
recognize_image(filename)
