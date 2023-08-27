import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
#선(위치,각도,색)
cv.line(img,(0,0),(511,511),(255,0,0),5)
#오른쪽위사각형
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
#원(위치,크기,색,색칠?)
cv.circle(img,(447,63), 63, (0,0,255), -1)
#반원(위치,크기,각도,색칠?)
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

cv.imshow("Display window", img)

k = cv.waitKey(0)
cv.destroyAllWindows()