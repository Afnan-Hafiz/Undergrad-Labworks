from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math 

first_person_mode = False
WIDTH, HEIGHT = 1400, 700
game_over = False
cheat_mode = False
missed_bullets = 0
total_villains = 5
villians = []
gun_angle = 0
total_bullets = []
cheat_targets_fired = set() 

# Camera-related variables
perspective = [0, 1320, 900, 0, 0, 0, 0, 0, 1] 
fovY = 45
GRID_LENGTH = 600  
angle_of_camera = 0
radius_of_camera = 500
gun_pov_angle = 0
gun_pov = False

#Player-related variables
player_pos = [0, 0, 0] 
player_lives = 5
player_score = 0

def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18, color=(1,1,1)):
    glColor3f(*color)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    
    # Set up an orthographic projection that matches window coordinates
    gluOrtho2D(0, WIDTH, 0, HEIGHT)  # left, right, bottom, top

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    # Draw text at (x, y) in screen coordinates
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    
    # Restore original projection and modelview matrices
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def draw_board():
    tiles_per_side = 10
    tile_size = (2 * GRID_LENGTH) / tiles_per_side
    wall_height = 35
    
    glBegin(GL_QUADS)
    for i in range(tiles_per_side):
        for j in range(tiles_per_side):
            x = -GRID_LENGTH + i * tile_size
            y = -GRID_LENGTH + j * tile_size
            
            if (i + j) % 2 == 0:
                glColor3f(0.7, 0.5, 0.95)
            else:
                glColor3f(1, 1, 1)
    
            glVertex3f(x, y, 0)
            glVertex3f(x + tile_size, y, 0)
            glVertex3f(x + tile_size, y + tile_size, 0)
            glVertex3f(x, y + tile_size, 0)
    glEnd()
    
    #wall 1 left orange
    glBegin(GL_QUADS)
    glColor3f(1, 0.55, 0)
    glVertex3f(-GRID_LENGTH, -GRID_LENGTH, 0)
    glVertex3f(-GRID_LENGTH, GRID_LENGTH, 0)
    glVertex3f(-GRID_LENGTH, GRID_LENGTH, wall_height)
    glVertex3f(-GRID_LENGTH, -GRID_LENGTH, wall_height)
    glEnd()
    
    #wall 2 right green
    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)
    glVertex3f(GRID_LENGTH, -GRID_LENGTH, 0)
    glVertex3f(GRID_LENGTH, GRID_LENGTH, 0)
    glVertex3f(GRID_LENGTH, GRID_LENGTH, wall_height)
    glVertex3f(GRID_LENGTH, -GRID_LENGTH, wall_height)
    glEnd()
    
    #wall 3 front blue
    glBegin(GL_QUADS)
    glColor3f(0, 0, 1)
    glVertex3f(-GRID_LENGTH, -GRID_LENGTH, 0)
    glVertex3f(GRID_LENGTH, -GRID_LENGTH, 0)
    glVertex3f(GRID_LENGTH, -GRID_LENGTH, wall_height)
    glVertex3f(-GRID_LENGTH, -GRID_LENGTH, wall_height)
    glEnd()
    
    #wall 4 back cyan
    glBegin(GL_QUADS)
    glColor3f(0, 1, 1)
    glVertex3f(-GRID_LENGTH, GRID_LENGTH, 0)
    glVertex3f(GRID_LENGTH, GRID_LENGTH, 0)
    glVertex3f(GRID_LENGTH, GRID_LENGTH, wall_height)
    glVertex3f(-GRID_LENGTH, GRID_LENGTH, wall_height)
    glEnd()

def draw_character():
    if first_person_mode and not game_over:
        return
    glPushMatrix()
    glTranslatef(player_pos[0], player_pos[1], player_pos[2])
    glRotatef(-gun_angle, 0, 0, 1)
    if game_over:
        glRotatef(-90, 1, 0, 0)
        glTranslatef(0, 0, -20)
    
    #legs
    glPushMatrix()
    glColor3f(0, 0, 1)
    glTranslatef(-10, 0, 0) #1st leg
    gluCylinder(gluNewQuadric(), 4, 4, 30, 10, 10)
    
    glTranslatef(20, 0, 0)  #2nd leg
    gluCylinder(gluNewQuadric(), 4, 4, 30, 10, 10)
    glPopMatrix()

    #body
    glPushMatrix()
    glColor3f(0.7, 0.2, 0.9)
    glTranslatef(0, 0, 45)
    glScalef(1, 1, 1.5)
    glutSolidCube(30)
    glPopMatrix()
    
    #arms
    glColor3f(1.0, 0.8, 0.6)
    glPushMatrix()              #1st arm
    glTranslatef(-15, 0, 60)
    glRotatef(-90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 5, 5, 40, 10, 10)
    glPopMatrix()
    
    glPushMatrix()              #2nd arm
    glTranslatef(15, 0, 60) 
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 5, 5, 40, 10, 10)
    glPopMatrix()
    
    #head
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslatef(0, 0, 75)  
    gluSphere(gluNewQuadric(), 22, 16, 16)
    glPopMatrix() 
    
    #gun
    glPushMatrix()
    glColor3f(0.75, 0.75, 0.75)  
    glTranslatef(0, 42, 40)
    glRotatef(90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 4, 3, 40, 12, 12)
    glPopMatrix()
    
    glPopMatrix()
    
def draw_villain(x, y, z=0, r=20):
    glPushMatrix()
    glTranslatef(x, y, z)
    
    #head
    glPushMatrix()
    glColor3f(0, 0, 0)  
    glTranslatef(0, 0, 35)
    gluSphere(gluNewQuadric(), r * 0.6, 10, 10)  
    glPopMatrix()
    
    #body
    glPushMatrix()
    glColor3f(1, 0, 0)
    glTranslatef(0, 0, 15)
    gluSphere(gluNewQuadric(), r, 10, 10)
    glPopMatrix()
    
    glPopMatrix()

def draw_bullet():
    for bullet in total_bullets:
        glPushMatrix()
        glColor3f(1, 1, 0)  
        glTranslatef(bullet['x'], bullet['y'], bullet['z'])
        glutSolidCube(8)
        glPopMatrix()
        
def get_view_angle():
    if cheat_mode and not gun_pov:
        return gun_pov_angle
    return gun_angle       

def draw_first_person_hands():
    view_angle = get_view_angle()
    eye_x = player_pos[0] + math.sin(math.radians(view_angle)) * 5
    eye_y = player_pos[1] + math.cos(math.radians(view_angle)) * 5
    eye_z = 55
    hand_x = eye_x + math.sin(math.radians(view_angle)) * 15
    hand_y = eye_y + math.cos(math.radians(view_angle)) * 15 
    
    #arms
    glPushMatrix()
    glTranslatef(hand_x, hand_y, eye_z - 15)
    glRotatef(view_angle, 0, 0, 1)
    
    glColor3f(1.0, 0.8, 0.6)  
    glPushMatrix()
    glTranslatef(-12, 0, 0)
    glRotatef(-90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 5, 5, 30, 10, 10)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(12, 0, 0)
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 5, 5, 30, 10, 10)
    glPopMatrix()
    
    #gun
    glColor3f(0.75, 0.75, 0.75)  
    glPushMatrix()
    glTranslatef(0, 8, 0)
    glRotatef(90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 6, 1, 45, 12, 12)
    glPopMatrix()
 
    glPopMatrix()

def reset_game():
    global player_pos, perspective, cheat_mode, game_over, gun_pov, player_lives, player_score, missed_bullets, total_villains, gun_angle, angle_of_camera, gun_pov_angle, villians, cheat_targets_fired
    
    player_pos = [0, 0, 0]  
    perspective = [0, 1320, 900, 0, 0, 0, 0, 0, 1] 
    cheat_mode = False
    game_over = False  
    gun_pov = False
    missed_bullets = 0
    player_lives = 5
    total_villains = 5
    gun_pov_angle = 0
    gun_angle = 0
    angle_of_camera = 0
    player_score = 0
    total_bullets.clear()
    villians.clear() 
    cheat_targets_fired.clear()
    
    while len(villians) < total_villains: 
        spawn_villain()

def villian_coordinates():
    x = random.randint(-GRID_LENGTH + 20, GRID_LENGTH - 20)
    y = random.randint(-GRID_LENGTH + 20, GRID_LENGTH - 20)
    return [x, y]

def spawn_villain():
    global villians
    if len(villians) < total_villains: 
        villians.append(villian_coordinates())

def cheat_mode_shoot(b):
    global gun_angle
    direction_x = b[0] - player_pos[0] 
    direction_y = b[1] - player_pos[1] 
    gun_angle = math.degrees(math.atan2(direction_x, direction_y)) % 360
    return gun_angle
    
def enemy_to_player_movement():
    for movement in villians:
        direction_x = player_pos[0] - movement[0]
        direction_y = player_pos[1] - movement[1]
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        if distance > 0:
            movement[0] += (direction_x / distance) * 0.22  
            movement[1] += (direction_y / distance) * 0.22
        else:
            movement[0] = player_pos[0]
            movement[1] = player_pos[1]
        
def shoot_bullet():
    direction_x = math.sin(math.radians(gun_angle))
    direction_y = math.cos(math.radians(gun_angle))
    muzzle_x = player_pos[0] + direction_x * 80
    muzzle_y = player_pos[1] + direction_y * 80 
    total_bullets.append({'x': muzzle_x, 'y': muzzle_y, 'z': 55, 'direction_x': direction_x, 'direction_y': direction_y})

def check_hitmiss():
    global player_score, missed_bullets, villians, total_villains
    for bullet in list(total_bullets):
        bullet['x'] += bullet['direction_x'] * 14
        bullet['y'] += bullet['direction_y'] * 14
        if abs(bullet['x']) > GRID_LENGTH or abs(bullet['y']) > GRID_LENGTH:
            total_bullets.remove(bullet)
            missed_bullets += 1
            print("Missed Your Shot! Total Missed Bullets:", missed_bullets)
            continue
        for enemy in list(villians):
            distance = math.sqrt((bullet['x'] - enemy[0]) ** 2 + (bullet['y'] - enemy[1]) ** 2)
            if distance < 20:  
                villians.remove(enemy)
                total_bullets.remove(bullet)
                player_score += 1
                print("You Hit a Villain! Total Score:", player_score)
                break
        
def check_collision():
    global player_lives, game_over
    
    for villain in villians:
        distance = math.sqrt((player_pos[0] - villain[0]) ** 2 + (player_pos[1] - villain[1]) ** 2)
        if distance < 30:  
            player_lives -= 1
            print("You were hit by a villain! Lives left:", player_lives)
            villians.remove(villain)  
            
            if player_lives <= 0:
                game_over = True
                print("Game Over! Press 'R' to Restart.")
            break
        
def animation():
    global villians, total_villains, game_over, gun_angle
    if player_lives <= 0 or missed_bullets >= 10:
        game_over = True
        print("Game Over! Press 'R' to Restart.")
        
    if not game_over:
        if len(villians) < total_villains:
            spawn_villain()
        if cheat_mode and villians:
            nearest_enemy = min(villians, key=lambda enemy: math.sqrt(
                    (enemy[0] - player_pos[0]) ** 2 +
                    (enemy[1] - player_pos[1]) ** 2))
            cheat_mode_shoot(nearest_enemy)
            if len(total_bullets) == 0:
                shoot_bullet()
                
        enemy_to_player_movement()
        check_hitmiss()
        check_collision()
        
    glutPostRedisplay() 
    
     
def keyboardListener(key, x, y):
    global player_pos, cheat_mode, game_over, gun_pov, gun_angle, gun_pov_angle, perspective, first_person_mode
    
    if key == b'r' or key == b'R':
        reset_game() 
        return 
    if not game_over:  
        position = math.radians(gun_angle)         
        if key == b'w' or key == b'W':
            player_pos[0] += math.sin(position) * 10
            player_pos[1] += math.cos(position) * 10
            
        if key == b's' or key == b'S':
            player_pos[0] -= math.sin(position) * 10
            player_pos[1] -= math.cos(position) * 10

        if key == b'a' or key == b'A':
            if cheat_mode:
                gun_pov_angle = (gun_pov_angle - 5) % 360 
            else:
                gun_angle = (gun_angle - 5) % 360 

        if key == b'd' or key == b'D':
            if cheat_mode: 
                gun_pov_angle = (gun_pov_angle + 5) % 360 
            else:
                gun_angle = (gun_angle + 5) % 360
            
        if key == b'c' or key == b'C':
            cheat_mode = not cheat_mode
            cheat_targets_fired.clear()
            if cheat_mode:
                gun_pov_angle = gun_angle
            
        if key == b'v' or key == b'V':
            gun_pov = not gun_pov  
            
        player_pos[0] = max(-GRID_LENGTH + 15, min(GRID_LENGTH - 15, player_pos[0]))
        player_pos[1] = max(-GRID_LENGTH + 15, min(GRID_LENGTH - 15, player_pos[1]))  
        
    else:
        return

def specialKeyListener(key, x, y):
    global perspective, first_person_mode, game_over
    x, y, z = perspective[0], perspective[1], perspective[2]
    
    if not first_person_mode and not game_over:
        if key == GLUT_KEY_UP:
            z += 10

        elif key == GLUT_KEY_DOWN:
            z -= 10

        elif key == GLUT_KEY_LEFT:
            x -=10

        elif key == GLUT_KEY_RIGHT:
            x += 5

        perspective = (x, y, z, 0, 0, 0, 0, 0, 1)
        glutPostRedisplay()  


def mouseListener(button, state, x, y):
    global first_person_mode, game_over
    if not game_over:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            print("Shots Fired")
            shoot_bullet()
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            first_person_mode = not first_person_mode


def setupCamera():
    glMatrixMode(GL_PROJECTION)  
    glLoadIdentity()  
    gluPerspective(fovY, WIDTH/HEIGHT, 0.1, 3000) 
    glMatrixMode(GL_MODELVIEW)  
    glLoadIdentity() 
    
    if first_person_mode:
        view_angle = get_view_angle()
        eye_x = player_pos[0] + math.sin(math.radians(view_angle)) * 5
        eye_y = player_pos[1] + math.cos(math.radians(view_angle)) * 5
        eye_z = 55
        look_x = eye_x + math.sin(math.radians(view_angle)) * 100
        look_y = eye_y + math.cos(math.radians(view_angle)) * 100          
        gluLookAt(eye_x, eye_y, eye_z, look_x, look_y, eye_z, 0, 0, 1)
    
    else:
        gluLookAt(
            perspective[0], perspective[1], perspective[2],
            perspective[3], perspective[4], perspective[5],
            perspective[6], perspective[7], perspective[8]
        )
        
def idle():
    global game_over
    if game_over:
        return
    else:
        animation()
    glutPostRedisplay()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  
    glViewport(0, 0, WIDTH, HEIGHT)  
    setupCamera() 
    draw_board()
    draw_character()
    for villain in villians:
        draw_villain(villain[0], villain[1])
    draw_bullet()
    if first_person_mode and not game_over:  
        draw_first_person_hands()
    draw_text(10, HEIGHT - 20, f"Player Life Remaining: {player_lives}")
    draw_text(10, HEIGHT - 40, f"Game Score: {player_score}")
    draw_text(10, HEIGHT - 60, f"Player Bullet Missed: {missed_bullets}")
    
    if game_over:
        draw_text(WIDTH // 2 - 50, HEIGHT // 2, "Game Over! You Died!", color = (1,0,0))
        draw_text(WIDTH // 2 - 100, HEIGHT // 2 - 20, "Press 'R' to Restart The Mission", color = (1,0,0))
    
    if cheat_mode:
        draw_text(WIDTH - 150, HEIGHT - 20, "Cheat Mode ON")

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  
    glutInitWindowSize(WIDTH, HEIGHT) 
    glutInitWindowPosition(0, 0)  
    glutCreateWindow(b"Bullet Frenzy Game") 
    reset_game()
    glutDisplayFunc(showScreen) 
    glutKeyboardFunc(keyboardListener) 
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle) 
    glutMainLoop()  
    
if __name__ == "__main__":
    main()