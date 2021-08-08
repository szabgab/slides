import cv2 as cv
import sys
import numpy as np

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)

def translate(img, x, y):
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translation_matrix, dimensions)

translated = translate(original, 100, 100)

cv.imshow('Translated', translated)

cv.waitKey(0)
