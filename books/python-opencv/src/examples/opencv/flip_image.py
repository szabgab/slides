import cv2 as cv
import sys

if len(sys.argv) != 3:
    exit(f"""
       Usage: {sys.argv[0]} FILENAME CODE
       Where
         0 - vertical flip
         1 - horizontal flip
        -1 - 180 degrees rotation (flipping both vertical and horiziontal)
    """)

filename = sys.argv[1]
flip_code = int(sys.argv[2])

original = cv.imread(filename)
cv.imshow('Original', original)

flipped = cv.flip(original, flip_code)

cv.imshow('Flipped', flipped)

cv.waitKey(0)
