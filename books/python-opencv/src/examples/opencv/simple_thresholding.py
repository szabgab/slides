import cv2 as cv
import sys
import numpy as np

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)

blank = np.zeros(original.shape, dtype='uint8')
#blank[:] = -1 # white
cv.imshow('Blank', blank)

grey = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

thresh, threshold = cv.threshold(grey, thresh=125, maxval=255, type=cv.THRESH_BINARY)
print(thresh) # The thresh value we passed in
cv.imshow('Simple Threshold', threshold)

thresh, threshold_inverted = cv.threshold(grey, thresh=125, maxval=255, type=cv.THRESH_BINARY_INV)
cv.imshow('Simple Inverted Threshold', threshold_inverted)

cv.waitKey(0)
