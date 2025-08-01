import cv2 as cv
import numpy as np
import sys


img = np.zeros((500, 500, 3), dtype='uint8')
print(img.shape) # (500, 500, 3)
red = 0
green = 0
blue = 255

cv.rectangle(img, (100,100), (250, 250), color=(blue, green, red), thickness=2)

red = 255
green = 0
blue = 0
cv.rectangle(img, (200,200), (350, 350), color=(blue, green, red), thickness=5)

red = 0
green = 255
blue = 0
cv.rectangle(img, (350,50), (450, 150), color=(blue, green, red), thickness=cv.FILLED)  # cv.FILLED == -1


cv.imshow('Image', img)
cv.waitKey(0)
