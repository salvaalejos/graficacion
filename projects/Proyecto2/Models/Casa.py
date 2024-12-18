import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluSphere, gluCylinder
import sys

class Casa():
    jump_offset = 0.0       # Para el movimiento de salto vertical
    jump_speed = 0.05       # Velocidad del salto
    jump_direction = 1      # Dirección del salto (1 hacia arriba, -1 hacia abajo)
    rotation_angle = 0.0    # Ángulo de rotación del muñeco de nieve

    def init():
        """Configuración inicial de OpenGL"""
        glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
        glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad

        # Configuración de la perspectiva
        glMatrixMode(GL_PROJECTION)
        gluPerspective(60, 1.0, 0.1, 100.0)  # Campo de visión más amplio
        glMatrixMode(GL_MODELVIEW)

        
    def trianguloPascal(n):
        triangulo = []

        for i in range(n):
            fila = [1] # La primera fila siempre es 1

            if triangulo:
                ultima_fila = triangulo[-1] # Selecciona la última fila del triangulo

                fila.extend([ultima_fila[j] + ultima_fila[j + 1] for j in range(len(ultima_fila) - 1)]) # Suma los diferentes valores en la ultima fila
                fila.append(1) # Nueva fila

            triangulo.append(fila)

        return triangulo

    #def trianguloGL(n, x, y):
        

    #####################################################
    def draw_sphere(radius=1, x=0, y=0, z=0):
        glPushMatrix()
        glTranslatef(x, y, z)
        quadric = gluNewQuadric()
        gluSphere(quadric, radius, 32, 32)
        glPopMatrix()

    def draw_triangule(base, x, y, z):
        glPushMatrix()
        glTranslatef(x, y, z)
        quadric = gluNewQuadric()
        
        glPopMatrix()

    def draw_cone(base=0.1, height=0.5, x=0, y=0, z=0):
        glPushMatrix()
        glTranslatef(x, y, z)
        glRotatef(-90, 1, 0, 0)  # Orientar el cono hacia adelante
        quadric = gluNewQuadric()
        gluCylinder(quadric, base, 0, height, 32, 32)
        glPopMatrix()



    def draw_snowman():
        global jump_offset, rotation_angle

        # Limpiar la pantalla y la profundidad
        # glLoadIdentity()

        # Configurar posición de la cámara
        # glTranslatef(x, y, z)  # Posición del muñeco de nieve y altura
        # glRotatef(rotation_angle, 0, 0, 1)  # Rotación en el eje Y

        # Cuerpo
        glColor3f(1, 1, 1)
        draw_sphere(1.0, 3, 0, 0)     # Base
        draw_sphere(0.75, 3, 1.2, 0)  # Cuerpo medio
        draw_sphere(0.5, 3, 2.2, 0)   # Cabeza

        # Ojos
        glColor3f(0, 0, 0)
        draw_sphere(0.05, 2.85, 2.3, 0.4)  # Ojo izquierdo
        draw_sphere(0.05, 3.15, 2.3, 0.4)   # Ojo derecho

        # Nariz (cono)
        glColor3f(1, 0.5, 0)  # Color naranja
        draw_cone(0.05, 0.2, 3, 2.2, 0.5)  # Nariz

        #glfw.swap_buffers(window)


    #####################################################
    def draw_cube():
        """Dibuja el cubo (base de la casa)"""
        glBegin(GL_QUADS)
        glColor3f(0.8, 0.5, 0.2)  # Marrón para todas las caras

        # Frente
        glVertex3f(-1, 0, 1)
        glVertex3f(1, 0, 1)
        glVertex3f(1, 5, 1)
        glVertex3f(-1, 5, 1)

        # Atrás
        glVertex3f(-1, 0, -1)
        glVertex3f(1, 0, -1)
        glVertex3f(1, 5, -1)
        glVertex3f(-1, 5, -1)

        # Izquierda
        glVertex3f(-1, 0, -1)
        glVertex3f(-1, 0, 1)
        glVertex3f(-1, 5, 1)
        glVertex3f(-1, 5, -1)

        # Derecha
        glVertex3f(1, 0, -1)
        glVertex3f(1, 0, 1)
        glVertex3f(1, 5, 1)
        glVertex3f(1, 5, -1)

        # Arriba
        glColor3f(0.9, 0.6, 0.3)  # Color diferente para el techo
        glVertex3f(-1, 5, -1)
        glVertex3f(1, 5, -1)
        glVertex3f(1, 5, 1)
        glVertex3f(-1, 5, 1)

        # Abajo
        glColor3f(0.6, 0.4, 0.2)  # Suelo más oscuro
        glVertex3f(-1, 0, -1)
        glVertex3f(1, 0, -1)
        glVertex3f(1, 0, 1)
        glVertex3f(-1, 0, 1)

        glColor3f(0,0,0) #Color ventanas

        # Ventana Frente
        
        glVertex3f(-.5, 2, 1.1)
        glVertex3f(.5, 2, 1.1)
        glVertex3f(.5, 4, 1.1)
        glVertex3f(-.5, 4, 1.1)

        # Ventana Atrás
        glVertex3f(-.5, 2, -1.1)
        glVertex3f(.5, 2, -1.1)
        glVertex3f(.5, 4, -1.1)
        glVertex3f(-.5, 4, -1.1)

        # Ventana Izquierda
        glVertex3f(-1.1, 2, -.5)
        glVertex3f(-1.1, 2, .5)
        glVertex3f(-1.1, 4, .5)
        glVertex3f(-1.1, 4, -.5)

        # Ventana Derecha
        glVertex3f(1.1, 2, -.5)
        glVertex3f(1.1, 2, .5)
        glVertex3f(1.1, 4, .5)
        glVertex3f(1.1, 4, -.5)




        glEnd()

    def draw_roof():
        """Dibuja el techo (pirámide)"""
        glBegin(GL_TRIANGLES)
        glColor3f(0.9, 0.1, 0.1)  # Rojo brillante

        # Frente
        glVertex3f(-1, 5, 1)
        glVertex3f(1, 5, 1)
        glVertex3f(0, 7, 0)

        # Atrás
        glVertex3f(-1, 5, -1)
        glVertex3f(1, 5, -1)
        glVertex3f(0, 7, 0)

        # Izquierda
        glVertex3f(-1, 5, -1)
        glVertex3f(-1, 5, 1)
        glVertex3f(0, 7, 0)

        # Derecha
        glVertex3f(1, 5, -1)
        glVertex3f(1, 5, 1)
        glVertex3f(0, 7, 0)
        glEnd()

    def draw_ground():
        """Dibuja un plano para representar el suelo o calle"""
        glBegin(GL_QUADS)
        glColor3f(0.3, 0.3, 0.3)  # Gris oscuro para la calle

        # Coordenadas del plano
        glVertex3f(-20, 0, 20)
        glVertex3f(20, 0, 20)
        glVertex3f(20, 0, -20)
        glVertex3f(-20, 0, -20)
        glEnd()

    def draw_house():
        """Dibuja una casa (base + techo)"""
        draw_snowman()
        draw_cube()  # Base de la casa
        draw_roof()  # Techo