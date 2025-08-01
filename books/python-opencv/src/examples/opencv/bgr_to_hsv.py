import cv2 as cv
import sys
import numpy as np

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)
print(original.shape)

hsv = cv.cvtColor(original, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
print(hsv.shape)

back = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('Back', back)
print(back.shape)

print(np.array_equal(original, back))

diff = original-back
cv.imshow('Diff', diff)
print(diff.shape)

print(set(diff.flatten()))

cv.waitKey(0)
