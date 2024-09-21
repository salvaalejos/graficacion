import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('resources/imagen2.jpg', 0)

# Obtener el tamaño de la imagen
x, y = img.shape

# Crear una imagen vacía para la traslación
translated_img = np.zeros((x, y), dtype=np.uint8)

# Definir el desplazamiento en x e y
dx, dy = 100, 50

# Trasladar la imagen
for i in range(x):
    for j in range(y):
        new_x = i + dy
        new_y = j + dx
        if 0 <= new_x < x and 0 <= new_y < y:
            translated_img[new_x, new_y] = img[i, j]

# Mostrar la imagen original y la trasladada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Trasladada', translated_img)
cv.waitKey(0)
cv.destroyAllWindows()