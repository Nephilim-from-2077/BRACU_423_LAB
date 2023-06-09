from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)
    # Drawing 6
    draw_line(200, 300, 300, 300)
    draw_line(200, 300, 200, 100)
    draw_line(200, 200, 300, 200)
    draw_line(300, 200, 300, 100)
    draw_line(200, 100, 300, 100)

    # Drawing 6
    glColor3f(0.0, 1.0, 0.456)

    draw_line(350, 300, 450, 300)
    draw_line(350, 300, 350, 200)
    draw_line(350, 200, 350, 100)
    draw_line(350, 200, 450, 200)
    draw_line(450, 200, 450, 100)
    draw_line(350, 100, 450, 100)

    glutSwapBuffers()


def write_pixel(x, y, zone):
    x, y = convert_to_zone_original(x, y, zone)
    print(x, y)
    draw_points(x, y)


def draw_line(x1, y1, x2, y2):
    zone = find_zone(x1, y1, x2, y2)
    x1, y1 = convert_zone_to_zero(x1, y1, zone)
    x2, y2 = convert_zone_to_zero(x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    y = y1
    x = x1
    while x <= x2:
        write_pixel(x, y, zone)
        if d > 0:
            d = d + incNE
            y = y + 1
        else:
            d = d + incE
        x = x + 1


def find_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) >= abs(dy):
        if dx >= 0 and dy > 0:
            zone = 0
        elif dx <= 0 and dy > 0:
            zone = 3
        elif dx <= 0 and dy < 0:
            zone = 4
        else:
            zone = 7
    else:
        if dx >= 0 and dy > 0:
            zone = 1
        elif dx <= 0 and dy > 0:
            zone = 2
        elif dx <= 0 and dy < 0:
            zone = 5
        else:
            zone = 6

    return zone


def convert_zone_to_zero(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    else:
        return x, -y


def convert_to_zone_original(x, y, zone):
    if zone == 2:
        return -y, x
    elif zone == 6:
        return y, -x
    else:
        return convert_zone_to_zero(x, y, zone)



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"ID: 19301166 Draw:66")  # window name
glutDisplayFunc(showScreen)
glutMainLoop()
glutDestroyWindow(wind)




