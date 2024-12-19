import cv2
import numpy as np

# Cargar la máscara (asegúrate de que sea PNG con transparencia)
mascara = cv2.imread('resources/cubre3.png', cv2.IMREAD_UNCHANGED)  # PNG con canal alfa

# Verificar si la imagen tiene un canal alfa
if mascara.shape[2] != 4:
    print("Error: La imagen no tiene canal alfa.")
    exit()

# Cargar clasificadores
face_cascade = cv2.CascadeClassifier('resources/haarcascade_frontalface_alt2.xml')  # Rostros
mouth_cascade = cv2.CascadeClassifier('resources/haarcascade_mcs_mouth.xml')       # Boca
eye_cascade = cv2.CascadeClassifier('resources/haarcascade_eye.xml')               # Ojos

# Capturar video desde la cámara
video = cv2.VideoCapture(0)

# Definir un desplazamiento inicial para la máscara
desplazamiento_x = -100  # Ajustar horizontal
desplazamiento_y = 90    # Ajustar vertical

# Variables de transformación
voltear_espejo = False
rotar_90 = False
factor_escala = 1.0  # Factor inicial de escala para la máscara

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Convertir el frame a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gris_color = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR)  # Gris en BGR para transformaciones

    # Detectar rostros
    rostros = face_cascade.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    for (x, y, w, h) in rostros:
        # Redimensionar la máscara según el factor de escala
        nuevo_ancho = int(w * factor_escala)
        nuevo_alto = int(h * factor_escala)
        mascara_redimensionada = cv2.resize(mascara, (nuevo_ancho, nuevo_alto))
        mascara_rgb = mascara_redimensionada[:, :, :3]
        mascara_alpha = mascara_redimensionada[:, :, 3]
        mascara_alpha = cv2.convertScaleAbs(mascara_alpha)

        # Ajustar la posición de la máscara con desplazamiento dinámico
        x_nuevo = x + desplazamiento_x
        y_nuevo = y + desplazamiento_y
        x_nuevo = max(0, min(x_nuevo, frame.shape[1] - nuevo_ancho))
        y_nuevo = max(0, min(y_nuevo, frame.shape[0] - nuevo_alto))

        # Superponer la máscara solo si las dimensiones coinciden
        if y_nuevo + nuevo_alto <= frame.shape[0] and x_nuevo + nuevo_ancho <= frame.shape[1]:
            roi = frame[y_nuevo:y_nuevo + nuevo_alto, x_nuevo:x_nuevo + nuevo_ancho]
            mascara_alpha_inv = cv2.bitwise_not(mascara_alpha)
            fondo = cv2.bitwise_and(roi, roi, mask=mascara_alpha_inv)
            mascara_fg = cv2.bitwise_and(mascara_rgb, mascara_rgb, mask=mascara_alpha)
            resultado = cv2.add(fondo, mascara_fg)
            frame[y_nuevo:y_nuevo + nuevo_alto, x_nuevo:x_nuevo + nuevo_ancho] = resultado
        else:
            print("La máscara no se puede superponer debido a las dimensiones.")

    # Aplicar transformaciones generales al frame
    if voltear_espejo:
        frame = cv2.flip(frame, 1)  # Voltear horizontalmente (espejo)

    if rotar_90:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)  # Rotar 90° en sentido horario

    # Mostrar el frame con todos los efectos aplicados
    cv2.imshow("Video con Efectos", frame)

    # Teclas de control
    tecla = cv2.waitKey(1) & 0xFF
    if tecla == ord('q'):  # Salir con 'q'
        break
    elif tecla == ord('f'):  # Activar o desactivar el efecto espejo
        voltear_espejo = not voltear_espejo
    elif tecla == ord('r'):  # Activar o desactivar la rotación 90°
        rotar_90 = not rotar_90
    elif tecla == ord('a'):  # Mover hacia la izquierda
        desplazamiento_x -= 10
        print(f"Desplazamiento X: {desplazamiento_x}")
    elif tecla == ord('d'):  # Mover hacia la derecha
        desplazamiento_x += 10
        print(f"Desplazamiento X: {desplazamiento_x}")
    elif tecla == ord('z'):  # Incrementar el zoom
        factor_escala += 0.1
        print(f"Factor de escala: {factor_escala}")
    elif tecla == ord('x'):  # Disminuir el zoom
        factor_escala = max(0.1, factor_escala - 0.1)
        print(f"Factor de escala: {factor_escala}")

# Liberar la captura de video y cerrar ventanas
video.release()
cv2.destroyAllWindows()