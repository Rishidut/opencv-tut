import cv2 as cv
import numpy as np
#Blurring basically reduces the number of contour lines
img=cv.resize(cv.imread('pokeon.jpg'), (0,0), fx=0.2, fy=0.2,interpolation=cv.INTER_AREA)
blank=np.zeros(img.shape, dtype='uint8')
im=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', im)
ret, thresh=cv.threshold(im, 288, 255, cv.THRESH_BINARY)#basically binaries an image
blur=cv.GaussianBlur(im,(5,5),cv.BORDER_DEFAULT)
cv.imshow('binarised_image',thresh)
cn=cv.Canny(img,125,175)
cv.imshow('Edges',cn)

contours, heirarchy=cv.findContours(cn,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv.drawContours(blank, contours,-1,(255,0,0), thickness=1)
cv.imshow('Blank',blank)
cv.waitKey(0)
