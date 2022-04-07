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

    def Update(self, dt):
        for obj in self.objects:
            obj.Update(dt)

    def Draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        for obj in self.objects:
            obj.Draw(screen)
        pg.display.update()

    def GetObject(self, position):
        for obj in self.objects:
            if obj.ContainsPoint(position):
                return obj
        return None

    def DeleteObject(self, position):
        deletedObject = None
        for obj in self.objects:
            if obj.ContainsPoint(position):
                deletedObject = obj
                break
        if isinstance(deletedObject, PhysicalBody):
            for i in range(len(self.objects) - 1, -1, -1):
                if isinstance(self.objects[i], PhysicalConnection) and self.objects[i].DependsOn(deletedObject):
                    del self.objects[i]
        if deletedObject != None:
            self.objects.remove(deletedObject)

    def DeleteUnnecessary(self):
        sqrLimit = POSITION_LIMIT*POSITION_LIMIT
        for i in range(len(self.objects) - 1, -1, -1):
            if isinstance(self.objects[i], PhysicalBody):
                if self.objects[i].position.length_squared() > sqrLimit:
                    del self.objects[i]
            elif (self.objects[i].firstBody.position.length_squared() > sqrLimit) or (self.objects[i].secondBody.position.length_squared() > sqrLimit):
                del self.objects[i]
                
        
