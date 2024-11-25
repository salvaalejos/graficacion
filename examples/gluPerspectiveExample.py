import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glEnable(GL_DEPTH_TEST)            # Activar prueba de profundidad

    # Configuración de la proyección en perspectiva
    glMatrixMode(GL_PROJECTION)        # Cambiar a la matriz de proyección
    glLoadIdentity()                   # Resetear la matriz de proyección
    gluPerspective(45, 4/3, 0.1, 60.0) # Configurar perspectiva
    glMatrixMode(GL_MODELVIEW)         # Cambiar a la matriz de modelo/vista

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -10)  # Alejar el objeto de la cámara

    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)  # Rojo
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glEnd()
    
    glfw.swap_buffers(window)

def main():
    global window
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Ejemplo de gluPerspective", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glViewport(0, 0, 800, 600)
    init()

    while not glfw.window_should_close(window):
        draw()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()