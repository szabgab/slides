import cv2 as cv
import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} FILENAME OUTFILE")

filename = sys.argv[1]
outfile = sys.argv[2]


original = cv.imread(filename)
print(original.shape)
cv.imshow('Original', original)


cropped = original[400:1200, 100:900]
print(cropped.shape)
cv.imshow('Cropped', cropped)



scale = 0.7
height, width, colors = cropped.shape
new_height = int(height * scale)
new_width = int(width * scale)
resized = cv.resize(cropped, (new_width, new_height), interpolation=cv.INTER_AREA)
print(resized.shape)
cv.imshow('Resized', resized)

cv.imwrite(outfile, resized)

cv.waitKey(0)
