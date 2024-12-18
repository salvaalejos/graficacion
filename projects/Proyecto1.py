
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

# Definir un desplazamiento para la máscara
desplazamiento_x = -100  # Ajustar horizontal
desplazamiento_y = 90    # Ajustar vertical

# Umbral para considerar que la boca está abierta
UMBRAL_BOCA_ABIERTA = 0.5  # Proporción de altura respecto al ancho de la boca

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Convertir el frame a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gris_color = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR)  # Gris en BGR para transformaciones

    # Detectar rostros
    rostros = face_cascade.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    boca_abierta = False  # Bandera para cambiar el color del video

    for (x, y, w, h) in rostros:
        # ROI para detectar boca y ojos
        roi_gris = gris[y:y + h, x:x + w]

        # Detectar boca dentro del rostro
        boca = mouth_cascade.detectMultiScale(roi_gris, scaleFactor=1.5, minNeighbors=10, minSize=(30, 30))

        # Detectar ojos dentro del rostro
        ojos = eye_cascade.detectMultiScale(roi_gris, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

        # Superponer la máscara
        mascara_redimensionada = cv2.resize(mascara, (w, h))
        mascara_rgb = mascara_redimensionada[:, :, :3]
        mascara_alpha = mascara_redimensionada[:, :, 3]
        mascara_alpha = cv2.convertScaleAbs(mascara_alpha)

        # Ajustar la posición de la máscara
        x_nuevo = x + desplazamiento_x
        y_nuevo = y + desplazamiento_y
        x_nuevo = max(0, min(x_nuevo, frame.shape[1] - w))
        y_nuevo = max(0, min(y_nuevo, frame.shape[0] - h))

        # Superponer la máscara solo si las dimensiones coinciden
        roi = frame[y_nuevo:y_nuevo + h, x_nuevo:x_nuevo + w]
        if roi.shape[:2] == mascara_alpha.shape[:2]:
            mascara_alpha_inv = cv2.bitwise_not(mascara_alpha)
            fondo = cv2.bitwise_and(roi, roi, mask=mascara_alpha_inv)
            mascara_fg = cv2.bitwise_and(mascara_rgb, mascara_rgb, mask=mascara_alpha)
            resultado = cv2.add(fondo, mascara_fg)
            frame[y_nuevo:y_nuevo + h, x_nuevo:x_nuevo + w] = resultado

        # Verificar si la boca está abierta
        for (mx, my, mw, mh) in boca:
            proporcion_boca = mh / mw
            if proporcion_boca > UMBRAL_BOCA_ABIERTA:
                boca_abierta = True
                break  # Basta con detectar una boca abierta

        # Dibujar círculos amarillos en los ojos
        for (ex, ey, ew, eh) in ojos:
            centro_ojos = (x + ex + ew // 2, y + ey + eh // 2)
            radio = ew // 4
            cv2.circle(frame, centro_ojos, radio, (0, 255, 255), -1)  # Amarillo

    # Cambiar el video a gris y la mascara si la boca está abierta
    if boca_abierta:
        frame = gris_color
        mascara = cv2.imread('resources/mascaraCarnaval.png', cv2.IMREAD_UNCHANGED)

    # Mostrar el frame con todos los efectos aplicados
    cv2.imshow("Video con Efectos", frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de video y cerrar ventanas
video.release()
cv2.destroyAllWindows()