import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

img = cv.imread('Resources/Photos/cat.jpg')
# blank[:] = 0,255,0
# cv.imshow('Green',blank)
# cv.imshow('Blank',img)
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-2)


cv.circle(blank, (250,250), 40, (0,0,250), thickness=3)
cv.line(blank, (0,0),(250,250),(255,255,255), thickness=3)
cv.putText(blank,"Hello from python and openCV", (250,250), cv.FONT_HERSHEY_TRIPLEX,1.0, (0,255,0), 2)

# cv.line(blank, (250,250), 40, (0,0,250),(255,255,255), thickness=4)
cv.imshow('Blank',blank)
cv.waitKey(0)