import cv2 as cv
import numpy as np
import sys


img = np.zeros((500, 500, 3), dtype='uint8')
print(img.shape) # (500, 500, 3)

red = 0
green = 0
blue = 255
cv.circle(img, center=(200, 200), radius=150, color=(blue, green, red), thickness=2)

red = 255
green = 0
blue = 0
cv.circle(img, center=(100, 100), radius=75, color=(blue, green, red), thickness=5)

red = 0
green = 255
blue = 0
cv.circle(img, center=(300, 100), radius=75, color=(blue, green, red), thickness=cv.FILLED)


cv.imshow('Image', img)
cv.waitKey(0)
