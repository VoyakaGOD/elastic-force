import pygame as pg
from coordSystems import *

class PhysicalBody:
    def __init__(self, mass, position):
        self.invMass = 1 / mass
        self.position = position
        self.velocity = ZERO_VECTOR()
        self.__isFixed = False

    @property
    def IsFixed(self):
        return self.__isFixed

    @IsFixed.setter
    def IsFixed(self, value):
        self.__isFixed = value
        self.velocity = ZERO_VECTOR()

    def AddForce(self, force, dt):
        self.velocity += force * self.invMass * dt

    def Update(self, dt):
        if self.__isFixed:
            return
        self.position += self.velocity * dt
        self.velocity += GRAVITY * dt

    def Draw(self, screen):
        color = OBJECT_COLOR
        if self.__isFixed:
            color = FIXED_BODY_COLOR
        pg.draw.circle(screen, color, WorldToScreen(self.position), BODY_SIZE)

    def ContainsPoint(self, point):
        dx = self.position.x - point.x
        dy = self.position.y - point.y
        return dx*dx + dy*dy < BODY_SIZE*BODY_SIZE 
