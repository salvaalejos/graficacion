import numpy as np
import cv2

# Dimensiones de la imagen
img_width, img_height = 800, 800

# Crear una imagen en blanco
imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

#################################### BATMAN ####################################
def batman():
    # Función para calcular y plotear la forma matemática
    def calcular_forma(x):
        w = 3 * np.sqrt(np.maximum(0, 1 - (x / 7)**2))
        l = (6 / 7) * np.sqrt(10) + (3 + x) / 2 - (3 / 7) * np.sqrt(10) * np.sqrt(np.maximum(0, 4 - (x + 1)**2))
        h = (1 / 2) * (3 * (abs(x - 1 / 2) + abs(x + 1 / 2) + 6) - 11 * (abs(x - 3 / 4) + abs(x + 3 / 4)))
        r = (6 / 7) * np.sqrt(10) + (3 - x) / 2 - (3 / 7) * np.sqrt(10) * np.sqrt(np.maximum(0, 4 - (x - 1)**2))
        y1 = w + (l - w) * (x >= -3) + (h - l) * (x >= -1) + (r - h) * (x >= 1) + (w - r) * (x >= 3)
        y2 = (1 / 2) * (3 * np.sqrt(np.maximum(0, 1 - (x / 7)**2)) + np.sqrt(np.maximum(0, 1 - (abs(abs(x) - 2) - 1)**2)) + abs(x / 2) - ((3 * np.sqrt(33) - 7) / 112) * x**2 - 3) * ((x + 4) / abs(x + 4) - (x - 4) / abs(x - 4)) - 3 * np.sqrt(np.maximum(0, 1 - (x / 7)**2))
        return y1, y2

    # Crear los valores de x para la gráfica
    x_vals = np.linspace(-7, 7, 1000)

    # Variables para escalar y trasladar la gráfica a la imagen
    scale_x = 50
    scale_y = 50
    offset_x = img_width // 2
    offset_y = img_height // 2

    # Dibujar la gráfica en la imagen
    for x in x_vals:
        y1, y2 = calcular_forma(x)
        # Convertir coordenadas a píxeles
        if not np.isnan(y1) and not np.isnan(y2):
            pt1 = (int(scale_x * x + offset_x), int(-scale_y * y1 + offset_y))
            pt2 = (int(scale_x * x + offset_x), int(-scale_y * y2 + offset_y))
            # Dibujar puntos en la imagen
            cv2.circle(imagen, pt1, 1, (0, 255, 255), -1)
            cv2.circle(imagen, pt2, 1, (0, 255, 255), -1)

################################################################################

############################# CORAZON #######################################

def corazon():
    # Función para calcular puntos de la curva paramétrica
    def calcular_puntos(t):
        x = 16 * np.sin(t)**3
        y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
        return x, y

    # Crear los valores del parámetro t para la gráfica
    t_vals = np.linspace(0, 2 * np.pi, 1000)

    # Variables para escalar y trasladar la curva a la imagen
    scale_x = 10
    scale_y = 10
    offset_x = img_width // 2
    offset_y = img_height // 2

    # Dibujar la curva en la imagen
    for t in t_vals:
        x, y = calcular_puntos(t)
        # Convertir coordenadas a píxeles
        pt = (int(scale_x * x + offset_x), int(-scale_y * y + offset_y))
        # Dibujar puntos en la imagen
        cv2.circle(imagen, pt, 1, (128,0,255), -1)

################################################################################

########################## ESTRELLA #####################################
        
def estrella():
    # Centro de la figura
    centro_x, centro_y = img_width // 2, img_height // 2

    # Función paramétrica para la estrella
    def parametric_curve(t):
        x = np.cos(t) * (1 - 0.5 * np.cos(5 * t))
        y = np.sin(t) * (1 - 0.5 * np.cos(5 * t))
        return x, y

    # Crear rango de valores para t (0 a 2pi para una vuelta completa)
    t_vals = np.linspace(0, 2 * np.pi, 1000)

    # Dibujar la curva
    for t in t_vals:
        # Calcular las coordenadas paramétricas
        x, y = parametric_curve(t)

        # Convertir coordenadas a píxeles
        px = int(centro_x + x * 200)  # Multiplicar por un factor de escala
        py = int(centro_y - y * 200)

        # Dibujar el punto en la imagen
        if 0 <= px < img_width and 0 <= py < img_height:  # Asegurarse de que el punto esté dentro de los límites
            cv2.circle(imagen, (px, py), radius=1, color=(50, 200, 255), thickness=-1)  # Estrella en rojo
            
################################################################################

######################## CICLOIDE #######################################

def cicloide():
    # Centro de la figura
    centro_x, centro_y = img_width//4, img_height // 2

    # Definir el valor de R (puedes cambiar este valor para modificar el tamaño)
    R = 20

    # Función paramétrica para la figura
    def parametric_curve(phi):
        x = R * (phi + np.sin(phi))
        y = R * (1 - np.cos(phi))
        return x, y

    # Crear rango de valores para φ (de 0 a 2π para una vuelta completa)
    phi_vals = np.linspace(0, 8 * np.pi, 1000)

    # Dibujar la curva
    for phi in phi_vals:
        # Calcular las coordenadas paramétricas
        x, y = parametric_curve(phi)

        # Convertir coordenadas a píxeles
        px = int(centro_x + x)  # Sin escalar porque ya se ajusta con R
        py = int(centro_y - y)

        # Dibujar el punto en la imagen
        if 0 <= px < img_width and 0 <= py < img_height:  # Asegurarse de que el punto esté dentro de los límites
            cv2.circle(imagen, (px, py), radius=1, color=(0, 255, 0), thickness=-1)  # Curva en verde

################################################################################

######################## ANIMACIÓN PARAMÉTRICA #######################################

def animacion_parametrica():
    # Función para generar un solo punto de la curva paramétrica en función del parámetro t
    def generar_punto_parametrica(a, b, t):
        x = (a - b) * np.cos(t) + np.cos(t * (a / b) - 1)
        y = (a - b) * np.sin(t) - np.sin(t * (a / b) - 1)
        return (int(x * 50 + 400), int(y * 50 + 400))  # Desplazamiento y escala para centrar

    # Crear los valores del parámetro t para la animación
    t_vals = np.linspace(0, 2 * np.pi, 1000)

    # Bucle de animación
    for i in range(200):  # Número de frames de la animación
        # Crear una nueva imagen en blanco en cada iteración
        imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

        # Ajustar los valores de a y b
        a = 5 + 2 * np.sin(i / 20.0)  # Variar a entre 3 y 7
        b = 3 + 2 * np.cos(i / 20.0)  # Variar b entre 1 y 5

        # Dibujar la curva paramétrica
        for t in t_vals:
            punto = generar_punto_parametrica(a, b, t)
            # Cambiar los colores en función de t
            blue = int(127 * (1 + np.sin(t)) + 128)
            green = int(127 * (1 + np.sin(t + 2 * np.pi / 3)) + 128)
            red = int(127 * (1 + np.sin(t + 4 * np.pi / 3)) + 128)
            cv2.circle(imagen, punto, 1, (blue, green, red), -1)
        # Mostrar la imagen con la curva paramétrica
        cv2.imshow('Curva Parametrica', imagen)

        # Controlar la velocidad de la animación (en milisegundos)
        cv2.waitKey(50)

    # Cerrar la ventana después de la animación
    cv2.destroyAllWindows()
    exit()
    
################################################################################

######################## INFINITO DE LEMNISCATA ################################
    
def lemniscata():
    # Función para calcular puntos de la lemniscata de Bernoulli
    def calcular_puntos(t):
        x = np.cos(t) / (1 + np.sin(t)**2)
        y = np.cos(t) * np.sin(t) / (1 + np.sin(t)**2)
        return x, y

    # Crear los valores del parámetro t para la gráfica
    t_vals = np.linspace(0, 2 * np.pi, 1000)

    # Variables para escalar y trasladar la curva a la imagen
    scale_x = 300
    scale_y = 300
    offset_x = img_width // 2
    offset_y = img_height // 2

    # Dibujar la curva en la imagen
    for t in t_vals:
        x, y = calcular_puntos(t)
        # Convertir coordenadas a píxeles
        pt = (int(scale_x * x + offset_x), int(-scale_y * y + offset_y))
        # Dibujar puntos en la imagen
        cv2.circle(imagen, pt, 1, (255, 0, 0), -1)
        
################################################################################

######################## ESPIRAL DE ARQUÍMEDES ################################

def espiral():
    # Función para calcular puntos de la espiral de Arquímedes
    def calcular_puntos(t):
        x = t * np.cos(t)
        y = t * np.sin(t)
        return x, y

    # Crear los valores del parámetro t para la gráfica
    t_vals = np.linspace(0, 4 * np.pi, 1000)

    # Variables para escalar y trasladar la curva a la imagen
    scale_x = 10
    scale_y = 10
    offset_x = img_width // 2
    offset_y = img_height // 2

    # Dibujar la curva en la imagen
    for t in t_vals:
        x, y = calcular_puntos(t)
        # Convertir coordenadas a píxeles
        pt = (int(scale_x * x + offset_x), int(-scale_y * y + offset_y))
        # Dibujar puntos en la imagen
        cv2.circle(imagen, pt, 1, (0, 255, 0), -1)
        
################################################################################

######################## HIPÓCICLOIDE ################################

def hipocicloide():
    # Parámetros de la hipocicloide
    a = 5
    b = 3

    # Función para calcular puntos de la hipocicloide
    def calcular_puntos(t):
        x = (a - b) * np.cos(t) + b * np.cos((a - b) / b * t)
        y = (a - b) * np.sin(t) - b * np.sin((a - b) / b * t)
        return x, y

    # Crear los valores del parámetro t para la gráfica
    t_vals = np.linspace(0, 2 * np.pi, 1000)

    # Variables para escalar y trasladar la curva a la imagen
    scale_x = 50
    scale_y = 50
    offset_x = img_width // 2
    offset_y = img_height // 2

    # Dibujar la curva en la imagen
    for t in t_vals:
        x, y = calcular_puntos(t)
        # Convertir coordenadas a píxeles
        pt = (int(scale_x * x + offset_x), int(-scale_y * y + offset_y))
        # Dibujar puntos en la imagen
        cv2.circle(imagen, pt, 1, (0, 0, 255), -1)
        
################################################################################

######################## ROSA DE 4 PÉTALOS ################################

def rosa():
    # Función para calcular puntos de la rosa de 4 pétalos
    def calcular_puntos(t):
        x = np.cos(2 * t) * np.cos(t)
        y = np.cos(2 * t) * np.sin(t)
        return x, y

    # Crear los valores del parámetro t para la gráfica
    t_vals = np.linspace(0, 2 * np.pi, 1000)

    # Variables para escalar y trasladar la curva a la imagen
    scale_x = 200
    scale_y = 200
    offset_x = img_width // 2
    offset_y = img_height // 2

    # Dibujar la curva en la imagen
    for t in t_vals:
        x, y = calcular_puntos(t)
        # Convertir coordenadas a píxeles
        pt = (int(scale_x * x + offset_x), int(-scale_y * y + offset_y))
        # Dibujar puntos en la imagen
        cv2.circle(imagen, pt, 1, (255, 0, 255), -1)
        
################################################################################

######################## CARDIODE ################################

def cardioide():
    # Función para calcular puntos de la cardioide
    def calcular_puntos(t):
        x = 2 * np.cos(t) - np.cos(2 * t)
        y = 2 * np.sin(t) - np.sin(2 * t)
        return x, y

    # Crear los valores del parámetro t para la gráfica
    t_vals = np.linspace(0, 2 * np.pi, 1000)

    # Variables para escalar y trasladar la curva a la imagen
    scale_x = 100
    scale_y = 100
    offset_x = img_width // 2
    offset_y = img_height // 2

    # Dibujar la curva en la imagen
    for t in t_vals:
        x, y = calcular_puntos(t)
        # Convertir coordenadas a píxeles
        pt = (int(scale_x * x + offset_x), int(-scale_y * y + offset_y))
        # Dibujar puntos en la imagen
        cv2.circle(imagen, pt, 1, (0, 255, 255), -1)
        
################################################################################

# Selección de opción
op = int(input("Seleccione una opción:\n1. Batman\n2. Corazón\n3. Estrella\n4. Cicloide\n5. Animación Paramétrica\n6. Lemniscata\n7. Espiral\n8. Hipocicloide\n9. Rosa de 4 pétalos\n10. Cardioide\n"))
if op == 1:
    batman()
    cv2.imwrite('actividades/resultados/batman.png',imagen)
elif op == 2:
    corazon()
    cv2.imwrite('actividades/resultados/corazon.png',imagen)
elif op == 3:
    estrella()
    cv2.imwrite('actividades/resultados/estrella.png',imagen)
elif op == 4:
    cicloide()
    cv2.imwrite('actividades/resultados/cicloide.png',imagen)
elif op == 5:
    animacion_parametrica()
elif op == 6:
    lemniscata()
    cv2.imwrite('actividades/resultados/infinito.png',imagen)
elif op == 7:
    espiral()
    cv2.imwrite('actividades/resultados/espiral.png',imagen)
elif op == 8:
    hipocicloide()
    cv2.imwrite('actividades/resultados/hipocicloide.png',imagen)
elif op == 9:
    rosa()
    cv2.imwrite('actividades/resultados/rosa.png',imagen)
elif op == 10:
    cardioide()
    cv2.imwrite('actividades/resultados/cardioide.png',imagen)
else:
    print("Opción no válida")

# Mostrar la imagen con la gráfica
cv2.imshow('Gráficas Paramétricas', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()