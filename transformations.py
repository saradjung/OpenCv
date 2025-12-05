import cv2 as cv
import numpy as npd

img=cv.imread('Static/ghost.png')

# cv.imshow("image",img)

# print(img.shape)

# def translate(image,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])
#     dim=(image.shape[1],image.shape[0])
#     return cv.warpAffine(image,transMat,dim)

# translted=translate(img,100,100)

# cv.imshow("translated",translted)
#ROTATION
# def rotate(image, angle, rotpoint=None):
#     (height,width)=image.shape[:2]
#     if rotpoint is None:
#         rotpoint= (width//2,height//2)
    
#     rotmatrix=cv.getRotationMatrix2D(rotpoint,angle,1.0)
#     dims=(width, height)
#     return cv.warpAffine(image,rotmatrix,dims)

# rotated=rotate(img,-45)
# cv.imshow("rotated",rotated)

#FLIPPING
flipped=cv.flip(img,-1)
cv.imshow("flipped",flipped)









cv.waitKey(0)