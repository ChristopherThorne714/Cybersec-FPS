import pygame as pg
import settings
import main

global paused
paused = False
FONT = pg.font.SysFont("arialblack", 24)
gametitle = FONT.render("Cybersecurity FPS", 1, (255, 255, 255))
pausetext = FONT.render("Press C to continue or Q to quit", 1, (255, 255, 255))
def pause():
    paused = True
    print("Paused")
    while paused:
        clock = pg.time.Clock()
        screen = pg.display.set_mode(settings.RES)
        screen.blit(gametitle, (settings.HALF_HEIGHT + 150, settings.THIRD_WIDTH - 500))
        screen.blit(pausetext, (settings.HALF_HEIGHT, settings.HALF_WIDTH))
        pg.display.flip()
        clock.tick(5)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_c or event.key == pg.K_ESCAPE):
                    print("Continue")
                    paused = False
                    break
                elif event.key == pg.K_q:
                    pg.quit()
                    quit()
