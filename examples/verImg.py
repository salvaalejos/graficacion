import cv2 as cv
import numpy as np

img = cv.imread('resources\imagen1.jpg')

cv.imshow('Imagen', img)
cv.waitKey(0)
cv.destroyAllWindows()
