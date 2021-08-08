import cv2 as cv
import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} FILENAME SCALE  where scale is 0.75 or some similar number between 0 and 1")

filename = sys.argv[1]
scale = float(sys.argv[2])

img = cv.imread(filename)

height, width, colors = img.shape
new_height = int(height * scale)
new_width = int(width * scale)

new_img = cv.resize(img, (new_width, new_height), interpolation=cv.INTER_AREA)
cv.imshow('Image', new_img)
cv.waitKey(0)
