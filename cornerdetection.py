import numpy as np
import cv2 as cv
import random
# basically detects the corners using Shi-Tomashi Algorithm
img =cv.imread('chessboard-queen.png')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
corners=cv.goodFeaturesToTrack(gray, 80, 0.01, 10)
list=np.int0(corners)
print(list)

for corner in corners:
    x,y=corner.ravel()
    circle=cv.circle(img, (x,y), 10, (255, 0,0), -1)
    
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        cor1=tuple(corners[i][0])
        cor2=tuple(corners[j][0])
        color=tuple(map(lambda x: int(x),np.random.randint(0,255, size=3)))
        cv.line(img, cor1, cor2, color, 1)
        

cv.imshow('Corners_image', img)
cv.waitKey(0)
cv.destroyAllWindows()