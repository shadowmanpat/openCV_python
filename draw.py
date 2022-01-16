import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank',blank)
img = cv.imread('Resources/Photos/cat.jpg')
blank[:] = 0,255,0
cv.imshow('Green',blank)
# cv.imshow('Blank',img)
cv.waitKey(0)