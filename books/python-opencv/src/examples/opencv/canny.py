import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Origianl', original)

edges = cv.Canny(original, =125, 175) # providing two thresholds
cv.imshow('Edges', edges)
cv.waitKey(0)
