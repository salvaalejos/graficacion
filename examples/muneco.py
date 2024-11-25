import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluNewQuadric, gluSphere, gluPerspective, gluCylinder
import sys
import math

# Variables globales
window = None
jump_offset = 0.0       # Para el movimiento de salto vertical
jump_speed = 0.05       # Velocidad del salto
jump_direction = 1      # Dirección del salto (1 hacia arriba, -1 hacia abajo)
rotation_angle = 0.0    # Ángulo de rotación del muñeco de nieve

def init():
    glClearColor(0.5, 0.7, 1.0, 1.0)  # Fondo de cielo
    glEnable(GL_DEPTH_TEST)

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1.0, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def draw_sphere(radius=1, x=0, y=0, z=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    quadric = gluNewQuadric()
    gluSphere(quadric, radius, 32, 32)
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
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configurar posición de la cámara
    glTranslatef(0.0 + jump_offset, -1.5 , -8)  # Posición del muñeco de nieve y altura
    glRotatef(rotation_angle, 0, 0, 1)  # Rotación en el eje Y

    # Cuerpo
    glColor3f(1, 1, 1)
    draw_sphere(1.0, 0, 0, 0)     # Base
    draw_sphere(0.75, 0, 1.2, 0)  # Cuerpo medio
    draw_sphere(0.5, 0, 2.2, 0)   # Cabeza

    # Ojos
    glColor3f(0, 0, 0)
    draw_sphere(0.05, -0.15, 2.3, 0.4)  # Ojo izquierdo
    draw_sphere(0.05, 0.15, 2.3, 0.4)   # Ojo derecho

    # Nariz (cono)
    glColor3f(1, 0.5, 0)  # Color naranja
    draw_cone(0.05, 0.2, 0, 2.2, 0.5)  # Nariz

    glfw.swap_buffers(window)

def update_motion():
    global jump_offset, jump_direction, rotation_angle

    # Actualizar el ángulo de rotación
    rotation_angle += 1  # Incrementa para que el muñeco gire
    if rotation_angle >= 360:
        rotation_angle = 0  # Reiniciar el ángulo después de una vuelta completa

    # Actualizar el movimiento de salto
    jump_offset += jump_speed * jump_direction
    if jump_offset > 1.0:        # Limite superior del salto
        jump_direction = -1      # Cambiar dirección hacia abajo
    elif jump_offset < 0.0:      # Limite inferior del salto
        jump_direction = 1       # Cambiar dirección hacia arriba

def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()
    
    # Crear ventana de GLFW
    width, height = 500, 500
    window = glfw.create_window(width, height, "Muñeco de Nieve en Movimiento", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    init()

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_snowman()
        update_motion()  # Actualizar el movimiento en cada cuadro
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()