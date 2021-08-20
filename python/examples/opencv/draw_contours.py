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

ret, threshold = cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', threshold)

contours, hierarchies = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'Number of countours: {len(contours)}')

cv.drawContours(blank, contours=contours, contourIdx=-1, color=(0, 255, 255), thickness=2)
# contourIdx number of countours we want
cv.imshow('Contours', blank)

# We can compare the result to the result of Canny
# We can try to use instead of the threshole image the Canny immage to findContours
# In general it is probably better to use Canny instead of threshold for finding contours

print(contours)
cv.waitKey(0)
