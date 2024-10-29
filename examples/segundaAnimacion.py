import numpy as np
import cv2


# Definir los parámetros iniciales
width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
img = np.ones((height, width, 3), dtype=np.uint8)*255

# Parámetros de la curva de Limacon
a, b = 150, 100  # Reducir los valores de a y b para que la curva se ajuste mejor
k = 0.5# Constante de multiplicación del ángulo
theta_increment = 0.05  # Incremento del ángulo
max_theta = 2 * np.pi  # Un ciclo completo

# Centro de la imagen
center_x, center_y = width // 2, height // 2

theta = 0  # Ángulo inicial
op = input("Que figura quieres?\n1. Corazon \n2. Batman\n3. Estrella\nSeleccione opción: ")
while True:  # Bucle infinito
    # Limpiar la imagen
    img = np.ones((width, height, 3), dtype=np.uint8) * 255
    
    # Dibujar la curva completa desde 0 hasta theta
    for t in np.arange(0, theta, theta_increment):
        # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
        r = a + b * np.sin(k * t)
        if(op == '1'):
            print('Corazon')
        elif(op == '2'):
            x = np.sin(t) * np.cos(t) * np.log(np.abs(t))
            y = np.abs(t) - np.sqrt(np.abs(t))
        elif(op == '3'):
            print('Estrella')

        # x = int(center_x + r * np.sin(t))
        # y = int(center_y + r * np.cos(-t))
        
        # Dibujar un círculo en la posición calculada
        cv2.circle(img, (x, y), 2, (0, 234, 0), 2)  # Color rojo
        # cv2.circle(img, (x-2, y-2), 2, (0, 0, 0), 2)  # Color rojo

    # Mostrar la constante k en la imagen
    #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Mostrar la imagen
    cv2.imshow("Parametric Animation", img)
    
    # Incrementar el ángulo
    theta += theta_increment
    
    # Reiniciar theta si alcanza su valor máximo
    #if theta >= max_theta:
    #    theta = 0  # Reinicia la animación para que se repita

    # Pausar para ver la animación
    if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
        break

# Cerrar la ventana al finalizar
cv2.destroyAllWindows()