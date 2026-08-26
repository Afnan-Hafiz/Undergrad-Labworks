from OpenGL.GL import *     
from OpenGL.GLUT import * 
import math
import random


WIDTH, HEIGHT = 500, 500
Sky_color =[135/255, 206/255, 235/255]
night_color = ( 52/255, 52/255, 52/255)
day_color = (135/255, 206/255, 235/255)
day=True


#rain variables
rain_color =(15/255, 82/255, 186/255)
total_rain_drops = 300
rain_drops = []
bend=0     
for i in range(total_rain_drops):
    m= random.randint(0, 500)
    n= random.randint(0, 500)
    rain_drops.append([m, n])


def figureCoordinates():
    glPointSize(6)     
#housesquare
    #lowertriange
    glBegin(GL_TRIANGLES)
    glColor3f(148/255,123/255,26/255)
    glVertex2d(100,50)  
    glVertex2d(100,350) 
    glVertex2d(400,50) 

    #uppertriangle
    glVertex2d(400,50)
    glVertex2d(100,350)
    glVertex2d(400,350)
    glEnd()

#roof
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2d(80,350)
    glVertex2d(250,450)
    glVertex2d(420,350)
    glEnd() 

#windows
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1)
    
    #left
    glVertex2d(130,220)
    glVertex2d(130,290)
    glVertex2d(190,220)
    
    glVertex2d(190,220)
    glVertex2d(130,290)
    glVertex2d(190,290)
    
    #right
    glVertex2d(310,220)
    glVertex2d(310,290)
    glVertex2d(370,220)

    glVertex2d(370,220)
    glVertex2d(310,290)
    glVertex2d(370,290)
    glEnd()
    
#windowlines
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    #left
    glVertex2d(160,220)  #leftverticalline
    glVertex2d(160,290)
    glVertex2d(130,255)  #lefthorizontaline
    glVertex2d(190,255)
    
    #right
    glVertex2d(340,220)  #rightverticalline
    glVertex2d(340,290)
    glVertex2d(310,255)  #righthorizontaline
    glVertex2d(370,255)
    glEnd()
   
 #door
    glBegin(GL_TRIANGLES)
    glColor3f(150/255, 75/255, 0)
    glVertex2d(220,50)
    glVertex2d(220,150)
    glVertex2d(280,50)
    
    glVertex2d(280,50)
    glVertex2d(220,150)
    glVertex2d(280,150)
    glEnd()
     
#doorknob
    glBegin(GL_POINTS)
    glColor3f(0, 0, 0)
    glVertex2d(265, 100)
    glEnd()

def background():
    global Sky_color
    global night_color  
    global day_color  
    step = 0.001 
    
    if day==False:
        if sum(Sky_color) > sum(night_color):
            Sky_color[0]-= step 
            Sky_color[1]-= step 
            Sky_color[2]-= step  
    else:
        if sum(Sky_color) < sum(day_color):
            Sky_color[0]+= step 
            Sky_color[1]+= step 
            Sky_color[2]+= step
#sky
    glBegin(GL_TRIANGLES)
    glColor3f(*Sky_color)
    glVertex2d(0,250)
    glVertex2d(0,500)
    glVertex2d(500,250)
    
    glVertex2d(500,250)
    glVertex2d(0,500)
    glVertex2d(500,500)
    glEnd()
#ground    
    glBegin(GL_TRIANGLES)
    glColor3f(79/255, 121/255, 66/255)
    glVertex2d(0,0)
    glVertex2d(0,250)
    glVertex2d(500,0)
    
    glVertex2d(500,0)
    glVertex2d(0,250)
    glVertex2d(500,250)
    glEnd()
    
def draw_rain():
    glBegin(GL_LINES)
    glColor3f(*rain_color)
    for i in rain_drops:
        glVertex2d(i[0], i[1])
        glVertex2d(i[0]+bend, i[1]-15)           
    glEnd()

def keyboard_listener(key, x, y):
    global day
    if key==b'd' or key==b'D':
        day = True
        print("Its morning already!")
        
    elif key==b'n' or key==b'N':
        day = False  
        print("Its night time")
        
    glutPostRedisplay()

def special_key_listener(key, x, y):
    global bend
    if key == GLUT_KEY_LEFT:  
        bend -= 5
        if bend < -40:
            bend = -40
        print("Rain moving left")      
    elif key == GLUT_KEY_RIGHT:  
        bend += 5
        if bend > 40:
            bend = 40
        print("Rain moving right")
        
    glutPostRedisplay()

def setup_projection():
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, 0, 1)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    setup_projection()
    background()
    figureCoordinates()
    draw_rain()
    glutSwapBuffers()

def animateRain():
    for i in rain_drops:
        i[1] -= 5
        i[0] += bend * 0.1
        if i[1]<0:
            i[0] = random.randint(0,500)
            i[1] = 500
        if i[0] < 0:
            i[0] = 500
        if i[0] > 500:
            i[0] = 0
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(300, 200)
    glutCreateWindow(b"Interactive House and Rain Animation")
    glutDisplayFunc(display)
    glutIdleFunc(animateRain)
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)
    glutMainLoop()


if __name__ == "__main__":
    main()
