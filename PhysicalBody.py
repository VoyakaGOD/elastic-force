import pygame as pg
from constants import *

def WorldToScreen(position):
    return Vector2(165 + position.x, 165 - position.y)

class PhysicalBody:
    def __init__(self, mass, position):
        self.invMass = 1 / mass
        self.position = position
        self.velocity = ZERO_VECTOR()
        self.fixed = False

    def AddForce(self, force, dt):
        self.velocity += force * self.invMass * dt

    def Update(self, dt):
        if self.fixed:
            return
        self.position += self.velocity * dt
        self.AddForce(GRAVITY, dt)

    def Draw(self, screen):
        color = OBJECT_COLOR
        if self.fixed:
            color = FIXED_BODY_COLOR
        pg.draw.circle(screen, color, WorldToScreen(self.position), BODY_SIZE)
