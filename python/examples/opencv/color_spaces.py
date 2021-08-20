import cv2 as cv
import sys
import numpy as np

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)
print(original.shape)

lab = cv.cvtColor(original, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)
print(lab.shape)

back = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('Back', back)
print(back.shape)

print(np.array_equal(original, back)) # False
cv.imshow('Diff', original-back)

cv.waitKey(0)
