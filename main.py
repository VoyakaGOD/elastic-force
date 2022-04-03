from Simulation import *

class App:
    def __init__(self):
        self.screen = pg.display.set_mode((330, 330))
        self.clock = pg.time.Clock()
        pg.display.set_caption('elastic force')

    def run(self):
        isRunning = True
        test = Simulation(10, 100)
        test.AddBody(Vector2(30,30))
        test.objects[0].fixed = True
        test.AddBody(Vector2(130,20))
        test.AddConnection(test.objects[0], test.objects[1])
        while isRunning:
            test.UpdateAndDraw(0.1, self.screen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    isRunning = False
            self.clock.tick(60)
        pg.quit()

if __name__ == '__main__':
    app = App()
    app.run()
