#Dibujar con OpenCV y NumPy
import cv2 as cv
import numpy as np

# Crear una imagen en blanco
img = np.ones((3751, 5938, 3), np.uint8)*255

# Imagen guia
# img = cv.imread('resources/ejemplo.jpg', 3)

# Escalar la imagen
scale_x, scale_y = 0.1, 0.1
prey, prex, _ = img.shape
print(f'Tamaño de la imagen: {prex}x{prey}')

img = cv.resize(img, None, fx=scale_x, fy=scale_y)

# Obtener el tamaño de la imagen
y, x, z = img.shape

print(f'Tamaño de la imagen: {x}x{y}')

posicion_linea_horizonte_y = (y // 2) + (y // 4)

cielo_inicio =( 174, 66, 137)
cielo_final = (149, 150, 254)

purpura_inicio = (184, 46, 254)

purpura_final = (111, 34, 98)

principal_montain = (229, 128, 196)

secondary_montain = (180, 60, 125)

# Cielo
for yp in range(posicion_linea_horizonte_y):
    r = int(cielo_inicio[0] + (cielo_final[0] - cielo_inicio[0]) * (yp / posicion_linea_horizonte_y))
    g = int(cielo_inicio[1] + (cielo_final[1] - cielo_inicio[1]) * (yp / posicion_linea_horizonte_y))
    b = int(cielo_inicio[2] + (cielo_final[2] - cielo_inicio[2]) * (yp / posicion_linea_horizonte_y))
    
    img[yp, :] = [r, g, b]
    
#Sol
cv.circle(img, (int(x/2), int(y/2)), 150, (95, 215, 255), -1)

# Agua
for yp in range(y - posicion_linea_horizonte_y):
    r = int(purpura_inicio[0] + (purpura_final[0] - purpura_inicio[0]) * (yp / (y - posicion_linea_horizonte_y)))
    g = int(purpura_inicio[1] + (purpura_final[1] - purpura_inicio[1]) * (yp / (y - posicion_linea_horizonte_y)))
    b = int(purpura_inicio[2] + (purpura_final[2] - purpura_inicio[2]) * (yp / (y - posicion_linea_horizonte_y)))
    
    img[yp + posicion_linea_horizonte_y, :] = [r, g, b]




# Nubes
def dibujarNube(x, y):
    randomX = np.random.randint(20, x-20)
    randomY = np.random.randint(20, posicion_linea_horizonte_y-20)
    randomSize = np.random.randint(10, 40)
    cv.circle(img, (randomX, randomY), randomSize, (239, 251, 255), -1)

for i in range(8):
    dibujarNube(x, posicion_linea_horizonte_y)
    


# Dibujar montañas
montainTwo = np.array([
                [x/2, posicion_linea_horizonte_y],
                [3*x/4, posicion_linea_horizonte_y/2+20],
                [x, posicion_linea_horizonte_y]
                ], np.int32)

# Cambiar la forma del arreglo
montainTwo = montainTwo.reshape((-1, 1, 2))

# Dibujar el polígono
cv.fillPoly(img, [montainTwo], secondary_montain)

snowTwo = np.array([
                [3*x/4, posicion_linea_horizonte_y/2+20],
                [(3*x/4)-25, posicion_linea_horizonte_y/2+40],
                [(3*x/4)+25, posicion_linea_horizonte_y/2+40],
                [3*x/4, posicion_linea_horizonte_y/2+20]
                ], np.int32)

# Cambiar la forma del arreglo
snowTwo = snowTwo.reshape((-1, 1, 2))

# Dibujar el polígono

cv.fillPoly(img, [snowTwo], (255, 255, 255))

###########################

montainThree = np.array([
                [x/2, posicion_linea_horizonte_y],
                [x/4, posicion_linea_horizonte_y/2+20],
                [0, posicion_linea_horizonte_y]
                ], np.int32)

# Cambiar la forma del arreglo
montainThree = montainThree.reshape((-1, 1, 2))

# Dibujar el polígono
cv.fillPoly(img, [montainThree], secondary_montain)

snowThree = np.array([
                [x/4, posicion_linea_horizonte_y/2+20],
                [x/4-25, posicion_linea_horizonte_y/2+40],
                [x/4+25, posicion_linea_horizonte_y/2+40],
                [x/4, posicion_linea_horizonte_y/2+20]
                ], np.int32)

# Cambiar la forma del arreglo
snowThree = snowThree.reshape((-1, 1, 2))

# Dibujar el polígono

cv.fillPoly(img, [snowThree], (255, 255, 255))


############################



montainPrincipal = np.array([
                [x/4, posicion_linea_horizonte_y],
                [x/2, posicion_linea_horizonte_y/2],
                [3*x/4, posicion_linea_horizonte_y]
                ], np.int32)

# Cambiar la forma del arreglo
montainPrincipal = montainPrincipal.reshape((-1, 1, 2))

# Dibujar el polígono
cv.fillPoly(img, [montainPrincipal], principal_montain)

snowPrincipal = np.array([
                [x/2, posicion_linea_horizonte_y/2],
                [x/2-25, posicion_linea_horizonte_y/2+20],
                [x/2+25, posicion_linea_horizonte_y/2+20],
                [x/2, posicion_linea_horizonte_y/2]
                ], np.int32)

# Cambiar la forma del arreglo
snowPrincipal = snowPrincipal.reshape((-1, 1, 2))

# Dibujar el polígono

cv.fillPoly(img, [snowPrincipal], (255, 255, 255))

###########################




# Dibujar "arboles"
trees = []
for i in range(0, x, 30):
    height = np.random.randint(20, 100)
    base = np.random.randint(10, 30)
    trees.append([i, posicion_linea_horizonte_y])
    trees.append([i + base // 2, posicion_linea_horizonte_y - height])
    trees.append([i + base, posicion_linea_horizonte_y])

trees = np.array(trees, np.int32)

# Cambiar la forma del arreglo
trees = trees.reshape((-1, 1, 2))

cv.fillPoly(img, [trees], purpura_final)







#Mostrar la imagen en una ventana
cv.imshow('Imagen en Blanco', img)
cv.waitKey(0)
cv.destroyAllWindows()