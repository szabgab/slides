import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

img = cv.imread(filename)
print(img.shape)  # (1800, 2880, 3)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(img.shape)  # (1800, 2880)

cv.imshow('Image', img)
cv.waitKey(0)
