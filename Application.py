from Simulation import *

def GetMouseWorldPosition():
    mp = pg.mouse.get_pos()
    return ScreenToWorld(Vector2(mp[0], mp[1]))

class Application:
    def __init__(self):
        self.simulation = None
        self.__dt = 0
        self.__iterationsCount = 1
        self.__isPaused = False
        self.__selectedBody = None
        self.__draggedBody = None

    def Start(self):
        mass = float(input("Enter mass of bodies:"))
        rigidity = float(input("Enter rigidity of connections:"))
        simulationSpeed = int(input("Enter simulation speed:"))
        simulationQuality =  int(input("Enter simulation quality:"))
        self.__dt = (1/FPS)/simulationQuality
        self.__iterationsCount = simulationSpeed * simulationQuality
        self.simulation = Simulation(mass, rigidity)
        
        #test
        self.simulation.AddBody(Vector2(0,0))
        self.simulation.objects[0].IsFixed = True
        self.simulation.AddBody(Vector2(130,20))
        self.simulation.AddBody(Vector2(180,40))
        self.simulation.AddConnection(self.simulation.objects[0], self.simulation.objects[1])
        self.simulation.AddConnection(self.simulation.objects[1], self.simulation.objects[2])

    def HandleEvent(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            obj = self.simulation.GetObject(GetMouseWorldPosition())
            if isinstance(obj, PhysicalBody):
                self.__draggedBody = obj

        if event.type == pg.MOUSEBUTTONUP:
            if self.__draggedBody != None:
                self.__draggedBody.velocity = ZERO_VECTOR()
            self.__draggedBody = None
                    
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.__isPaused = not self.__isPaused
            elif event.key == pg.K_e:
                obj = self.simulation.GetObject(GetMouseWorldPosition())
                if isinstance(obj, PhysicalBody):
                    obj.IsFixed = not obj.IsFixed
            elif event.key == pg.K_a:
                self.simulation.AddBody(GetMouseWorldPosition())
            elif event.key == pg.K_d:
                self.simulation.DeleteObject(GetMouseWorldPosition())
            elif event.key == pg.K_s:
                obj = self.simulation.GetObject(GetMouseWorldPosition())
                if isinstance(obj, PhysicalBody):
                    if (self.__selectedBody != None) and (self.__selectedBody != obj):
                        self.simulation.AddConnection(self.__selectedBody, obj)
                    self.__selectedBody = obj
                else:
                    self.__selectedBody = None

    def Update(self):
        if not self.__isPaused:
            for t in range(self.__iterationsCount):
                self.simulation.Update(self.__dt)
            self.simulation.DeleteUnnecessary()
        if self.__draggedBody != None:
            self.__draggedBody.position = GetMouseWorldPosition()

    def Draw(self, screen):
        self.simulation.Draw(screen)
