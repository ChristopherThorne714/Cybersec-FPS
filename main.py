import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from pause import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        FONT = pg.font.SysFont("arialblack", 24)

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = Raycasting(self)
        self.object_handler = ObjectHandler(self)
        #self.static_sprite = SpriteObject(self)
        #self.animated_sprite = AnimatedSprite(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        #self.static_sprite.update()
        #self.animated_sprite.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        #self.screen.fill('black')
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()

#The following function will handle the "paused" game state.
    def check_events(self):
        paused = False
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pause()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            paused = False
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
