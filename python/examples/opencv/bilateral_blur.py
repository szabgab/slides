import cv2 as cv
import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} FILENAME DIAMETER")

filename = sys.argv[1]
diameter = int(sys.argv[2])

original = cv.imread(filename)
cv.imshow('Original', original)

blurred = cv.bilateralFilter(original, d=diameter, sigmaColor=50, sigmaSpace=15)
cv.imshow('Bilateral Blurred', blurred)

cv.waitKey(0)
