from OpenGL.GL import *     
from OpenGL.GLUT import * 
import math
import random
WIDTH, HEIGHT = 500, 500
speed = 0.06
blink_counter = 0
freeze = False
blink = False
blink_time = 1000
dots=[]

def convert_coordinate(x, y):
    a = x - (WIDTH / 2)
    b = (HEIGHT / 2) - y
    return a, b
    
def keyboard_listener(key, x, y):
    global freeze
    if key == b' ':
        freeze = not freeze
        print("Animation frozen"if freeze==True else "Animation resumed")
        
    glutPostRedisplay()


def special_key_listener(key, x, y):   
    global speed
    
    if freeze:
        print("Animation is frozen. Press Spacebar to continue.")
        return
    if key == GLUT_KEY_UP:
        speed += 0.06
        print("Ball speed increased")    
    elif key == GLUT_KEY_DOWN:
        speed = max(0, speed - 0.06)
        print("Ball speed decreased")

    glutPostRedisplay()

def mouse_listener(button, state, x, y):
    global dots
    global blink
    
    if state != GLUT_DOWN:
        return  
    if freeze:
        print("Animation is frozen. Press Spacebar to continue.")
        return 
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and not freeze:
        blink = not blink
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN and not freeze:
        new_x,new_y = convert_coordinate(x,y)
        direcx =  random.choice([-1,1])
        direcy = random.choice([-1,1])
        color = [random.random(), random.random(), random.random()]
        dots.append([new_x, new_y, direcx, direcy, color[0], color[1], color[2]])
 
def animatedots():
    global dots
    global blink
    global blink_counter
    global blink_time
    
    if freeze:
        glutPostRedisplay()
        return    
    if not freeze:
        for point in dots:
            point[0] += point[2] * speed
            point[1] += point[3] * speed
            if point[0] <= -WIDTH / 2 or point[0] >= WIDTH / 2:
                point[2] *= -1
            if point[1] <= -HEIGHT / 2 or point[1] >= HEIGHT / 2:
                point[3] *= -1

        if blink:
            blink_counter += 1
            if blink_counter >= blink_time * 2:  
                blink_counter = 0
        else:
            blink_counter = 0
            
    glutPostRedisplay()
    
def setup_projection():
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-WIDTH/2, WIDTH/2, -HEIGHT/2, HEIGHT/2, 0, 1)
    glMatrixMode(GL_MODELVIEW)

def point_drawing(x, y, size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    setup_projection()

    for point in dots:
        x, y, direction_x, direction_y, color_x, color_y, color_z = point
        if not blink or blink_counter <= blink_time:
            glColor3f(color_x, color_y, color_z)
        else:
            glColor3f(0, 0, 0)
            
        point_drawing(x, y, 5)
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(300, 200)
    glutCreateWindow(b"Blinking Dots Animation")
    glutDisplayFunc(display)
    glutIdleFunc(animatedots)
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)
    glutMouseFunc(mouse_listener)
    glutMainLoop()


if __name__ == "__main__":
    main()