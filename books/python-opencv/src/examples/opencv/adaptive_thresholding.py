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

# blockSize is like a kernelsize, the size of the box for which the algorithm computes the threshold
# computes the mean of each block and that's the optimal threshold for the center of that block
threshold = cv.adaptiveThreshold(grey, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv.THRESH_BINARY, blockSize=11, C=3)
cv.imshow('Adaptive Threshold', threshold)

# inverted_threshold = cv.adaptiveThreshold(grey, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv.THRESH_BINARY_INV, blockSize=11, C=3)
# cv.imshow('Adaptive Inverted Threshold', inverted_threshold)

# gaussian_threshold = cv.adaptiveThreshold(grey, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv.THRESH_BINARY, blockSize=11, C=3)
# cv.imshow('Adaptive Gaussian Threshold', gaussian_threshold)


# thresh, threshold_inverted = cv.threshold(grey, thresh=125, maxval=255, type=cv.THRESH_BINARY_INV)
# cv.imshow('Simple Inverted Threshold', threshold_inverted)

cv.waitKey(0)
