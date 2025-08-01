import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
#print(type(original))  # numpy.ndarray
print(original.shape)

cv.imshow('Original', original)
cv.waitKey(0)
