import cv2 as cv
import sys
import numpy as np

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
#print(type(original))  # numpy.ndarray

cv.imshow('Original', original)
print(original.shape) # 3 dimensional matrix

blue, green, red = cv.split(original)
cv.imshow('Blue', blue)
print(blue.shape) # 2 dimensional matrix


cv.imshow('Green', green)
print(green.shape) # 2 dimensional matrix

cv.imshow('Red', red)
print(red.shape) # 2 dimensional matrix

bgr = cv.merge([blue, green, red])
cv.imshow('BGR', bgr)
print(bgr.shape) # 3 dimensional matrix

print(np.array_equal(original, bgr)) # True
print(np.array_equal(original[:,:,0], blue)) # True
print(np.array_equal(original[:,:,1], green)) # True
print(np.array_equal(original[:,:,2], red)) # True

black = np.zeros(original.shape[:2], dtype='uint8') # aka. blank

real_blue = cv.merge([blue, black, black])
cv.imshow('Real blue', real_blue)
print(np.array_equal(original[:,:,0], real_blue[:, :, 0])) # True

real_green = cv.merge([black, green, black])
cv.imshow('Real green', real_green)
print(np.array_equal(original[:,:,1], real_green[:, :, 1])) # True

real_red = cv.merge([black, black, red])
cv.imshow('Real red', real_red)
print(np.array_equal(original[:,:,2], real_green[:, :, 2])) # True



diff = original-bgr
cv.imshow('Diff', diff)
print(set(diff.flatten())) # {0}

cv.waitKey(0)
