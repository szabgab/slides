import cv2 as cv
import sys
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)

mask = None
# height, width = original.shape[:2]
# blank = np.zeros(shape=original.shape[:2], dtype='uint8')
# mask = cv.circle(blank.copy(), center=(int(width/2), int(height/2)), radius=int(min(width/5, height/5)), color=255, thickness=cv.FILLED)
# cv.imshow('Mask', mask)
# masked = cv.bitwise_and(original, original, mask=mask)
# cv.imshow('Masked', masked)

cv.waitKey(0)

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.xticks(ticks=[0, 50, 100, 150, 200, 255], labels=["0\nDark", 50, "100", 150, 200, "255\nBright"])
plt.ylabel("# of pixels")

colors  = ('blue', 'green', 'red')
for ix, color in enumerate(colors):
    hist = cv.calcHist([original], channels=[ix], mask=mask, histSize=[256], ranges=[0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])

plt.show()
