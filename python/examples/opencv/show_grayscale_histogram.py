import cv2 as cv
import sys
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)

gray = cv.cvtColor(original, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = None
# height, width = gray.shape[:2]
# blank = np.zeros(shape=gray.shape[:2], dtype='uint8')
# mask = cv.circle(blank.copy(), center=(int(width/2), int(height/2)), radius=int(min(width/5, height/5)), color=255, thickness=cv.FILLED)
# cv.imshow('Mask', mask)
# masked = cv.bitwise_and(gray, gray, mask=mask)
# cv.imshow('Masked', masked)

cv.waitKey(0)


# histSize = number of bins
gray_hist = cv.calcHist([gray], channels=[0], mask=mask, histSize=[256], ranges=[0, 256])
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.xticks(ticks=[0, 50, 100, 150, 200, 255], labels=["0\nBlack", 50, "100", 150, 200, "255\nWhite"])
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()
