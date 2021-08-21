import cv2 as cv
import sys
import numpy as np

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)
print(original.shape) # 3 dimension

gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

back = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('Back', back)

print(gray.shape) # 2 dimensional
print(back.shape) # 3 dimension
print(np.array_equal(gray, back[:,:,0])) # True
print(np.array_equal(gray, back[:,:,1])) # True
print(np.array_equal(gray, back[:,:,2])) # True

cv.waitKey(0)
