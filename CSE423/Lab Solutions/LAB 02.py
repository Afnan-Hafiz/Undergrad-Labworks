from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

WIDTH, HEIGHT = 300, 600
paused= False
cheat=False
game=False
score=0

#catcher
catcher_width= 100
catcher_speed= 10
catcher_height= 20
catcher_on_x= WIDTH/2
catcher_on_y= 40

#diamond
diamond_speed = 0.67
diamond_size = 10
diamond_color= [random.random(), random.random(), random.random()]
diamond_on_x = random.randint(25, WIDTH-25)
diamond_on_y = HEIGHT - 80



#midpoint algorithm starts
def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    
def search_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone=0
    
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx < 0 and dy >= 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        elif dx >= 0 and dy < 0:
            zone = 7
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx < 0 and dy >= 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        elif dx >= 0 and dy < 0:
            zone = 6
    return zone

def convert_to_zone0(x, y, zone):
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
    elif zone == 7:
        return x, -y
    
def convert_to_original_zone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y
#midpoint algorithm ends

def line_drawing(x1, y1, x2, y2):
    zone = search_zone(x1, y1, x2, y2)
    converted_x1, converted_y1 = convert_to_zone0(x1, y1, zone)
    converted_x2, converted_y2 = convert_to_zone0(x2, y2, zone)
    
    dx = converted_x2 - converted_x1
    dy = converted_y2 - converted_y1
    d = (2 * dy) - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    x = converted_x1
    y = converted_y1
       
    while x <= converted_x2:
        OG_x, OG_y = convert_to_original_zone(x, y, zone)
        draw_pixel(OG_x, OG_y)
        if d > 0:
            d += incNE
            y += 1
            x += 1
        else:
            d += incE
            x += 1
   
def special_key_listener(key, x, y):
    global paused
    global cheat
    global game
    global catcher_on_x
    
    if paused or game or cheat:
        print("Game is frozen. Click the Pause button again to continue.")
        return
    if key == GLUT_KEY_LEFT and not game and not cheat:
       catcher_on_x = max(catcher_width/2, catcher_on_x - catcher_speed)
    if key == GLUT_KEY_RIGHT and not game and not cheat:
       catcher_on_x = min(WIDTH - catcher_width/2, catcher_on_x + catcher_speed)
       
    glutPostRedisplay() 
            
def mouse_listener(button, state, x, y):
    global paused
    global game
    new_y = HEIGHT - y
    
    if state != GLUT_DOWN or button != GLUT_LEFT_BUTTON:
        return 
    #arrowbutton-reset
    if 34 <= x <= 66 and 544 <= new_y <= 576:
        resetGame()
    #pausebutton
    elif  134 <= x <= 166 and 544 <= new_y <= 576:    
        if not game:
            paused = not paused
    #closebutton
    elif 234 <= x <= 266 and 544 <= new_y <= 576:    
        print(f"Goodbye! Final score: {score}")
        glutLeaveMainLoop()
        
    if paused:
        print("Game is frozen. Click the Pause button again to continue.")
        return 
def keyboard_listener(key, x, y):
    global cheat
    global catcher_on_x
    
    if not (paused or game or cheat): 
        if key==b'a' or key==b'A':
            catcher_on_x = max(catcher_width/2, catcher_on_x - catcher_speed)
        elif key==b'd' or key==b'D':
            catcher_on_x = min(WIDTH - catcher_width/2, catcher_on_x + catcher_speed)
            
    if key==b'c' or key==b'C':
        cheat= not cheat
        if cheat:
            print("Cheat mode is on")
        else:
            print("Cheat mode is off")
            
    glutPostRedisplay()

def draw_interface():
    #arrow
    glColor3f(0, 1, 1)
    line_drawing(66, 560, 34, 560)
    line_drawing(34, 560, 44, 571)
    line_drawing(34, 560, 44, 549)
    
    #cross
    glColor3f(1,0,0)
    line_drawing(234, 544, 266, 576)
    line_drawing(234, 576, 266, 544)
    
    #pause
    glColor3f(1,1,0)
    if paused:
        line_drawing(142, 576, 142, 544)
        line_drawing(142, 544, 166, 560)
        line_drawing(166, 560, 142, 576)
    else:
        line_drawing(144, 544, 144, 576) 
        line_drawing(156, 544, 156, 576)
        
def draw_catcher():
    global game
    
    if game:
        glColor3f(1,0,0)
    else:
        glColor3f(1,1,1)

    x_left = catcher_on_x - catcher_width // 2
    x_right = catcher_on_x + catcher_width // 2
    y_top = catcher_on_y + catcher_height
    y_bot = catcher_on_y
    
    line_drawing(x_left, y_top, x_right, y_top)
    line_drawing(x_left, y_top, x_left + 10, y_bot)
    line_drawing(x_right, y_top, x_right - 10, y_bot)
    line_drawing(x_left + 10, y_bot, x_right - 10, y_bot)
   
def draw_diamond():
    global diamond_on_x   
    global diamond_on_y 
    global diamond_color
    
    glColor3f(*diamond_color)
    line_drawing(diamond_on_x, diamond_on_y + diamond_size, diamond_on_x + diamond_size, diamond_on_y)
    line_drawing(diamond_on_x + diamond_size, diamond_on_y, diamond_on_x, diamond_on_y - diamond_size)
    line_drawing(diamond_on_x, diamond_on_y - diamond_size, diamond_on_x - diamond_size, diamond_on_y)
    line_drawing(diamond_on_x - diamond_size, diamond_on_y, diamond_on_x, diamond_on_y + diamond_size)
 
 
def resetGame():
    global paused
    global game 
    global diamond_on_x
    global diamond_on_y
    global score
    global diamond_speed 
    global catcher_on_x  
    
    game = False
    paused = False
    score = 0 
    diamond_speed = 0.67
    diamond_on_y = HEIGHT - 80
    diamond_on_x = random.randint(25, WIDTH-25)
    catcher_on_x = WIDTH / 2
    print("Starting Over!")
    
def animation():
    global paused
    global game 
    global diamond_on_x
    global diamond_on_y
    global score
    global diamond_speed
    global catcher_on_x 
    
    if game or paused:
        return
    if cheat:
        if diamond_on_x > catcher_on_x:
            catcher_on_x += catcher_speed           
        elif diamond_on_x < catcher_on_x:      
            catcher_on_x -= catcher_speed
    diamond_on_y -= diamond_speed
    update_score()  
    
    glutPostRedisplay()
def update_score():
    global game 
    global diamond_on_x
    global diamond_on_y
    global score
    global diamond_speed
    global diamond_color
    
    catcher_left = catcher_on_x - catcher_width / 2
    catcher_top = catcher_on_y
    catcher_right = catcher_left + catcher_width
    catcher_bottom = catcher_top + catcher_height

    diamond_left = diamond_on_x - diamond_size
    diamond_top = diamond_on_y - diamond_size
    diamond_right = diamond_left + diamond_size * 2
    diamond_bottom = diamond_top + diamond_size * 2
     
    if (catcher_left < diamond_right and catcher_right > diamond_left and catcher_top < diamond_bottom and catcher_bottom > diamond_top):
        score += 1
        print(f"Score: {score}")
        diamond_color = [random.random(), random.random(), random.random()]
        diamond_speed += 0.03
        diamond_on_x = random.randint(25, WIDTH-25)
        diamond_on_y = HEIGHT - 80
        
    elif diamond_on_y - diamond_size <= 0:
        print(f"Game Over! Score: {score}")
        game = True

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_interface()
    draw_catcher()
    draw_diamond()
    glutSwapBuffers()

def setup_projection():
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(300, 100)
    glutCreateWindow(b"Diamond Catcher Game")
    setup_projection()
    glutDisplayFunc(display)
    glutIdleFunc(animation)
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)
    glutMouseFunc(mouse_listener)
    glutMainLoop()


if __name__ == "__main__":
    main()
