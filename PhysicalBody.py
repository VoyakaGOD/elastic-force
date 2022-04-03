import pygame as pg
from pygame import Vector2

GRAVITY = Vector2(0, -9.81)
WHITE_COLOR = (255, 255, 255)
ZERO_VECTOR = Vector2(0, 0)
BODY_SIZE = 5

class PhysicalBody:
    def __init__(self, mass, position):
        self.invMass = 1 / mass
        self.position = position
        self.velocity = ZERO_VECTOR

    def AddForce(self, force, dt):
        self.velocity += force * self.invMass * dt

    def Update(self, dt):
        self.position += self.velocity * dt
        self.AddForce(GRAVITY, dt)

    def Draw(self, screen):
        pg.draw.circle(screen, WHITE_COLOR, self.position, BODY_SIZE)
