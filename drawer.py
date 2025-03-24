import pygame as pg
import random
from game_config import *


class Game_UI:
    def draw_ui(self, screen):
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
        rect1 = pg.Rect(Config.game_width//100,Config.game_height//100,int(Config.game_width*49/50),int(Config.game_height*49/50))
        pg.draw.rect(self.__screen,Drawer.GetColor("LPP"),rect1)
    
    def draw(self):
        tmp = pg.Surface((Config.panel_size))
        self.__screen.fill(self.GetColor('PP'))
        self.background()
        self.__ui.draw_ui(self.__screen)

    def UpdateAll(self):
        self.draw()
        self.__clock.tick(Config.fps)
        pg.display.flip()

class Game:
    def __init__(self):
        self.__draw = Drawer()

    def gameupdate(self):
        pass

    def run(self):
        print("RUN")
        running= True
        while (running):
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    running == False
                if ev.type == pg.KEYDOWN:
                    if game.__state == 'playing':     
                        if ev.key == pg.K_q:
                            self.__piece.move_current(-1,0)
                        if ev.key == pg.K_w:
                            self.__piece.move_current(1,0)
                        if ev.key == pg.K_e:
                            self.__piece.rotate_current()
                        if ev.key == pg.K_r:
                            self.__piece.falling()
                        if ev.key == pg.K_t:
                            self.__piece.force_falling()
                        if ev.key == pg.K_a:
                            self.__piece.move_current(-1,0)
                        if ev.key == pg.K_s:
                            self.__piece.move_current(1,0)
                        if ev.key == pg.K_SPACE:
                            self.__game_reset()

            self.gameupdate()
            self.__draw.UpdateAll()
        pg.quit()
        print("Exit Run")

if __name__ == "__main__":
    game = Game()
    game.run()



