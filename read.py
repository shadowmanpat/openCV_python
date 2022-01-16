import cv2 as cv

from rescale import rescaleFrame

img = cv.imread('Resources/Photos/cat.jpg')
resized_image = rescaleFrame(img)
cv.imshow('Cat', resized_image)
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_sized = rescaleFrame(frame,scale = 0.2)

    cv.imshow('Video', frame_sized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()

cv.destroyAllWindows()
# cv.waitKey(0)

