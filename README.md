# Graficacion :pencil2:

# Proyectos :bulb:

:x: Proyectos incompletos

## Proyecto 1 - Flujo óptico
:heavy_exclamation_mark: Incompleto, idea que cuando aparezcan ciertas cosas en pantalla se haga cierta acción. 
- Cuando se abra la boca quitar mascara y cambiar color de video
- Al mostrar mano rotar video
- Al presionar una tecla hacer efecto espejo


## Proyecto 2 - Ciudad 3D
:heavy_exclamation_mark: Incompleto, idea ciudad en 3D reutilizando modelos.

# Actividades :heavy_check_mark:

## :star: Tansformaciones - Rotación, escalamiento y traslación de una imagen :white_check_mark:
Este proyecto es un ejercicio práctico donde se realizan operaciones de rotación, escalado y traslación en una imagen utilizando la librería OpenCV de Python. A través de este código, se transforma una imagen aplicando estas operaciones básicas de procesamiento digital de imágenes.

Archivo `transformaciones_aplicadas.py`

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
## :star: Practica 2 - Dibujar con OpenCV :white_check_mark:

Este proyecto utiliza OpenCV y NumPy para generar imágenes mediante la creación de formas geométricas simples y degradados. A continuación se detalla cómo funciona el código para crear una escena que incluye un cielo, un sol, montañas, agua, nubes, y árboles.

Archivo `practica2_pixelart.py`

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

## :star: Operadores puntuales - Al menos 5 operadores
- Lo primero para estos operadores es que convertimos la imagen a una escala de grises

Archivo `operadores_puntuales.py`

### :small_blue_diamond: Filtrado binario
Con este filtrado lo que se hace es que se recorre toda la matriz de la imagen y detecta si esta por encima de un valor de 150 lo hacemo igual a 255 (blanco) y de lo contrario lo hacemos 0 (negro), por eso se le llama binario ya que ahora la imagen estara compuesta de 0s y 1s.

### :small_blue_diamond: Blur
Este filtro aplica un suavizado promedio a la imagen, útil para reducir el ruido.

- El filtro de suavizado aplica un promediado a los píxeles de la imagen, reduciendo el ruido y suavizando las transiciones.
- El filtro de suavizado (o blur) toma un área de píxeles y reemplaza el valor de cada píxel con el promedio de los valores de sus vecinos. Esto ayuda a reducir el ruido y suavizar las texturas.

```
blur = cv.blur(img, (5, 5))
cv.imshow('Filtro de suavizado (Blur)', blur)
```

Aquí, se utiliza un kernel de tamaño 5x5 para el promediado.

### :small_blue_diamond: Filtro Gaussiano (GaussianBlur)
El filtro gaussiano es similar al filtro de suavizado, pero utiliza una función gaussiana para calcular los valores de los píxeles, proporcionando un suavizado más natural.

- El filtro gaussiano pondera los píxeles vecinos según una distribución gaussiana, lo que significa que los píxeles más cercanos al centro del kernel tienen más influencia en el valor promedio. Esto resulta en una imagen más suavizada y menos afectada por el ruido.

```
gaussian = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('Filtro Gaussiano (GaussianBlur)', gaussian)
```

Se usa un kernel de 5x5 y la desviación estándar de 0, que indica que OpenCV calculará la desviación estándar basada en el tamaño del kernel.

### :small_blue_diamond: Detección de Bordes (Canny)
El filtro Canny es un algoritmo de detección de bordes que identifica los bordes en una imagen analizando los cambios bruscos en la intensidad de los píxeles.

El algoritmo Canny realiza varios pasos:

1. Suaviza la imagen con un filtro gaussiano.
2. Calcula el gradiente de la imagen para encontrar las áreas de cambio brusco.
3. Aplica supresión de no-máximos para eliminar los píxeles que no son máximos locales.
4. Utiliza umbrales para clasificar los píxeles como bordes fuertes, bordes débiles o no bordes.

```
canny = cv.Canny(img, 100, 200)
cv.imshow('Detección de bordes (Canny)', canny)
```

Aquí, se utilizan umbrales de 100 y 200 para la detección de bordes.

### :small_blue_diamond: Transformación Morfológica (Erosión)
La erosión es una operación morfológica que reduce las regiones blancas en una imagen binaria, eliminando pequeñas irregularidades y ruido.

- La erosión utiliza un kernel para "erosionar" las fronteras de las regiones blancas (objetos). El valor del píxel central del kernel se reemplaza con el valor mínimo de los píxeles vecinos dentro del kernel.

```
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
erosion = cv.erode(img, kernel, iterations=1)
cv.imshow('Transformación Morfológica (Erosión)', erosion)
```

Aquí, se utiliza un kernel rectangular de 5x5 y una iteración de erosión.

### :small_blue_diamond: Transformación Morfológica (Dilatación)
La dilatación es la operación inversa a la erosión, aumentando las regiones blancas en una imagen binaria, cerrando pequeños agujeros y conectando componentes.

- La dilatación utiliza un kernel para "dilatar" las fronteras de las regiones blancas. El valor del píxel central del kernel se reemplaza con el valor máximo de los píxeles vecinos dentro del kernel.

```
dilation = cv.dilate(img, kernel, iterations=1)
cv.imshow('Transformación Morfológica (Dilatación)', dilation)
```

Aquí, también se utiliza un kernel rectangular de 5x5 y una iteración de dilatación.

---

## :star: Que es una parametrica?

Archivo `practica3_parametrica.py`

### **¿Qué es una ecuación paramétrica?**

Una **ecuación paramétrica** describe una curva o superficie en términos de un parámetro independiente (o varios parámetros). En lugar de expresar \(y\) directamente como función de \(x\), se definen las coordenadas \(x\) y \(y\) como funciones de un parámetro común \(t\):
\[
x = f(t), \quad y = g(t)
\]

---

### **Usos de las ecuaciones paramétricas**

1. **Gráficos y animaciones:**
   - Se utilizan para modelar trayectorias de objetos en simulaciones y videojuegos.
   - Permiten animar movimientos complejos como órbitas, hélices, o trayectorias de proyectiles.

2. **Geometría computacional:**
   - Generación de formas como elipses, parábolas y curvas más complejas (p. ej., curvas Bézier en diseño gráfico).

3. **Física y cinemática:**
   - Representación de trayectorias de partículas y cuerpos en movimiento, especialmente en sistemas dinámicos.

4. **Modelado 3D:**
   - En gráficos por computadora, para describir superficies paramétricas como esferas, cilindros o toros.

5. **Astronomía y mecánica orbital:**
   - Modelar las órbitas de planetas, satélites y otros cuerpos celestes, como en el ejemplo del sistema solar.

---

### **Aplicación en el código del sistema solar**

En este programa, las ecuaciones paramétricas de una elipse definen las órbitas de los planetas alrededor del Sol. Esto permite calcular sus posiciones dinámicas a medida que el parámetro \(t\) varía, simulando el movimiento orbital con realismo visual.

---

### **Explicación del código**

Este código simula un sistema solar básico utilizando animación y ecuaciones paramétricas para representar las órbitas elípticas de varios planetas alrededor de un "Sol" central. La animación se genera actualizando las posiciones de los planetas cuadro por cuadro.

---

### **Componentes del código**

#### 1. **Librerías**
- `numpy`: Para cálculos matemáticos, como la generación de puntos en una elipse y el manejo de arrays.
- `cv2` (OpenCV): Para crear y mostrar imágenes.

#### 2. **Generación de puntos en una elipse**
La función `generar_punto_elipse(a, b, t)` calcula las coordenadas de un punto en una elipse usando las ecuaciones paramétricas:
\[
x = a \cdot \cos(t) + x_{\text{centro}}
\]
\[
y = b \cdot \sin(t) + y_{\text{centro}}
\]
Donde:
- `a` y `b` son los semiejes mayor y menor.
- `t` es el parámetro que varía entre \(0\) y \(2\pi\), describiendo la posición del planeta en la órbita.

#### 3. **Creación de la animación**
- En cada iteración del bucle `for`, se genera un cuadro de la animación.
- Los planetas son círculos en movimiento que siguen trayectorias elípticas.
- Las trayectorias completas de las órbitas se dibujan para dar contexto visual al movimiento.

#### 4. **Planetas y Sol**
- El Sol se representa como un círculo amarillo fijo en el centro de la imagen.
- Los planetas tienen diferentes colores y tamaños, definidos por sus parámetros de órbita (`a` y `b`).

#### 5. **Estrellas de fondo**
En cada cuadro, se generan puntos aleatorios que simulan un cielo estrellado.

#### 6. **Visualización**
- La función `cv2.imshow` muestra cada cuadro de la animación.
- `cv2.waitKey(10)` controla la velocidad de la animación, con un retardo de 10 milisegundos entre cuadros.

---

### **Resumen**
Este código combina ecuaciones paramétricas y animación con OpenCV para simular un sistema solar. Los planetas se mueven en órbitas elípticas, mientras un Sol central y estrellas aleatorias completan el escenario visual.


--- 

## :star: Ecuaciones Parametricas - 10 ejemplos

Archivo `ejemplos_parametricas.py`

## Descripción General

Este código genera imágenes de varias figuras geométricas y curvas paramétricas utilizando Python, las cuales se dibujan en una imagen en blanco mediante la librería OpenCV (`cv2`). La imagen resultante puede mostrar figuras como un logo de Batman, corazones, estrellas, espirales, entre otras. Cada figura se genera a partir de una función matemática paramétrica.


---

## Requerimientos

- `numpy`: Para la manipulación de arrays y cálculo de funciones matemáticas.
- `cv2` (OpenCV): Para la creación y manipulación de imágenes.

Instalar dependencias:

```bash
pip install numpy opencv-python
```

---

## Variables Globales

- `img_width`, `img_height`: Definen el tamaño de la imagen en píxeles (800x800 en este caso).
- `imagen`: Es una matriz de ceros (imagen en blanco), que tiene dimensiones `(img_height, img_width, 3)` para representar una imagen a color (RGB).

---

## Funciones Definidas

### 1. `batman()`
Dibuja una figura basada en una aproximación matemática del logo de Batman.

- **Matemáticas involucradas**: Funciones cuadráticas y trigonométricas que definen una forma compuesta de curvas.
- **Gráfica**: Genera puntos en coordenadas `(x, y)` para representar la forma de Batman en la imagen.

![Batman](actividades\resultados\batman.png)

### 2. `corazon()`
Dibuja un corazón utilizando una curva paramétrica.

- **Ecuación paramétrica**:  
  \[
  x = 16 \sin^3(t), \quad y = 13 \cos(t) - 5 \cos(2t) - 2 \cos(3t) - \cos(4t)
  \]
- **Visualización**: El corazón se dibuja en color morado sobre un fondo blanco.
  
![Corazón](actividades\resultados\corazon.png)

### 3. `estrella()`
Genera una estrella usando coordenadas polares.

- **Ecuación paramétrica**:
  \[
  x = \cos(t) \left( 1 - 0.5 \cos(5t) \right), \quad y = \sin(t) \left( 1 - 0.5 \cos(5t) \right)
  \]
- **Escala**: La estrella se escala por un factor de 200.

![Estrella](actividades\resultados\estrella.png)

### 4. `cicloide()`
Dibuja una cicloide (la curva generada por un punto en una rueda que rueda sin deslizarse).

- **Ecuación paramétrica**:
  \[
  x = R (\phi + \sin(\phi)), \quad y = R (1 - \cos(\phi))
  \]
- **Escala**: El valor de `R` es 20 y la curva se ajusta a una escala acorde a la imagen.

![Cicloide](actividades\resultados\cicloide.png)

### 5. `animacion_parametrica()`
Genera una animación de una curva paramétrica que varía con el tiempo.

- **Curva**: Depende de dos parámetros `a` y `b` que cambian con el tiempo.
- **Animación**: La imagen se actualiza frame a frame para mostrar el cambio en la curva.

### 6. `lemniscata()`
Genera una lemniscata de Bernoulli, una figura en forma de "infinito".

- **Ecuación paramétrica**:
  \[
  x = \frac{\cos(t)}{1 + \sin^2(t)}, \quad y = \frac{\cos(t) \sin(t)}{1 + \sin^2(t)}
  \]
- **Escala**: La curva se escala por un factor de 300.

![Infinito](actividades\resultados\infinito.png)

### 7. `espiral()`
Dibuja una espiral de Arquímedes.

- **Ecuación paramétrica**:
  \[
  x = t \cos(t), \quad y = t \sin(t)
  \]
- **Escala**: La espiral se ajusta con un factor de escala de 10.

![Espiral](actividades\resultados\espiral.png)

### 8. `hipocicloide()`
Dibuja una hipocicloide, una figura generada por un punto de una rueda más pequeña que rueda dentro de una rueda más grande.

- **Ecuación paramétrica**:
  \[
  x = (a - b) \cos(t) + b \cos\left(\frac{a - b}{b} t\right), \quad y = (a - b) \sin(t) - b \sin\left(\frac{a - b}{b} t\right)
  \]
- **Parámetros**: `a = 5` y `b = 3`.

![Hipocicloide](actividades\resultados\hipocicloide.png)

### 9. `rosa()`
Genera una curva en forma de rosa con 4 pétalos.

- **Ecuación paramétrica**:
  \[
  x = \cos(2t) \cos(t), \quad y = \cos(2t) \sin(t)
  \]
- **Escala**: Los valores de la curva se amplifican por un factor de 200.

![Rosa](actividades\resultados\rosa.png)

### 10. `cardioide()`
Dibuja una cardioide, una figura en forma de corazón generada por una parábola.

- **Ecuación paramétrica**:
  \[
  x = 2 \cos(t) - \cos(2t), \quad y = 2 \sin(t) - \sin(2t)
  \]
- **Escala**: Se utiliza un factor de escala de 100.

![Cardioide](actividades\resultados\cardioide.png)



---

## Interactividad

El código solicita al usuario seleccionar una figura (del 1 al 10) para generar la correspondiente en la imagen.

- **Entrada**: El usuario ingresa un número del 1 al 10 para elegir la figura a dibujar.
- **Salida**: La figura seleccionada se genera en la imagen y se muestra utilizando `cv2.imshow()`. Luego de generar la imagen, la ventana de la imagen se muestra hasta que el usuario cierre la ventana.

---

## Uso

Para usar el código:

1. Ejecuta el script.
2. Ingresa un número entre 1 y 10 según la figura que deseas dibujar.
3. La figura seleccionada será mostrada en la ventana generada por OpenCV.

---

## Notas

- El código utiliza OpenCV para mostrar imágenes y realizar dibujos, lo que requiere tener una interfaz gráfica disponible en el entorno de ejecución.
- Se pueden modificar los parámetros de las funciones para cambiar las formas y tamaños de las figuras generadas.

---

## :star: Casas con muñeco - OpenGL
Este código es un ejemplo de una aplicación de OpenGL en Python que utiliza GLFW y la biblioteca OpenGL para crear una simulación 3D de un muñeco de nieve, casas y un escenario.

### Importaciones
```python
import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluSphere, gluCylinder
import sys
```
- `glfw`: Biblioteca para crear y manejar ventanas y eventos en OpenGL.
- `OpenGL.GL` y `OpenGL.GLU`: Bibliotecas para interactuar con OpenGL y manejar gráficos 3D, como la creación de esferas, conos y matrices de transformación.

### Función de inicialización
```python
def init():
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad

    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1.0, 0.1, 100.0)  # Campo de visión más amplio
    glMatrixMode(GL_MODELVIEW)
```
Configura el entorno de OpenGL, el color de fondo y la perspectiva de la cámara para la escena 3D.

### Función de Triángulo de Pascal
```python
def trianguloPascal(n):
    triangulo = []
    for i in range(n):
        fila = [1]
        if triangulo:
            ultima_fila = triangulo[-1]
            fila.extend([ultima_fila[j] + ultima_fila[j + 1] for j in range(len(ultima_fila) - 1)])
            fila.append(1)
        triangulo.append(fila)
    return triangulo
```
Genera un Triángulo de Pascal hasta `n` filas. Aunque no se usa en el resto del código, podría servir para otros cálculos o visualizaciones.

### Funciones para dibujar objetos
Estas funciones utilizan OpenGL para crear varias formas 3D.

#### Dibujo de esfera
```python
def draw_sphere(radius=1, x=0, y=0, z=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    quadric = gluNewQuadric()
    gluSphere(quadric, radius, 32, 32)
    glPopMatrix()
```
Dibuja una esfera en las coordenadas `(x, y, z)`.

#### Dibujo de un cono
```python
def draw_cone(base=0.1, height=0.5, x=0, y=0, z=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(-90, 1, 0, 0)  # Orientar el cono hacia adelante
    quadric = gluNewQuadric()
    gluCylinder(quadric, base, 0, height, 32, 32)
    glPopMatrix()
```
Dibuja un cono en las coordenadas `(x, y, z)`.

#### Dibujo del muñeco de nieve
```python
def draw_snowman():
    global jump_offset, rotation_angle
    glColor3f(1, 1, 1)
    draw_sphere(1.0, 3, 0, 0)     # Base
    draw_sphere(0.75, 3, 1.2, 0)  # Cuerpo medio
    draw_sphere(0.5, 3, 2.2, 0)   # Cabeza

    glColor3f(0, 0, 0)
    draw_sphere(0.05, 2.85, 2.3, 0.4)  # Ojo izquierdo
    draw_sphere(0.05, 3.15, 2.3, 0.4)   # Ojo derecho

    glColor3f(1, 0.5, 0)  # Nariz naranja
    draw_cone(0.05, 0.2, 3, 2.2, 0.5)  # Nariz
```
Dibuja un muñeco de nieve con una base, cuerpo, cabeza, ojos y nariz.

#### Dibujo de una casa
```python
def draw_cube():
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)  # Marrón para todas las caras
    # Cuadrado de la casa, con sus ventanas y puertas
    glEnd()
```
Dibuja el cubo que representa la base de la casa, y añade detalles como las ventanas.

#### Dibujo del techo
```python
def draw_roof():
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.1, 0.1)  # Rojo brillante
    # Triángulos que forman el techo
    glEnd()
```
Dibuja el techo de la casa como una pirámide.

### Función principal para dibujar la escena
```python
def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(10, 8, 15, 0, 0, 0, 0, 1, 0)  # Posición y orientación de la cámara
    draw_ground()  # Dibuja el suelo
    positions = [(-5, 0, -5), (5, 0, -5), (-5, 0, 5), (5, 0, 5)]  # Posiciones de las casas
    for pos in positions:
        glPushMatrix()
        glTranslatef(*pos)  # Mueve la casa a su posición
        draw_house()
        glPopMatrix()
    glfw.swap_buffers(window)
```
Dibuja el suelo y cuatro casas en la escena en diferentes posiciones.

### Bucle principal
```python
def main():
    global window
    if not glfw.init():
        sys.exit()
    window = glfw.create_window(800, 600, "Escena con 4 casas", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, 800, 600)
    init()

    while not glfw.window_should_close(window):
        draw_scene()
        glfw.poll_events()

    glfw.terminate()
```
Inicializa GLFW, crea una ventana y comienza el bucle de renderizado, donde se dibuja la escena continuamente.

### Resumen
Este programa crea una ventana con GLFW y dibuja una escena 3D que contiene un muñeco de nieve y casas. Se utilizan esferas para las partes del muñeco, cubos para la casa y un cono para la nariz. La cámara está configurada para que se vea la escena desde una posición determinada.


---
---
---

# Practicas

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
