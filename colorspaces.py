import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.resize(cv.imread('pokeon.jpg'), (0,0), fx=0.2, fy=0.2,interpolation=cv.INTER_AREA)
blank=np.zeros(img.shape, dtype='uint8')
im=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', im)
#CONVERTING BGR TO HSV format(HUE SATURATION VALUE)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV_image',hsv)
#CONVERTING BGR TO LAB format()
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB_image',rgb)
cv.imshow('LAB_image',lab)
plt.imshow(rgb)
plt.show()
#MATPLOTLIB basically displays an rgb image so there's an inversion of color