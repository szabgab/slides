import cv2 as cv
import sys
#import numpy as np

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} FILENAME DEGREES")

filename = sys.argv[1]
degrees = float(sys.argv[2])

original = cv.imread(filename)
cv.imshow('Original', original)

def rotate(img, angle, center=None):
    height, width = img.shape[0:2]
    if center is None:
        center = (width//2, height//2)

    rotation_matrix = cv.getRotationMatrix2D(center, angle, 1.0)

    dimensions = (width, height)
    return cv.warpAffine(img, rotation_matrix, dimensions)

rotated = rotate(original, degrees)

cv.imshow('Rotated', rotated)

cv.waitKey(0)
