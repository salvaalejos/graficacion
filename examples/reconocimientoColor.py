import cv2 as cv
import numpy as np


op = input('Quieres ver video o una imagen?\n1. Imagen\t2. Video\nSeleccione un opción: ')

if int(op) == 1:
    img = cv.imread('resources/imagen2.jpg',1)

    # H: 0 - 180 (Red, Orange, Yellow...)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    uba=(15,255,255)
    ubb=(0,100,100)

    uba2 = (180,255,255)
    ubb2 = (170 , 100, 100)

    mask1 = cv.inRange(hsv, ubb, uba)
    mask2 = cv.inRange(hsv, ubb2, uba2)
    mask = mask1 + mask2

    res = cv.bitwise_and(img, img, mask=mask)

    cv.imshow('Original',img)
    cv.imshow('HSV', hsv)
    cv.imshow('Resultado', res)

    cv.waitKey(0)
    cv.destroyAllWindows()
elif int(op) == 2:

    ############################# Tarea pendiente - aplicar bitwise

    cap = cv.VideoCapture(0)

    while(True):
        ret, img = cap.read()
        if ret:
            cv.imshow('video', img)
            hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
            uba=(100,255,255)
            ubb=(80,40,40)

            uba2 = (20,255,255)
            ubb2 = (0 , 10, 10)

            mask1 = cv.inRange(hsv, ubb, uba)
            mask2 = cv.inRange(hsv, ubb2, uba2)
            mask = mask1 + mask2

            res = cv.bitwise_and(img, img, mask=mask)
            cv.imshow('Filtrado', res)
            k =cv.waitKey(1) & 0xFF
            if k == 27 :
                break
        else:
            break
        
    cap.release()
    cv.destroyAllWindows()
else:
    print('Seleccione opción válida')