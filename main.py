from Application import *

def Main():
    app = Application()
    app.Start()
    screen = pg.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT), pg.RESIZABLE)
    clock = pg.time.Clock()
    pg.display.set_caption('elastic force')
    try:
        pg.display.set_icon(pg.image.load('icon.ico'))
    except:
        print("Icon not found.")
    isRunning = True
    while isRunning:
        app.Update()
        app.Draw(screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                isRunning = False
            elif event.type == pg.VIDEORESIZE:
                UpdateScreenSizeInfo(event.w, event.h)
            else:
                app.HandleEvent(event)
        clock.tick(FPS)
    pg.quit()

if __name__ == '__main__':
    try:
        Main()
    except Exception as e:
        print("Exception:", e)
        input()
        
