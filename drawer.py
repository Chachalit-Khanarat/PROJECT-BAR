import pygame as pg
import random
from game_config import *


class Game_UI:
    def __init__(self):
        self.__screen = pg.display.set_mode((Config.game_width,Config.game_height))
    
    def draw_ui(self):
        tmp = pg.Surface(Config.panel_size, pg.SRCALPHA)
        rect1 = pg.Rect(Config.game_width//4,Config.game_height//4,Config.game_width//2,Config.game_height//2)
        tmp.fill(Drawer.GetColor("B"),rect1)

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
    
    def draw(self):
        self.__ui.draw_ui()

    def UpdateAll(self):
        self.draw()
        self.__clock.tick(Config.fps)
        pg.display.flip()




