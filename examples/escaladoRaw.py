import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('resources/imagen2.jpg', 0)

# Obtener el tamaño de la imagen
y, x = img.shape

# Definir el factor de escala
scale_x, scale_y = 0.5, 0.5

# Crear una nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

# Aplicar el escalado
for i in range(int(x * scale_y)):
    for j in range(int(y * scale_x)):
        orig_x = int(i / scale_y)
        orig_y = int(j / scale_x)
        if 0 <= orig_x < x and 0 <= orig_y < y:
            scaled_img[i, j] = img[orig_x, orig_y]

# Mostrar la imagen original y la escalada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada (modo raw)', scaled_img)
cv.waitKey(0)
cv.destroyAllWindows()