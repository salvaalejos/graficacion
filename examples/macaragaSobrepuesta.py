import cv2
import numpy as np

# Cargar la máscara que deseas agregar (asegúrate de que sea PNG con transparencia)
mascara = cv2.imread('resources/mascara.png', cv2.IMREAD_UNCHANGED)  # Cargar PNG con transparencia

# Cargar el clasificador preentrenado de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

# Capturar video desde la cámara (o puedes usar un archivo de video)
video = cv2.VideoCapture(0)  # Cambia el 0 por la ruta de un archivo de video si quieres usar un archivo

while True:
    # Leer cada frame del video
    ret, frame = video.read()

    if not ret:
        break

    # Convertir el frame a escala de grises
    frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar los rostros en el frame
    rostros = face_cascade.detectMultiScale(frame_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Procesar cada rostro detectado
    for (x, y, w, h) in rostros:
        # Redimensionar la máscara para que coincida con el tamaño del rostro detectado
        mascara_redimensionada = cv2.resize(mascara, (w, h))

        # Separar los canales de la máscara: color y alfa (transparencia)
        mascara_rgb = mascara_redimensionada[:, :, :3]  # Canal de color
        mascara_alpha = mascara_redimensionada[:, :, 3]  # Canal de transparencia

        # Crear una región de interés (ROI) en el frame donde colocaremos la máscara
        roi = frame[y:y+h, x:x+w]

        # Invertir la máscara alfa para obtener la parte del rostro donde se aplicará la máscara
        mascara_alpha_inv = cv2.bitwise_not(mascara_alpha)

        # Enmascarar la región del rostro en la imagen original
        fondo = cv2.bitwise_and(roi, roi, mask=mascara_alpha_inv)

        # Enmascarar la máscara RGB
        mascara_fg = cv2.bitwise_and(mascara_rgb, mascara_rgb, mask=mascara_alpha)

        # Combinar el fondo (parte del rostro sin máscara) y la parte con la máscara
        resultado = cv2.add(fondo, mascara_fg)

        # Reemplazar la región del rostro con la imagen combinada
        frame[y:y+h, x:x+w] = resultado

    # Mostrar el frame con la máscara aplicada
    cv2.imshow('Video con mascara', frame)

    # Presionar 'q' para salir del loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de video y cerrar las ventanas
video.release()
cv2.destroyAllWindows()