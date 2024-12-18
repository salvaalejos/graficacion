# Sistema solar

import numpy as np
import cv2

# Función para generar un solo punto de la elipse en función del parámetro t
def generar_punto_elipse(a, b, t):
    x = int(a * np.cos(t) + 400)  # Desplazamiento para centrar
    y = int(b * np.sin(t) + 400)
    return (x, y)

# Dimensiones de la imagen
img_width, img_height = 800, 800

# Crear una imagen en blanco
imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

# Parámetros de la elipse
a = 200  # Semieje mayor
b = 100  # Semieje menor
num_puntos = 1000

a2 = 100
b2 = 50

a5 = 150
b5 = 75

a3 = 300
b3 = 150

a4 = 350
b4 = 200


# Crear los valores del parámetro t para la animación
t_vals = np.linspace(0, 2 * np.pi, num_puntos)


# Bucle de animación
for t in t_vals:
    # Crear una nueva imagen en blanco en cada iteración
    imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

    #Sol
    cv2.circle(imagen, ( int (img_width/2), int (img_height/2)), 50, (0,200,200), -1)
    
    # Generar el punto en la elipse
    punto = generar_punto_elipse(a, b, t) 
    punto2 = generar_punto_elipse(a2,b2,t)
    punto3 = generar_punto_elipse(a3,b3,t)
    punto4 = generar_punto_elipse(a4,b4,t)
    punto5 = generar_punto_elipse(a5,b5,t)
    
    # Dibujar el punto en la elipse
    cv2.circle(imagen, punto, radius=5, color=(0, 255, 0), thickness=-1)
    cv2.circle(imagen, punto2, 5, (200,10,10),-1)
    cv2.circle(imagen, punto3, 5, (10,10,200),-1)
    cv2.circle(imagen, punto4, 5, (10,100,100),-1)
    cv2.circle(imagen, punto5, 5, (200,10,200),-1)
    
    # Dibujar la trayectoria completa de la elipse (opcional, si quieres ver toda la elipse)
    for t_tray in t_vals:
        pt_tray = generar_punto_elipse(a, b, t_tray)
        pt_tray2 = generar_punto_elipse(a2,b2,t_tray)
        pt_tray3 = generar_punto_elipse(a3,b3,t_tray)
        pt_tray4 = generar_punto_elipse(a4,b4,t_tray)
        pt_tray5 = generar_punto_elipse(a5,b5,t_tray)
        
        cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)
        cv2.circle(imagen, pt_tray2, 1, (255,255,255),-1)
        cv2.circle(imagen, pt_tray3, 1, (255,255,255),-1)
        cv2.circle(imagen, pt_tray4, 1, (255,255,255),-1)
        cv2.circle(imagen, pt_tray5, 1, (255,255,255),-1)
    
    for i in range(30):
        xran = np.random.randint(0,img_width-1)
        yran = np.random.randint(0,img_height-1)
        cv2.circle(imagen,(xran,yran),1,(250,250,240))

    # Mostrar la imagen con el punto en movimiento
    cv2.imshow('img', imagen)
    
    # Controlar la velocidad de la animación (en milisegundos)
    cv2.waitKey(10)

# Cerrar la ventana después de la animación
cv2.destroyAllWindows()