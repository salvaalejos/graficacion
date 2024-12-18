import cv2 as cv

# Leer la imagen en escala de grises
img = cv.imread('resources/imagen2.jpg', 0)
cv.imshow('Original', img)

# Obtener las dimensiones de la imagen
x, y = img.shape

# Aplicar umbral binario
for i in range(x):
    for j in range(y):
        if img[i, j] > 150:
            img[i, j] = 255
        else:
            img[i, j] = 0

cv.imshow('Umbral Binario', img)

# Aplicar filtro de suavizado (Blur)
blur = cv.blur(img, (5, 5))
cv.imshow('Filtro de suavizado (Blur)', blur)

# Aplicar filtro gaussiano (GaussianBlur)
gaussian = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('Filtro Gaussiano (GaussianBlur)', gaussian)

# Aplicar detección de bordes (Canny)
canny = cv.Canny(img, 100, 200)
cv.imshow('Detección de bordes (Canny)', canny)

# Aplicar transformación morfológica (erosión)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
erosion = cv.erode(img, kernel, iterations = 1)
cv.imshow('Transformación Morfológica (Erosión)', erosion)

# Aplicar transformación morfológica (dilatación)
dilation = cv.dilate(img, kernel, iterations = 1)
cv.imshow('Transformación Morfológica (Dilatación)', dilation)

print(img.shape, x, y)
cv.waitKey(0)
cv.destroyAllWindows()