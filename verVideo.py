import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

while(True):
    ret, img = cap.read()
    if ret:
        cv.imshow('video', img)
        img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        w,h = img2.shape
        img3=255-img2
        cv.imshow('img2', img2)
        cv.imshow('hsv', hsv)
        cv.imshow('img3', img3)
        
        k =cv.waitKey(1) & 0xFF
        if k == 27 :
            break
    else:
        break
    
cap.release()
cv.destroyAllWindows()