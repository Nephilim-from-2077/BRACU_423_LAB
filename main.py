import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *





def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def draw_Lines_for_ID():
    glBegin(GL_LINES)
    glVertex2f(100,150)
    glVertex2f(100,200)

    glEnd()


def draw_Lines():
    #glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(200,300) #jekhane show korbe pixel
    glVertex2f(300,300)
    glVertex2f(300,300)
    glVertex2f(250,400)
    glVertex2f(250,400)
    glVertex2f(200,300)#Upper Triangle Done
    glVertex2f(200,300)
    glVertex2f(200,200)#left line
    glVertex2f(300,300)
    glVertex2f(300,200)#right line
    glVertex2f(200,200)
    glVertex2f(300, 200)#bottom_line

    glEnd()

def draw_Using_Triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(300,300)
    glVertex2f(400,300)
    glVertex2f(400,400)
    glVertex2f(300,300)
    glEnd()


def draw_Using_Quads():
    glBegin(GL_QUADS)
    glVertex2f(240,200)
    glVertex2f(240,225)
    glVertex2f(240,225)
    glVertex2f(260,225)
    glVertex2f(260,225)
    glVertex2f(260,200)
    glVertex2f(260,200)
    glVertex2f(240,200)#door Done
    glVertex2f(215,235)
    glVertex2f(215,245)
    glVertex2f(215,245)
    glVertex2f(225,245)
    glVertex2f(225,245)
    glVertex2f(225,235)
    glVertex2f(225,235)
    glVertex2f(215,235)#left window
    glVertex2f(275,235)
    glVertex2f(275,245)
    glVertex2f(275,245)
    glVertex2f(285,245)
    glVertex2f(285,245)
    glVertex2f(285,235)
    glVertex2f(285,235)
    glVertex2f(275,235)#right window

    glEnd()




def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()



def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here
    #for Task-1
    #for i in range(50):
        #x = random.randrange(100, 400, 1)
        #y = random.randrange(100, 400, 1)
        #draw_points(x,y)
    # For Task 2
    draw_Lines()
    #draw_Using_Triangle()
    # For Task 2
    draw_Using_Quads()
    #draw_Lines_for_ID()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()