# Graficacion :pencil2:

## Primer Commit

Se instalaron las librerías y entornos necesarios y se realizó la siguiente práctica:

#### Leer Imagen
- Práctica de leer imagen
- Archivo: `verImg.py`

## Operador Puntual

En esta práctica se aplicó un filtro blanco y negro recorriendo la matriz de la imagen.
- Primero se lee la imagen en escala de grises.
- Si los valores de los píxeles son mayores a 150, se convierten a 255 (blanco).
- Si los valores son menores o iguales a 150, se convierten a 0 (negro).
- Archivo: `operadorPuntual.py`

## Leer Video

Se toma el video grabado con nuestro dispositivo y se maneja la imagen recibida.
- Archivo: `verVideo.py`
- 
## Transformaciones geometricas en modo RAW

### Trasladar Imagen ( *RAW* )

Se toma una imagen y se guarda su tamaño para luego crear una imagen vacía del mismo tamaño. Se crean variables con los desplazamientos deseados en x e y, y se recorre el rango en x e y para generar las nuevas posiciones. En la imagen creada, se asignan los valores de la imagen original en las nuevas posiciones.
- Archivo `traslacionRaw.py`

### Rotación Imagen ( *RAW* )
La rotación se realiza alrededor del centro de la imagen, utilizando las fórmulas matemáticas correspondientes.
- :exclamation: Error corregido en `rotated_img = np.zeros((x*2, y*2), dtype=np.uint8)` ya que multiplicar `x*2, y*2` aumentaba bastante el tamaño de la ventana con espacio vacío.
- Archivo `rotacionRaw.py`

### Escalado Imagen ( *RAW* )
El escalado cambia el tamaño de la imagen multiplicando las coordenadas por un factor de escala.
- :exclamation: Error corregido, ya que al escalar la imagen solo hacía un tipo de "zoom". 
- Archivo `escaladoRaw.py`


### Cizallamiento / Shearing ( *RAW* )
En el cizallamiento, los píxeles se desplazan en una dirección proporcional a otra, lo que inclina la imagen.
- Archivo `shearingRaw.py`

### Reflexion vertical y horizontal ( *RAW* )
El código realiza una reflexión (espejo) de una imagen en escala de grises, ya sea horizontal o verticalmente, según la opción que el usuario elija.
- :sparkles: Funcion añadida para que el usuario pueda escoger que reflexion ver.
- Archivo `reflexionRaw.py`

## Transformaciones geometricas con OpenCV

### Trasladar Imagen

En OpenCV, la traslación se realiza usando matrices de transformación afín y la función `cv.warpAffine()`.
- Archivo `traslacion.py`

### Rotación Imagen
La rotación alrededor del centro de la imagen se puede realizar con la función `cv.getRotationMatrix2D()`.
- Archivo `rotacion.py`

### Escalado Imagen
EEl escalado se puede realizar usando la función `cv.resize()`.
- Archivo `escalado.py`

### Cizallamiento / Shearing
El cizallamiento se puede realizar creando una matriz de transformación afín personalizada.
- Archivo `shearing.py`

### Reflexion vertical y horizontal
En OpenCV, la reflexión de una imagen se realiza con la función `cv.flip()`.
- :sparkles: Funcion añadida para que el usuario pueda escoger que reflexion ver.
- Archivo `reflexion.py`.
  
## Parametricas
En el archivo `primerAnimacion.py` podemos observar un código en el que se crea una elipse en base a su ecuación parametrica, en ella se crea un punto en ella el
cual va avanzando en esa misma elipse.


# Proyectos :bulb:

## Practica 1 - Rotación, escalamiento y traslación de una imagen :white_check_mark:
Este proyecto es un ejercicio práctico donde se realizan operaciones de rotación, escalado y traslación en una imagen utilizando la librería OpenCV de Python. A través de este código, se transforma una imagen aplicando estas operaciones básicas de procesamiento digital de imágenes.

### Descripción del código:
1. #### Carga de imagen:
   La imagen utilizada en esta práctica `(imagen2.jpg)` se carga en escala de grises usando la función `cv.imread()`.
   
   ```
   img = cv.imread('resources/imagen2.jpg', 0)
   ```

2. #### Rotación de imagen:
   Se rota la imagen 60 grados alrededor de su centro. Para lograr esto, se utiliza `cv.getRotationMatrix2D()` para crear la matriz de rotación, y luego `cv.warpAffine()` para aplicar la rotación.

   ```
    angle = 60
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated_img = cv.warpAffine(img, M, (y, x))
   ```

3. #### Escalado de imagen:
   Se reduce el tamaño de la imagen utilizando factores de escala en los ejes X e Y de 0.5, lo que equivale a reducir la imagen a la mitad de su tamaño original.

   ```
    scale_x, scale_y = 0.5, 0.5
    scaled_img = cv.resize(img, None, fx=scale_x, fy=scale_y)
   ```
4. #### Traslacion de imagen:
   Se traslada la imagen 100 píxeles en los ejes X e Y. Para ello, se crea una matriz de traslación y se aplica a la imagen utilizando `cv.warpAffine()`.

   ```
    dx, dy = 100, 100
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    translated_img = cv.warpAffine(img, M, (y, x))
   ```
5. #### Visualización:
   Al ejecutar el código se puede visualizar la **original**, *rotada*, *escalada*, *trasladada* y la imagen **final** con todas estas transformaciones aplicadas.

   ```
    cv.imshow('Imagen Original', img)
    cv.imshow('Imagen Rotada', rotated_img)
    cv.imshow('Imagen Escalada', scaled_img)
    cv.imshow('Imagen Trasladada', translated_img)
    cv.imshow('Imagen Final', finalImg)
    cv.waitKey(0)
    cv.destroyAllWindows()
   ```
---
## Practica 2 - Dibujar con OpenCV :white_check_mark:

Este proyecto utiliza OpenCV y NumPy para generar imágenes mediante la creación de formas geométricas simples y degradados. A continuación se detalla cómo funciona el código para crear una escena que incluye un cielo, un sol, montañas, agua, nubes, y árboles.

### Funcionalidades del código:
1. **Creación de la imagen base:** Se crea una imagen en blanco de tamaño 3751x5938 píxeles, aunque se escala un 10% del tamaño original. (Esto ya que la imagen que se tomó de guía media este tamaño)
   ```
   img = np.ones((3751, 5938, 3), np.uint8)*255
   img = cv.resize(img, None, fx=0.1, fy=0.1)
   ```
2. **Degradado en el cielo:** Con un ciclo se crea un degradado para el color de fondo en el cielo, asignado pixeles x pixeles el color correspondiente hasta llegar a la linea de "horizonte".
   
   ```
   for yp in range(posicion_linea_horizonte_y):
      # Calcular el color en cada iteración
      img[yp, :] = [r, g, b]
   ```
3. **Dibujo del sol:** Se dibuja un círculo que representa el sol en el centro de la imagen.

   ```
   cv.circle(img, (int(x/2), int(y/2)), 150, (95, 215, 255), -1)
   ```
4. **Degradado de agua:** Similar al degradado del cielo, pero en la parte inferior, con colores más púrpura.
   
   ```
   for yp in range(y - posicion_linea_horizonte_y):
      # Calcular el degradado para el agua
      img[yp + posicion_linea_horizonte_y, :] = [r, g, b]
   ```
5. **Dibujo de nubes:** Se agregan nubes al azar en el cielo usando círculos de color blanco con la siguiente función.
   ```
   def dibujarNube(x, y):
      randomX = np.random.randint(20, x-20)
      randomY = np.random.randint(20, posicion_linea_horizonte_y-20)
      randomSize = np.random.randint(10, 40)
      cv.circle(img, (randomX, randomY), randomSize, (239, 251, 255), -1)
   
   for i in range(10):
      dibujarNube(x, y)
   ```

6. **Montañas y nieve:** Se dibujan montañas usando polígonos y se rellenan con colores que simulan la tierra y nieve en la cima.
   ```
   montainPrincipal = np.array([
                [x/4, posicion_linea_horizonte_y],
                [x/2, posicion_linea_horizonte_y/2],
                [3*x/4, posicion_linea_horizonte_y]
                ], np.int32)

   # Cambiar la forma del arreglo
   montainPrincipal = montainPrincipal.reshape((-1, 1, 2))

   # Dibujar el polígono
   cv.fillPoly(img, [montainPrincipal], principal_montain)

   snowPrincipal = np.array([
                  [x/2, posicion_linea_horizonte_y/2],
                  [x/2-25, posicion_linea_horizonte_y/2+20],
                  [x/2+25, posicion_linea_horizonte_y/2+20],
                  [x/2, posicion_linea_horizonte_y/2]
                  ], np.int32)

   # Cambiar la forma del arreglo
   snowPrincipal = snowPrincipal.reshape((-1, 1, 2))

   # Dibujar el polígono

   cv.fillPoly(img, [snowPrincipal], (255, 255, 255))

   ```
7. **Arboles:** Árboles: Se generan árboles al azar con triángulos en donde se divide el agua y las montañas (*la linea de horizonte*).
   ```
   trees = []
   for i in range(0, x, 30):
      # Dibujar árboles
      trees.append([i, posicion_linea_horizonte_y])
   cv.fillPoly(img, [trees], purpura_final)
   ```

### Resultados:
Resultados
Este script genera una imagen con:

- Un cielo degradado.
- Un sol amarillo en el centro.
- Montañas con nieve.
- Un degradado de agua debajo del horizonte.
- Nubes generadas de forma aleatoria.
- Árboles en el paisaje.
---