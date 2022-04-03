from PhysicalBody import *

class PhysicalConnection:
    def __init__(self, firstBody, secondBody, rigidity):
        self.firstBody = firstBody
        self.secondBody = secondBody
        self.length = (firstBody.position - secondBody.position).length()
        self.rigidity = rigidity

    def Update(self, dt):
        delta = self.secondBody.position - self.firstBody.position
        force = delta.normalize() * (delta.length() - self.length) * self.rigidity
        self.firstBody.AddForce(force, dt)
        self.secondBody.AddForce(-force, dt)

    def Draw(self, screen):
        pg.draw.line(screen, OBJECT_COLOR, WorldToScreen(self.firstBody.position), WorldToScreen(self.secondBody.position), PHYSICAL_CONNECTION_WIDTH)
