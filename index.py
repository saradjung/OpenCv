import cv2 as cv
# reading images
image=cv.imread('Static/ghost.png')

cv.imshow('Ghost', image)

# # cv.waitKey(0)

# def resize_fun(frame, scale=0.75):
#     height=int(frame.shape[0] *scale)
#     width= int(frame.shape[1]* scale)

#     dimension=(width, height)

#     return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# # captureVid=cv.VideoCapture('Static/test.mp4')

# # while True:
# #     isTrue, frame= captureVid.read()

# #     frame_resized=resize_fun(frame)
# #     cv.imshow('Video',frame)
# #     cv.imshow('vid1',frame_resized)
# #     if cv.waitKey(20) & 0xFF== ord('d'):
# #         break
# #captureVid.release()
# # cv.destroyAllWindows()

# im_resized=resize_fun(image)
# cv.imshow('im1',im_resized)
# cv.waitKey(0)
# # 

# gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

# cv.imshow('colorchange',gray)

# blur=cv.GaussianBlur(image,(3,3),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

#edge cascade
# edge=cv.Canny(image,(100),(200))
# cv.imshow('Edge',edge)

# dilated=cv.dilate(edge,(3,3),iterations=3)
# cv.imshow('Dilated',dilated)

# eroded=cv.erode(dilated,(3,3),iterations=3)
# cv.imshow('eroded',eroded)

cropped=image[20:250,40:300]
cv.imshow("Cropeed",cropped)

resized=cv.resize(image,(200,300),interpolation=cv.INTER_BITS)
cv.imshow("resized,",resized)

cv

cv.waitKey(0)