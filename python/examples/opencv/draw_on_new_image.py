import cv2 as cv
import numpy as np
import sys


img = np.zeros((500, 500, 3), dtype='uint8')
print(img.shape) # (500, 500, 3)
red = 0
green = 0
blue = 255

img[:] = 255,255,255          # pain the whole image to white
#img[:] = blue,green,red          # pain the whole image
#img[0:100] = blue,green,red      # 100 rows on the top of the image
#img[:,0:100] = blue,green,red    # 100 columns on the left of the image
#img[100:200, 200:300] = blue,green,red  # A square on the image

#cv.line(img, (30, 70), (150, 90), color=(blue, green, red), thickness=3)

#cv.putText(img, text="Hello World", org=(20, 100), fontFace=cv.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(blue, green, red), thickness=2)

cv.imshow('Image', img)
cv.waitKey(0)
