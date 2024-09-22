import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('resources/imagen2.jpg', 0)

# Obtener el tamaño de la imagen
x, y = img.shape

# Crear una imagen vacía para la reflexión
reflected_img = np.zeros((x, y), dtype=np.uint8)

op = input("Escoja una opcion que quiera visualizar:\n1. Horizontal\t2. Vertical\n")

if op == "1":
    # Aplicar la reflexión horizontal
    for i in range(x):
        for j in range(y):
            reflected_img[i, y - j - 1] = img[i, j]

    # Mostrar la imagen original y la reflejada
    cv.imshow('Imagen Original', img)
    cv.imshow('Imagen Reflejada Horizontalmente (modo raw)', reflected_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
elif op == "2":
    # Aplicar la reflexión vertical
    for i in range(x):
        for j in range(y):
            reflected_img[x - i - 1, j] = img[i, j]
else:
    print("Opción inválida")

    # Mostrar la imagen original y la reflejada
    cv.imshow('Imagen Original', img)
    cv.imshow('Imagen Reflejada Verticalmente (modo raw)', reflected_img)
    cv.waitKey(0)
    cv.destroyAllWindows()