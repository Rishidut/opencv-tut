import cv2 as cv
import numpy as np
capture=cv.VideoCapture(0)
# this resize only works on live videos
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)
#changes the resolution of already existing videos or webcam.
def rescaleframe(frame, scale=0.2):
    width=int(frame.shape[1]*scale)# shape[1] basically specifies the width of the corresponding frame
    height=int(frame.shape[0]*scale)# shape[0] basically specifies the height of the corresponding frame
    dim=(width,height)#creates a tuple
    
    return cv.resize(frame,dim, interpolation=cv.INTER_AREA)

while True:
    istrue,frame=capture.read()
    frame_resized=rescaleframe(frame,scale=0.6)
    cv.imshow('video',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('q'):
       break
   
capture.release()
cv.destroyAllWindows()