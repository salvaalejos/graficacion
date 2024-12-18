# Practica donde se rota (a 60°), escala y traslada una imagen con OpenCV

import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('resources/imagen2.jpg', 0)

# Obtener el tamaño de la imagen
x, y = img.shape

# Calcular el centro de la imagen
center = (y // 2, x // 2)

####################  Rotacion ########################

# Definir el ángulo de rotación (en grados)
angle = 60

# Crear la matriz de rotación
M = cv.getRotationMatrix2D(center, angle, 1.0)

# Aplicar la rotación usando warpAffine
rotated_img = cv.warpAffine(img, M, (y, x))
finalImg = rotated_img

####################  Escala ########################

# Definir el factor de escala
scale_x, scale_y = 0.5, 0.5

# Aplicar el escalado usando cv.resize()
scaled_img = cv.resize(img, None, fx=scale_x, fy=scale_y)
finalImg = cv.resize(finalImg, None, fx=scale_x, fy=scale_y)

####################  Traslacion ########################

# Obtener el tamaño de la imagen final
xf, yf = finalImg.shape

# Definir el desplazamiento en x e y
dx, dy = 100, 100

# Crear la matriz de traslación
M = np.float32([[1, 0, dx], [0, 1, dy]])

# Aplicar la traslación usando warpAffine
translated_img = cv.warpAffine(img, M, (y, x))
finalImg = cv.warpAffine(finalImg, M, (yf, xf))

# Mostrar la imagen original y la trasladada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Rotada', rotated_img)
cv.imshow('Imagen Escalada', scaled_img)
cv.imshow('Imagen Trasladada', translated_img)
cv.imshow('Imagen Final', finalImg)
cv.waitKey(0)
cv.destroyAllWindows()