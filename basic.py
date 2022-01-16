import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')

# cv.imshow('Cat', img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

canny = cv.Canny(blur,125,175)
cv.imshow('canny', canny)

dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dilated', dilated)

eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)


resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)