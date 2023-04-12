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
    glColor3f(0.5, 0.5, 0.5)  # konokichur color set (RGB)
    draw_circle(500, 500, 300)  # draw a circle with center (500, 500) and radius 300
    draw_circle(650, 500, 150)
    draw_circle(350, 500, 150)
    draw_circle(500, 650, 150)
    draw_circle(500, 350, 150)
    draw_circle(606.0660172, 606.0660172, 150)#Upper Right
    draw_circle(393.9339828, 606.0660172, 150)#Upper Left
    draw_circle(393.9339828, 393.9339828, 150)#Lower Left
    draw_circle(606.0660172, 393.9339828, 150)#Lower Right
    glutSwapBuffers()

def write_pixel(x, y, xc, yc):
    draw_points(xc + x, yc + y)
    draw_points(xc + x, yc - y)
    draw_points(xc - x, yc + y)
    draw_points(xc - x, yc - y)
    draw_points(xc + y, yc + x)
    draw_points(xc + y, yc - x)
    draw_points(xc - y, yc + x)
    draw_points(xc - y, yc - x)

def draw_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    write_pixel(x, y, xc, yc)
    while y > x: #East
        if d < 0:
            d = d + 2 * x + 3

        else:   #South East
            d = d + 2 * (x - y) + 5
            y -= 1
        x += 1
        write_pixel(x, y, xc, yc)

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000,1000)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Draw Circle using Midpoint Circle Algorithm")  # window name
glutDisplayFunc(showScreen)
glutMainLoop()
glutDestroyWindow(wind)