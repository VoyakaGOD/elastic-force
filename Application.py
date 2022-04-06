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

    def Start(self):
        mass = float(input("Enter mass of bodies:"))
        rigidity = float(input("Enter rigidity of connections:"))
        simulationSpeed = int(input("Enter simulation speed:"))
        simulationQuality =  int(input("Enter simulation quality:"))
        self.__dt = (1/FPS)/simulationQuality
        self.__iterationsCount = simulationSpeed * simulationQuality
        
        #test
        self.simulation = Simulation(mass, rigidity)
        self.simulation.AddBody(Vector2(0,0))
        self.simulation.objects[0].fixed = True
        self.simulation.AddBody(Vector2(130,20))
        self.simulation.AddBody(Vector2(180,40))
        self.simulation.AddConnection(self.simulation.objects[0], self.simulation.objects[1])
        self.simulation.AddConnection(self.simulation.objects[1], self.simulation.objects[2])

    def HandleEvent(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            print(self.simulation.GetObject(GetMouseWorldPosition()))
        if (event.type == pg.KEYDOWN) and (event.key == pg.K_SPACE):
            self.__isPaused = not self.__isPaused

    def Update(self):
        if self.__isPaused:
            return
        for t in range(self.__iterationsCount):
            self.simulation.Update(self.__dt)

    def Draw(self, screen):
        if self.__isPaused:
            return
        self.simulation.Draw(screen)
