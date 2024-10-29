import numpy as np
import cv2 as cv

# Cargar la imagen en escala de grises
img = cv.imread('resources/imagen2.jpg', 0)

# Obtener el tamaño de la imagen
y, x = img.shape

# Definir el factor de escala
scale_x, scale_y = 1, 1

# Crear una nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)


# Aplicar el escalado
for i in range(int(x * scale_y)):
    for j in range(int(y * scale_x)):
        orig_x = int(i / scale_y)
        orig_y = int(j / scale_x)
        if 0 <= orig_x < x and 0 <= orig_y < y:
            if(scaled_img[i,j] < 20 and i > 1 and j> 1 and i < scale_x and scale_y):
                derecha =int(scaled_img[i+1,j]*(1/9))
                izquierda =int(scaled_img[i-1,j]*(1/9))
                izquierda_arriba =int(scaled_img[i-1,j-1]*(1/9))
                derecha_abajo =int(scaled_img[i+1,j+1]*(1/9))
                derecha_arriba =int(scaled_img[i+1,j-1]*(1/9))
                izquierda_abajo =int(scaled_img[i-1,j+1]*(1/9))
                scaled_img[i,j] = derecha+izquierda+izquierda_arriba+izquierda_abajo+derecha_arriba+derecha_abajo
            else:
                scaled_img[i, j] = img[orig_x, orig_y]



# Mostrar la imagen original y la escalada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada (modo raw)', scaled_img)
cv.waitKey(0)
cv.destroyAllWindows()