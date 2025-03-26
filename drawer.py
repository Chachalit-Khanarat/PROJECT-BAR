import pygame as pg
import random
from game_config import *


class Game_UI:
    def draw_ui(self):
        tmp = pg.Surface(Config.panel_size, pg.SRCALPHA)
         

class Drawer:

    @staticmethod
    def curr_time():
        return pg.time.get_ticks()

    @staticmethod
    def GetColor(k):
        return Config.game_color[k]

    def __init__(self):
        pg.init()
        self.__screen = pg.display.set_mode((Config.game_width,Config.game_height))
        self.__clock = pg.time.Clock()
        self.__game_info = None
        self.__ui = Game_UI()

    def background(self):
        pic = pg.image.load("data/Project Bar.png").convert()
        self.__screen.blit(pic,(0,0))
    
    def draw(self):
        tmp = pg.Surface((Config.panel_size))
        self.__screen.fill(self.GetColor('PP'))
        self.background()
        self.__ui.draw_ui()

    def UpdateAll(self):
        self.draw()
        self.__clock.tick(Config.fps)
        pg.display.flip()

class Game:
    def __init__(self):
        self.__draw = Drawer()
        self.__state = "playing"

    def gameupdate(self):
        pass

    def run(self):
        print("RUN")
        running= True
        while (running):
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    running == False

            self.gameupdate()
            self.__draw.UpdateAll()
        pg.quit()
        print("Exit Run")

if __name__ == "__main__":
    game = Game()
    game.run()



