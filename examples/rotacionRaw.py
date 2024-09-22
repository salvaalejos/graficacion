import cv2 as cv
import numpy as np
import math

# Cargar la imagen en escala de grises
img = cv.imread('resources/imagen2.jpg', 0)

# Obtener el tamaño de la imagen
x, y = img.shape

# Crear una imagen vacía para almacenar el resultado
rotated_img = np.zeros((x, y), dtype=np.uint8)
xx, yy = rotated_img.shape
# Calcular el centro de la imagen
cx, cy = int(x  // 2), int(y  // 2)

# Definir el ángulo de rotación (en grados) y convertirlo a radianes
angle = 45
theta = math.radians(angle)

# Rotar la imagen
for i in range(x):
    for j in range(y):
        new_x = int((j - cx) * math.cos(theta) - (i - cy) * math.sin(theta) + cx)
        new_y = int((j - cx) * math.sin(theta) + (i - cy) * math.cos(theta) + cy)
        if 0 <= new_x < y and 0 <= new_y < x:
            rotated_img[new_y, new_x] = img[i, j]

# Mostrar la imagen original y la rotada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Rotada (modo raw)', rotated_img)
cv.waitKey(0)
cv.destroyAllWindows()