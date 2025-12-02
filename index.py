import cv2 as cv
# reading images
image=cv.imread('Static/ghost.png')

cv.imshow('Ghost', image)

# cv.waitKey(0)

def resize_fun(frame, scale=0.75):
    height=int(frame.shape[0] *scale)
    width= int(frame.shape[1]* scale)

    dimension=(width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# captureVid=cv.VideoCapture('Static/test.mp4')

# while True:
#     isTrue, frame= captureVid.read()

#     frame_resized=resize_fun(frame)
#     cv.imshow('Video',frame)
#     cv.imshow('vid1',frame_resized)
#     if cv.waitKey(20) & 0xFF== ord('d'):
#         break
#captureVid.release()
# cv.destroyAllWindows()

im_resized=resize_fun(image)
cv.imshow('im1',im_resized)
cv.waitKey(0)
# 
