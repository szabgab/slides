import cv2 as cv
import sys
import numpy as np

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
print(original.shape)
height, width, _= original.shape
print(width)
cv.imshow('Original', original)

blank = np.zeros(shape=original.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank.copy(), center=(int(width/2), int(height/2)), radius=int(min(width/3, height/3)), color=255, thickness=cv.FILLED)
cv.imshow('Mask', mask)
print(mask.shape) # 2D

masked = cv.bitwise_and(original, original, mask=mask)
cv.imshow('Masked', masked)


full_mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
print(full_mask.shape) #3D

masked2 = cv.bitwise_and(original, full)
cv.imshow('Masked 2', masked2)
print(np.array_equal(masked, masked2)) #True


cv.waitKey(0)
