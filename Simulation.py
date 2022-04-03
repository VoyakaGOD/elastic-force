from PhysicalConnection import *

class Simulation:
    def __init__(self, mass, rigidity):
        self.mass = mass
        self.rigidity = rigidity
        self.objects = []

    def AddBody(self, position):
        self.objects += [PhysicalBody(self.mass, position)]
        
    def AddConnection(self, body1, body2):
        self.objects += [PhysicalConnection(body1, body2, self.rigidity)]

    def UpdateAndDraw(self, dt, screen):
        screen.fill(BACKGROUND_COLOR)
        for obj in self.objects:
            obj.Update(dt)
            obj.Draw(screen)
        pg.display.update()

    def GetObject(position):
        return None
