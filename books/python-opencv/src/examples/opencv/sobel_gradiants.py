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

sobelx = cv.Sobel(gray, ddepth=cv.CV_64F, dx=1, dy=0)
sobely = cv.Sobel(gray, ddepth=cv.CV_64F, dx=0, dy=1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel', combined_sobel)


cv.waitKey(0)
