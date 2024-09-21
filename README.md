# Graficacion

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

## Trasladar Imagen

Se toma una imagen y se guarda su tamaño para luego crear una imagen vacía del mismo tamaño. Se crean variables con los desplazamientos deseados en x e y, y se recorre el rango en x e y para generar las nuevas posiciones. En la imagen creada, se asignan los valores de la imagen original en las nuevas posiciones.
- Archivo `traslacionRaw.py`