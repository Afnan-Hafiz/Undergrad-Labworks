# ====== PyOpenGL Interactive Example ======
# Features:
#   - Draws coordinate axes, triangle, and square
#   - Displays a moving point ("ball")
#   - Left-click to reposition ball
#   - Right-click to create an extra point
#   - Use UP/DOWN arrow keys to change ball speed
#   - Use W/S keys to increase/decrease ball size
#
#   Author: Abid Jahan Apon
# ===========================================

from OpenGL.GL import *      # Core OpenGL functions
from OpenGL.GLUT import *    # GLUT library for window and input handling
from OpenGL.GLU import *     # OpenGL Utility library
import math

# ===== Global Variables =====
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
ball_x, ball_y = 0, 0        # Ball coordinates (in OpenGL space)
ball_speed = 0.01            # Ball movement speed
ball_size = 2                # Ball size (GL point size)
new_point = False            # Whether a new point is created on right-click


# ===== Coordinate Conversion =====
def convert_coordinate(x, y):
    """
    Converts mouse (screen) coordinates to OpenGL (Cartesian) coordinates.
    Top-left of the window is (0,0) in screen space,
    but OpenGL center is (0,0).
    """
    a = x - (WINDOW_WIDTH / 2)
    b = (WINDOW_HEIGHT / 2) - y
    return a, b


# ===== Draw Functions =====
def draw_point(x, y, size):
    """Draws a single point at (x, y) with given size."""
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_axes():
    """Draws X and Y axes centered at origin."""
    glLineWidth(1)
    glBegin(GL_LINES)
    # X-axis (red)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-250, 0)
    glVertex2f(250, 0)
    # Y-axis (blue)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0, -250)
    glVertex2f(0, 250)
    glEnd()

    # Draw origin (green point)
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0, 0)
    glEnd()


def draw_shapes():
    """Draws a triangle and a square with color gradients."""
    # Triangle
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2d(-160, 150)
    glColor3f(0, 1, 0)
    glVertex2d(-180, 150)
    glColor3f(0, 0, 1)
    glVertex2d(-170, 170)
    glEnd()

    # Square (quad)
    glBegin(GL_QUADS)
    glColor3f(1, 0, 1)
    glVertex2d(-170, 120)
    glColor3f(0, 0, 1)
    glVertex2d(-150, 120)
    glColor3f(0, 1, 0)
    glVertex2d(-150, 140)
    glColor3f(1, 1, 0)
    glVertex2d(-170, 140)
    glEnd()


# ===== Keyboard & Mouse Interaction =====
def keyboard_listener(key, x, y):
    """Handles normal keyboard inputs."""
    global ball_size
    if key == b'w':  # Increase size
        ball_size += 1
        print("Ball size increased")
    elif key == b's':  # Decrease size
        ball_size = max(1, ball_size - 1)
        print("Ball size decreased")
    glutPostRedisplay()


def special_key_listener(key, x, y):
    """Handles special keys (arrows, F-keys, etc.)."""
    global ball_speed
    if key == GLUT_KEY_UP:
        ball_speed *= 2
        print("Speed increased")
    elif key == GLUT_KEY_DOWN:
        ball_speed /= 2
        print("Speed decreased")
    glutPostRedisplay()


def mouse_listener(button, state, x, y):
    """
    Handles mouse clicks.
    Left-click: Move ball.
    Right-click: Create a new point.
    """
    global ball_x, ball_y, new_point
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        ball_x, ball_y = convert_coordinate(x, y)
        print(f"Ball moved to ({ball_x}, {ball_y})")

    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        new_point = convert_coordinate(x, y)
        print(f"New point created at {new_point}")


# ===== Projection Setup =====
def setup_projection():
    """Defines a 2D orthographic coordinate system."""
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -250, 250, 0, 1)
    glMatrixMode(GL_MODELVIEW)


# ===== Display & Animation =====
def display():
    """Main display callback for rendering each frame."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    setup_projection()

    draw_axes()
    draw_shapes()
    draw_point(ball_x, ball_y, ball_size)

    # Draw bounding L-shape in the top-right corner
    glBegin(GL_LINES)
    glVertex2d(180, 0)
    glVertex2d(180, 180)
    glVertex2d(180, 180)
    glVertex2d(0, 180)
    glEnd()

    # Draw the right-clicked point (if any)
    if new_point:
        px, py = new_point
        glColor3f(0.7, 0.8, 0.6)
        draw_point(px, py, 6)

    glutSwapBuffers()


def animate():
    """Continuously moves the ball diagonally."""
    global ball_x, ball_y, ball_speed
    ball_x = (ball_x + ball_speed) % 180
    ball_y = (ball_y + ball_speed) % 180
    glutPostRedisplay()


# ===== Main Function =====
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Interactive Animation")

    # Register callback functions
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)
    glutMouseFunc(mouse_listener)

    glutMainLoop()


# ===== Entry Point =====
if __name__ == "__main__":
    main()
