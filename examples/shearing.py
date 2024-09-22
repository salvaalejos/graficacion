import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('resources/imagen2.jpg', 0)

# Obtener el tamaño de la imagen
x, y = img.shape

# Definir el factor de cizallamiento
shear_factor = 0.5

# Crear la matriz de cizallamiento
M = np.float32([[1, shear_factor, 0], [0, 1, 0]])

# Aplicar el cizallamiento usando warpAffine
sheared_img = cv.warpAffine(img, M, (y, x))

# Mostrar la imagen original y la cizallada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Cizallada', sheared_img)
cv.waitKey(0)
cv.destroyAllWindows()