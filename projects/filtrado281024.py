import numpy as np
import cv2 as cv

# Cargar la imagen en escala de grises
img = cv.imread('resources/imagen2.jpg', 0)

# Obtener el tamaño de la imagen
y, x = img.shape

# Definir el factor de escala
scale_x, scale_y = 1.2, 1.2

# Crear una nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

scaled_y, scaled_x = scaled_img.shape
print(f'scaled_y: {int(scaled_y)}, scaled_x: {int(scaled_x)}')
# Aplicar el escalado
for i in range(int(x * scale_y)):
    for j in range(int(y * scale_x)):
        orig_x = int(i / scale_y)
        orig_y = int(j / scale_x)
        if 0 <= orig_x < x and 0 <= orig_y < y:
            scaled_img[i, j] = img[orig_x, orig_y]

cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada (modo raw)', scaled_img)
after_filter = scaled_img

for i in range(int(scaled_x)):
    for j in range(int(scaled_y)):
        if(after_filter[i,j] <= 20 and i > 1 and j> 1 and i < scaled_x-1 and j < scaled_y-1):
                print('Entra al filtrado')
                derecha =int(after_filter[i+1,j]*(1/9))
                izquierda =int(after_filter[i-1,j]*(1/9))
                izquierda_arriba =int(after_filter[i-1,j-1]*(1/9))
                derecha_abajo =int(after_filter[i+1,j+1]*(1/9))
                derecha_arriba =int(after_filter[i+1,j-1]*(1/9))
                izquierda_abajo =int(after_filter[i-1,j+1]*(1/9))

                after_filter[i,j] = derecha+izquierda+izquierda_arriba+izquierda_abajo+derecha_arriba+derecha_abajo



# Mostrar la imagen original y la escalada

cv.imshow('Imagen despues del filtro', after_filter)

cv.waitKey(0)
cv.destroyAllWindows()