import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('resources/imagen2.jpg', 0)

# Obtener el tamaño de la imagen
x, y = img.shape

# Definir el desplazamiento en x e y
dx, dy = 100, 100

# Crear la matriz de traslación
M = np.float32([[1, 0, dx], [0, 1, dy]])

# Aplicar la traslación usando warpAffine
translated_img = cv.warpAffine(img, M, (y, x))

# Mostrar la imagen original y la trasladada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Trasladada', translated_img)
cv.waitKey(0)
cv.destroyAllWindows()