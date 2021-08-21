import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)
print(original.shape)

rgb = cv.cvtColor(original, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
print(rgb.shape)

bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow('BGR', bgr)
print(bgr.shape)

print(np.array_equal(original, bgr)) # False

diff = original-bgr
cv.imshow('Diff', diff)

print(set(diff.flatten()))

cv.waitKey(0)

#plt.imshow(original)
#plt.show()
