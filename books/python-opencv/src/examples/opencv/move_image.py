import cv2 as cv
import sys
import numpy as np

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)

def move(img, x, y):
    move_matrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, move_matrix, dimensions)

moved = move(original, 100, 100)

# x < 0  = left
# x > 0  = Right
# y < 0  = Up
# y > 0  = Down

cv.imshow('Moved', moved)

cv.waitKey(0)
