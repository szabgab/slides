import cv2 as cv
import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} FILENAME KERNEL")

filename = sys.argv[1]
kernel = int(sys.argv[2])

original = cv.imread(filename)
cv.imshow('Original', original)

blurred = cv.blur(original, ksize=(kernel, kernel))

cv.imshow('Blurred', blurred)
cv.waitKey(0)
