import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)
grey = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)
canny = cv.Canny(grey, 125, 175)  # # or of original?
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# Try also
# cv.RETR_EXTERNAL
# cv.RETR_TREE

# cv.CHAIN_APPROX_NONE - return all the contours
# cv.CHAIN_APPROX_SIMPLE - compress to endpoints

# Number of contours: length of the list

# Try to blur the image before finding the edges and finding the contours it will probably reduce the contours

# ret, threshold = cv.threshold(img, 125, 255, cv.THRESH_BINARY)
# this will try to binarize the image


print(contours)
cv.waitKey(0)
