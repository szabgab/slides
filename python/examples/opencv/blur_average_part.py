import cv2 as cv
import sys

if len(sys.argv) != 6:
    exit(f"Usage: {sys.argv[0]} FILENAME KERNEL TOP LEFT SIZE")

filename = sys.argv[1]
kernel = int(sys.argv[2])
top = int(sys.argv[3])
left = int(sys.argv[4])
size = int(sys.argv[5])

original = cv.imread(filename)
cv.imshow('Original', original)

blurred_part = cv.blur(original[top:top+size, left:left+size], ksize=(kernel, kernel), )
blurred = original.copy()
blurred[top:top+size, left:left+size] = blurred_part
cv.imshow('Blurred', blurred)

cv.waitKey(0)
