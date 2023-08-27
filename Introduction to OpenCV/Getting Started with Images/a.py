import cv2 as cv
import sys
import os

path = os.getcwd()
path += "\\Introduction to OpenCV\\Getting Started with Images\\"

img = cv.imread(cv.samples.findFile(path + "starry_night.jpg"))
if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite(path + "starry_night.png", img)