from constants import *

half_screen_width = DEFAULT_SCREEN_WIDTH * 0.5
half_screen_height = DEFAULT_SCREEN_HEIGHT * 0.5

def WorldToScreen(position):
    return Vector2(half_screen_width + position.x, half_screen_height - position.y)

def ScreenToWorld(position):
    return Vector2(position.x - half_screen_width, half_screen_height - position.y)

def UpdateScreenSizeInfo(width, height):
    global half_screen_width
    global half_screen_height
    half_screen_width = width * 0.5
    half_screen_height = height * 0.5
