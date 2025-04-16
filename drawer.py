import pygame as pg
import random
from game_config import *
from drinks import *
from bar_ui import *


class Draw_manager:

    @staticmethod
    def GetColor(k):
        return Config.game_color[k]

    def __init__(self):
        pg.init()
        self.__screen = pg.display.set_mode((Config.game_width,Config.game_height))
        self.__clock = pg.time.Clock()
        self.__ui = Game_UI()

    def mixer(self, mixer : Mixer, drink = None):
        self.__ui.draw_mixer(mixer, self.__screen)
        self.__ui.draw_shaker(mixer, self.__screen, drink)

    def background(self, state):
        if state == "bar":
            pic = pg.image.load("data/Bartending.png").convert()
        self.__screen.blit(pic,(0,0))
    
    def draw(self, state):
        self.__screen.fill(self.GetColor('PP'))
        self.background(state)

    def UpdateAll(self,state):
        self.draw(state)
        self.__clock.tick(Config.fps)



