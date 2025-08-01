import cv2 as cv
import numpy as np

blank = np.zeros(shape=(400, 400), dtype='uint8')

square = cv.rectangle(blank.copy(), pt1=(50, 50), pt2=(350, 350), color=255, thickness=cv.FILLED)
circle = cv.circle(blank.copy(), center=(200, 200), radius=180, color=255, thickness=cv.FILLED)
cv.imshow('square', square)
cv.imshow('circle', circle)

bitwise_and = cv.bitwise_and(square, circle)
cv.imshow('Bitwise AND', bitwise_and)

bitwise_or = cv.bitwise_or(square, circle)
cv.imshow('Bitwise OR', bitwise_or)

bitwise_xor = cv.bitwise_xor(square, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

bitwise_not_square = cv.bitwise_not(square)
cv.imshow('Bitwise NOT Square', bitwise_not_square)

bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT Circle', bitwise_not_circle)

cv.waitKey(0)
