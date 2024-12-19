import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt, gluNewQuadric, gluSphere, gluCylinder
import sys

# Variables globales para controlar la posición de la cámara
cam_x, cam_y, cam_z = 10, 8, 15
cam_speed = 0.5

def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1.0, 0.1, 100.0)  # Campo de visión más amplio
    glMatrixMode(GL_MODELVIEW)

def key_callback(window, key, scancode, action, mods):
    """Procesa las entradas de teclado"""
    global cam_x, cam_y, cam_z, cam_speed

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            cam_y += cam_speed  # Mover la cámara hacia arriba
        elif key == glfw.KEY_DOWN:
            cam_y -= cam_speed  # Mover la cámara hacia abajo
        elif key == glfw.KEY_LEFT:
            cam_x -= cam_speed  # Mover la cámara hacia la izquierda
        elif key == glfw.KEY_RIGHT:
            cam_x += cam_speed  # Mover la cámara hacia la derecha
        elif key == glfw.KEY_W:
            cam_z -= cam_speed  # Acercar la cámara
        elif key == glfw.KEY_S:
            cam_z += cam_speed  # Alejar la cámara

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

def draw_cylinder(base=0.1, height=1.0, x=0, y=0, z=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(-90, 1, 0, 0)  # Orientar el cilindro hacia arriba
    quadric = gluNewQuadric()
    gluCylinder(quadric, base, base, height, 32, 32)
    glPopMatrix()

def draw_cube():
    """Dibuja un cubo"""
    glBegin(GL_QUADS)

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

    glColor3f(0, 0, 0)  # Color ventanas

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

def draw_snowman():
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

def draw_road():
    """Dibuja una carretera"""
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)  # Color gris oscuro para la carretera

    # Dibujar la carretera principal
    glVertex3f(-2, 0.01, 20)
    glVertex3f(2, 0.01, 20)
    glVertex3f(2, 0.01, -20)
    glVertex3f(-2, 0.01, -20)

    glEnd()

    # Dibujar las líneas blancas de la carretera
    glColor3f(1.0, 1.0, 1.0)  # Color blanco para las líneas
    for i in range(-20, 20, 4):
        glBegin(GL_QUADS)
        glVertex3f(-0.1, 0.02, i + 1)
        glVertex3f(0.1, 0.02, i + 1)
        glVertex3f(0.1, 0.02, i - 1)
        glVertex3f(-0.1, 0.02, i - 1)
        glEnd()

def draw_ground():
    """Dibuja el suelo alrededor de la carretera"""
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.7, 0.3)  # Verde para el suelo

    # Coordenadas del suelo
    glVertex3f(-20, 0, 20)
    glVertex3f(20, 0, 20)
    glVertex3f(20, 0, -20)
    glVertex3f(-20, 0, -20)

    glEnd()

def draw_tree(x, y, z):
    """Dibuja un árbol en la posición (x, y, z)"""
    # Dibujar el tronco
    glColor3f(0.55, 0.27, 0.07)  # Color marrón para el tronco
    draw_cylinder(0.1, 1.0, x, y, z)

    # Dibujar las hojas
    glColor3f(0.0, 0.8, 0.0)  # Color verde para las hojas
    draw_cone(0.5, 1.0, x, y + 1.0, z)

def draw_house():
    """Dibuja una casa (base + techo)"""
    draw_cube()  # Base de la casa
    draw_roof()  # Techo
    draw_snowman()

def draw_church():
    """Dibuja una iglesia"""
    glColor3f(0.2, 0.2, 0.4)  # Marrón para la iglesia

    # Base de la iglesia
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(1.5, 1.5, 1.5)
    draw_cube()
    glPopMatrix()

    # Torre de la iglesia
    glColor3f(0.1, 0.1, 0.4)  # Marrón más oscuro para la torre
    glPushMatrix()
    glTranslatef(0, 3, 0)
    glScalef(0.5, 2, 0.5)
    draw_cube()
    glPopMatrix()

    # Cruz en la cima de la torre
    glColor3f(1, 1, 1)  # Blanco para la cruz
    glPushMatrix()
    glTranslatef(0, 7.5, 0)
    glScalef(0.1, 1, 0.1)
    draw_cube()  # Poste vertical de la cruz
    glPopMatrix()

    glColor3f(1, 1, 1)  # Blanco para la cruz
    glPushMatrix()
    glTranslatef(0, 8, 0)
    glScalef(0.5, 0.1, 0.1)
    draw_cube()  # Poste horizontal de la cruz
    glPopMatrix()

def draw_school():
    """Dibuja una escuela"""
    glColor3f(0.6, 0.6, 0.6)  # Gris para la escuela

    # Base de la escuela
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(3, 1.5, 2)
    draw_cube()
    glPopMatrix()

    # Puerta de la escuela
    glColor3f(0.2, 0.2, 0.2)  # Negro para la puerta
    glPushMatrix()
    glTranslatef(0, 0.5, 1.1)
    glScalef(0.5, 1, 0.1)
    draw_cube()
    glPopMatrix()

    # Ventanas de la escuela
    glColor3f(0.8, 0.8, 0.8)  # Blanco para las ventanas
    for i in range(-2, 3, 2):
        for j in range(1, 4, 2):
            glPushMatrix()
            glTranslatef(i, j, 1.1)
            glScalef(0.5, 1, 0.1)
            draw_cube()
            glPopMatrix()

def draw_fountain():
    """Dibuja una fuente"""
    # Base de la fuente
    glColor3f(0.5, 0.5, 0.5)  # Gris para la base
    draw_cylinder(1.0, 0.5, 0, 0, 0)

    # Agua de la fuente
    glColor3f(0.0, 0.0, 1.0)  # Azul para el agua
    draw_sphere(0.8, 0, 0.5, 0)
    
def draw_bench():
    # Dibujar el asiento de la banca (rectángulo largo)
    glPushMatrix()
    
    glColor3f(0.6, 0.3, 0.0)  # Color marrón para el asiento
    glBegin(GL_QUADS)
    
    # Parte superior del asiento
    glVertex3f(-1.5, 0, -0.5)  # Esquina inferior izquierda
    glVertex3f(1.5, 0, -0.5)   # Esquina inferior derecha
    glVertex3f(1.5, 0, 0.5)    # Esquina superior derecha
    glVertex3f(-1.5, 0, 0.5)   # Esquina superior izquierda
    
    glEnd()
    
    # Dibujar los soportes (dos cubos pequeños a cada lado del asiento)
    glColor3f(0.4, 0.2, 0.0)  # Color más oscuro para los soportes
    # Soporte izquierdo
    glPushMatrix()
    glTranslatef(-1.4, 0, 0)  # Desplazamos a la izquierda
    glBegin(GL_QUADS)
    
    glVertex3f(-0.1, 0, -0.1)   # Esquina inferior izquierda
    glVertex3f(0.1, 0, -0.1)    # Esquina inferior derecha
    glVertex3f(0.1, -1, -0.1)   # Esquina superior derecha
    glVertex3f(-0.1, -1, -0.1)  # Esquina superior izquierda
    
    glVertex3f(-0.1, 0, 0.1)    # Esquina inferior izquierda
    glVertex3f(0.1, 0, 0.1)     # Esquina inferior derecha
    glVertex3f(0.1, -1, 0.1)    # Esquina superior derecha
    glVertex3f(-0.1, -1, 0.1)   # Esquina superior izquierda
    
    glVertex3f(-0.1, 0, -0.1)   # Esquina inferior izquierda
    glVertex3f(-0.1, 0, 0.1)    # Esquina inferior derecha
    glVertex3f(-0.1, -1, 0.1)   # Esquina superior derecha
    glVertex3f(-0.1, -1, -0.1)  # Esquina superior izquierda
    
    glVertex3f(0.1, 0, -0.1)    # Esquina inferior izquierda
    glVertex3f(0.1, 0, 0.1)     # Esquina inferior derecha
    glVertex3f(0.1, -1, 0.1)    # Esquina superior derecha
    glVertex3f(0.1, -1, -0.1)   # Esquina superior izquierda
    
    glEnd()
    glPopMatrix()
    
    # Soporte derecho
    glPushMatrix()
    glTranslatef(1.4, 0, 0)  # Desplazamos a la derecha
    glBegin(GL_QUADS)
    
    glVertex3f(-0.1, 0, -0.1)   # Esquina inferior izquierda
    glVertex3f(0.1, 0, -0.1)    # Esquina inferior derecha
    glVertex3f(0.1, -1, -0.1)   # Esquina superior derecha
    glVertex3f(-0.1, -1, -0.1)  # Esquina superior izquierda
    
    glVertex3f(-0.1, 0, 0.1)    # Esquina inferior izquierda
    glVertex3f(0.1, 0, 0.1)     # Esquina inferior derecha
    glVertex3f(0.1, -1, 0.1)    # Esquina superior derecha
    glVertex3f(-0.1, -1, 0.1)   # Esquina superior izquierda
    
    glVertex3f(-0.1, 0, -0.1)   # Esquina inferior izquierda
    glVertex3f(-0.1, 0, 0.1)    # Esquina inferior derecha
    glVertex3f(-0.1, -1, 0.1)   # Esquina superior derecha
    glVertex3f(-0.1, -1, -0.1)  # Esquina superior izquierda
    
    glVertex3f(0.1, 0, -0.1)    # Esquina inferior izquierda
    glVertex3f(0.1, 0, 0.1)     # Esquina inferior derecha
    glVertex3f(0.1, -1, 0.1)    # Esquina superior derecha
    glVertex3f(0.1, -1, -0.1)   # Esquina superior izquierda
    
    glEnd()
    glPopMatrix()
    
    

    glPopMatrix()

def draw_scene():
    """Dibuja toda la escena con casas, carretera, árboles, una iglesia, una escuela y una fuente"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configuración de la cámara
    gluLookAt(cam_x, cam_y, cam_z,  # Posición de la cámara
              0, 0, 0,    # Punto al que mira
              0, 1, 0)    # Vector hacia arriba

    # Dibujar el suelo
    draw_ground()

    # Dibujar la carretera
    draw_road()

    # Dibujar las casas en diferentes posiciones
    house_positions = [
        (5, 0, -5),   # Casa 2
        (-5, 0, 5),   # Casa 3
    ]
    for pos in house_positions:
        glPushMatrix()
        glTranslatef(*pos)  # Mover la casa a la posición actual
        draw_house()
        glPopMatrix()

    # Dibujar la iglesia en la posición de la cuarta casa
    glPushMatrix()
    glTranslatef(5, 0, 5)  # Posición de la iglesia
    draw_church()
    glPopMatrix()

    # Dibujar la escuela en la posición de la primera casa
    glPushMatrix()
    glTranslatef(-5, 0, -5)  # Posición de la escuela
    draw_school()
    glPopMatrix()

    # Dibujar la fuente entre la hilera de árboles detrás de la escuela y la casa 3
    glPushMatrix()
    glTranslatef(15, 0, 0)  # Posición de la fuente
    draw_fountain()
    glPopMatrix()
    
    bench_positions = [
        (15, 1, 3),   # Banca 1
        (15, 1, -3),   # Banca 2
    ]
    for pos in bench_positions:
        glPushMatrix()
        glTranslatef(*pos)  # Mover la banca a la posición actual
        draw_bench()
        glPopMatrix()

    # Dibujar los árboles en diferentes posiciones
    tree_positions = [
        (-10, 0, -10), (-8, 0, -10), (-6, 0, -10),  # Línea de árboles 1
        (-10, 0, 10), (-8, 0, 10), (-6, 0, 10),      # Línea de árboles 2
        (10, 0, -10), (8, 0, -10), (6, 0, -10),      # Línea de árboles 3
        (10, 0, 10), (8, 0, 10), (6, 0, 10)          # Línea de árboles 4
    ]
    for pos in tree_positions:
        glPushMatrix()
        glTranslatef(*pos)  # Mover el árbol a la posición actual
        draw_tree(0, 0, 0)
        glPopMatrix()

    glfw.swap_buffers(window)

def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()

    # Crear ventana de GLFW
    width, height = 800, 600
    window = glfw.create_window(width, height, "Pueblo", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    init()

    # Configurar callback de teclado
    glfw.set_key_callback(window, key_callback)

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_scene()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()