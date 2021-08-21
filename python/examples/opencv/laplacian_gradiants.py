import cv2 as cv
import sys
import numpy as np

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
print(original.shape)

cv.imshow('Original', original)

gray = cv.cvtColor(original, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

lap = cv.Laplacian(gray, ddepth=cv.CV_64F)
cv.imshow('Laplacian', lap)

lap2 = np.uint8(np.absolute(lap))
cv.imshow('Laplacian 2', lap2)


cv.waitKey(0)
