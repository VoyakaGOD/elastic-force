import pygame as pg
from pygame import Vector2

WHITE_COLOR = (0, 0, 0)
ZERO_VECTOR = Vector2(0, 0)
BODY_SIZE = 5

class PhysicalBody:
    def __init__(self, mass, position):
        self.invMass = 1 / mass
        self.position = position
        self.velocity = ZERO_VECTOR

    def AddForce(self, force):
        self.velocity += force * self.invMass

    def Update(self, dt):
        self.position += self.velocity * dt

    def Draw(self, screen):
        pg.draw.circle(screen, WHITE_COLOR, self.position, BODY_SIZE)
