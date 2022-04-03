from PhysicalBody import *

PHYSICAL_CONNECTION_WIDTH = 3

class PhysicalConnection:
    def __init__(self, firstBody, secondBody, rigidity):
        self.firstBody = firstBody
        self.secondBody = secondBody
        self.length = (firstBody.position - secondBody.position).length()
        self.rigidity = rigidity

    def Update(self, dt):
        delta = secondBody.position - firstBody.position
        force = delta.normalize() * (delta.length() - self.length) * k
        firstBody.AddForce(force, dt)
        secondBody.AddForce(-force, dt)

    def Draw(self, screen):
        pg.draw.line(screen, WHITE_COLOR, self.firstBody.position, self.secondBody.position, PHYSICAL_CONNECTION_WIDTH)
