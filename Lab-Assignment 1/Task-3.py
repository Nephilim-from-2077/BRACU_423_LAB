from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_lines(x1,y1,x2,y2):
    glPointSize(20) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)#jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here


    # Drawing 1
    glColor3f(0.0, 1.0, 1.0)
    draw_lines(50, 400, 50, 600)

    # Drawing 9
    glColor3f(1.0, 0.0, 1.0)
    draw_lines(70, 500, 70, 600)
    draw_lines(70, 600, 150, 600)
    draw_lines(150, 600, 150, 400)
    draw_lines(70, 400, 150, 400)
    draw_lines(70, 500, 150, 500)



    #Drawing 1

    glColor3f(0.0, 1.0, 1.0)
    draw_lines(170, 400, 170, 600)


    # Drawing 0
    glColor3f(0.5, 0.0, 1.0)
    draw_lines(190, 600, 270, 600)
    draw_lines(190, 600, 190, 400)
    draw_lines(190, 400, 270, 400)
    draw_lines(270, 400, 270, 600)

    # Drawing 1
    glColor3f(0.5, 1.0, 0.0)
    draw_lines(290, 400, 290, 600)

    # # draw_lines(290, 400, 290, 600)

    #Drawing 1

    glColor3f(1.0, 0.5, 1.0)
    draw_lines(330, 400, 330, 600)


    #Drawing 2
    glColor3f(1.0, 0.0, 0.0)
    draw_lines(350, 600, 430, 600)
    draw_lines(430, 600, 430, 500)
    draw_lines(350, 500, 430, 500)
    draw_lines(350, 500, 350, 400)
    draw_lines(350, 400, 430, 400)



    #Drawing 5
    glColor3f(0.3, 0.0, 0.9)
    draw_lines(450, 600, 530, 600)
    draw_lines(450, 600, 450, 500)
    draw_lines(450, 500, 530, 500)
    draw_lines(530, 500, 530, 400)
    draw_lines(450, 400, 530, 400)









    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()