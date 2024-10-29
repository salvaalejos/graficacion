import cv2 as cv
import numpy as np

imagen = cv.imread("resources/imagen2.jpg", 1)

imagenHSV = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)

bajo_rojo1 = np.array([0,40,40])
alto_rojo1 = np.array([10,255,255])
bajo_rojo2 = np.array([160,40,40])
alto_rojo2 = np.array([180,255,255])

mascara_rojo1 = cv.inRange(imagenHSV, bajo_rojo1, alto_rojo1)
mascara_rojo2 = cv.inRange(imagenHSV, bajo_rojo2, alto_rojo2)

mascara_rojo = cv.add(mascara_rojo1, mascara_rojo2)

imagen_gris = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)

imagen_gris_bgr = cv.cvtColor(imagen_gris, cv.COLOR_GRAY2BGR)

resultado = np.where(mascara_rojo[:,:,None] == 255, imagen, imagen_gris_bgr)

cv.imshow('Color resaltado', resultado)
cv.imshow('Mascara roja', mascara_rojo)
cv.imshow('Original', imagen)
cv.imshow('Gris BGR', imagen_gris_bgr)
cv.waitKey(0)
cv.destroyAllWindows()
