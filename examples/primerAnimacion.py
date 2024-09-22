import numpy as np
import cv2

# Función para generar un solo punto de la elipse en función del parámetro t
def generar_punto_elipse(a, b, t):
    x = int(a * np.cos(t) + 300)  # Desplazamiento para centrar
    y = int(b * np.sin(t) + 300)
    return (x, y)

# Dimensiones de la imagen
img_width, img_height = 600, 600

# Crear una imagen en blanco
imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

# Parámetros de la elipse
a = 200  # Semieje mayor
b = 100  # Semieje menor
num_puntos = 1000

# Crear los valores del parámetro t para la animación
t_vals = np.linspace(0, 2 * np.pi, num_puntos)

# Bucle de animación
for t in t_vals:
    # Crear una nueva imagen en blanco en cada iteración
    imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)
    
    # Generar el punto en la elipse
    punto = generar_punto_elipse(a, b, t)
    
    # Dibujar el punto en la elipse
    cv2.circle(imagen, punto, radius=5, color=(0, 255, 0), thickness=-1)
    
    # Dibujar la trayectoria completa de la elipse (opcional, si quieres ver toda la elipse)
    for t_tray in t_vals:
        pt_tray = generar_punto_elipse(a, b, t_tray)
        cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)
    
    # Mostrar la imagen con el punto en movimiento
    cv2.imshow('img', imagen)
    
    # Controlar la velocidad de la animación (en milisegundos)
    cv2.waitKey(10)

# Cerrar la ventana después de la animación
cv2.destroyAllWindows()