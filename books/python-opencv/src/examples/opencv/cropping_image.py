import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

img = cv.imread(filename)
print(img.shape)
cv.imshow('Image', img)

cropped = img[450:800, 600:1000]

print(cropped.shape)
cv.imshow('Cropped', cropped)

cv.waitKey(0)
