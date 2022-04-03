import pygame as pg

class App:
    def __init__(self):
        self.screen = pg.display.set_mode((330, 330))
        self.clock = pg.time.Clock()
        pg.display.set_caption('elastic force')

    def run(self):
        isRunning = True
        while isRunning:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    isRunning = False
            self.clock.tick(60)
        pg.quit()

if __name__ == '__main__':
    app = App()
    app.run()
