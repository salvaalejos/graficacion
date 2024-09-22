import cv2 as cv

# Cargar la imagen en escala de grises
img = cv.imread('resources/imagen2.jpg', 0)
def mostrar_imagen():
    cv.imshow('Imagen Original', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

op = input("1. Reflejar horizontalmente\n2. Reflejar verticalmente\nOpción: ")

if op == '1':
    # Aplicar la reflexión horizontal usando cv.flip()
    reflected_img = cv.flip(img, 1)
    cv.imshow('Imagen Reflejada Horizontalmente', reflected_img)
    mostrar_imagen()
    
elif op == '2':
    # Aplicar la reflexión vertical usando cv.flip()
    reflected_img = cv.flip(img, 0)
    cv.imshow('Imagen Reflejada Verticalmente', reflected_img)
    mostrar_imagen()
else:
    print("Opción inválida")


