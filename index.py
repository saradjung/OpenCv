import cv2 as cv
# reading images
# image=cv.imread('Static/ghost.png')

# cv.imshow('Ghost', image)

# cv.waitKey(0)
captureVid=cv.VideoCapture('Static/test.mp4')

while True:
    isTrue, frame= captureVid.read()

    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF== ord('d'):
        break

captureVid.release()
cv.destroyAllWindows()
