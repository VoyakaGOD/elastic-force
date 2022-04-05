from Simulation import *

def GetMouseWorldPosition():
    mp = pg.mouse.get_pos()
    return ScreenToWorld(Vector2(mp[0], mp[1]))

class App:
    def __init__(self):
        self.screen = pg.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), pg.RESIZABLE)
        self.clock = pg.time.Clock()
        pg.display.set_caption('elastic force')
        pg.display.set_icon(pg.image.load('icon.ico'))

    def run(self):
        isRunning = True
        test = Simulation(10, 100)
        test.AddBody(Vector2(0,0))
        test.objects[0].fixed = True
        test.AddBody(Vector2(130,20))
        test.AddBody(Vector2(180,40))
        test.AddConnection(test.objects[0], test.objects[1])
        test.AddConnection(test.objects[1], test.objects[2])
        while isRunning:
            test.UpdateAndDraw(0.1, self.screen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    isRunning = False
                if event.type == pg.VIDEORESIZE:
                    UpdateScreenSizeInfo(event.w, event.h)
                if event.type == pg.MOUSEBUTTONDOWN:
                    print(test.GetObject(GetMouseWorldPosition()))
            self.clock.tick(60)
        pg.quit()

if __name__ == '__main__':
    try:
        app = App()
        app.run()
    except Exception as e:
        print("Exception:", e)
        input()
        
