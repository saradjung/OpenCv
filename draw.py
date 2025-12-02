import cv2 as cv
import numpy as np

rand_img=np.zeros(shape=(500,500,3))

# cv.imshow('img',rand_img)
# rand_img[:]=0,0,255
# cv.imshow('img1',rand_img)

cv.rectangle(rand_img,pt1=(0,0),pt2=(500,250),color=(0,255,0),thickness=cv.FILLED)
cv.imshow('rectangel',rand_img)

cv.circle(rand_img,center=(250,250),radius=50,color=(255,0,0),thickness=cv.FILLED)
cv.imshow('circle',rand_img)

cv.line(rand_img,pt1=(10,10),pt2=(250,251),color=(0,255,255),thickness=4)
cv.imshow('line',rand_img)

cv.putText(rand_img,text="hello my guy", org=(250,250),thickness=4, fontFace=cv.FONT_HERSHEY_SCRIPT_COMPLEX, fontScale=1.0 ,color=(255,255,255))
cv.imshow('text',rand_img)
cv.waitKey(0)