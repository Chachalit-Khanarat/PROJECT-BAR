from drinks import *
from game_config import *
from game import *
import pygame as pg
import time
import math

from game import *
from sound import *

class Game_UI:
    def __init__(self):
        from drawer import Draw_manager
        self.__screen = Draw_manager().get_screen()
        self.shaker_frame = 0

    def draw_shaker(self, mixer: Mixer, drink = None):
        try:
            pic = pg.image.load("data/Shaker.png").convert_alpha()

            original_pos = (1314.6, 486.6)

            if mixer.state == 0:
                self.__screen.blit(pic, original_pos)
                

            elif mixer.state == 1:
                max_angle = 20
                angle = math.sin(self.shaker_frame * 0.2) * max_angle
                self.shaker_frame += 1

                rotated_pic = pg.transform.rotate(pic, angle)

                image_center = (
                    original_pos[0] + pic.get_width() / 2,
                    original_pos[1] + pic.get_height() / 2
                )
                rotated_rect = rotated_pic.get_rect(center=image_center)
                self.__screen.blit(rotated_pic, rotated_rect)

                if time.time() - mixer.shake_time > 5:
                    mixer.state = 2
            
            elif mixer.state == 2:
                max_angle = 20
                angle = math.sin(self.shaker_frame * 0.5) * max_angle
                self.shaker_frame += 1

                rotated_pic = pg.transform.rotate(pic, angle)

                image_center = (
                    original_pos[0] + pic.get_width() / 2,
                    original_pos[1] + pic.get_height() / 2
                )
                rotated_rect = rotated_pic.get_rect(center=image_center)
                self.__screen.blit(rotated_pic, rotated_rect)

            elif mixer.state == 3:
                    if drink:
                        pic = pg.image.load(f"sprite/drink_img/{drink.replace('Big ', '')}.png").convert_alpha()
                        self.__screen.blit(pic, (1302.7,486.6))
                        font = pg.font.Font("data/Font/norwester.otf", 35)
                        drink = drink.replace("_", " ").title()
                        text = font.render(drink, True, (255, 255, 255))
                        text_rect = text.get_rect(center=(1302.7 + pic.get_width() / 2, 486.6 + pic.get_height() / 2), y = 669.5)
                        self.__screen.blit(text, text_rect)
        except pg.error:
            print("Error loading shaker image.")

    def draw_timer(self, time):
        font = pg.font.Font("data/Font/MedodicaRegular.otf", 120)
        time = time / 1000
        minutes = int(time // 60)
        seconds = int(time % 60)
        text = f"{minutes:02d}:{seconds:02d}"
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(centerx=1715.85, centery=759.55)  # Adjust 'right' to align text to the right
        self.__screen.blit(text_surface, text_rect)

    def draw_money(self):
        font = pg.font.Font("data/Font/MedodicaRegular.otf", 60)
        text = f"{int(PlayerData().get_money())}"
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(x = 1015.5, centery = 1003.4)
        self.__screen.blit(text_surface, text_rect)
    
    def draw_track(self):
        music = SoundManager()
        font = pg.font.Font("data/Font/MedodicaRegular.otf", 30)
        text = music.get_music_name()
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(x = 989.2,y = 889.4)
        self.__screen.blit(text_surface, text_rect)
        ctime, ftime = music.get_music_time()
        minutes = int(ctime // 60)
        seconds = int(ctime % 60)
        fseconds = int(ftime) % 60
        fminutes = int(ftime // 60)
        text = f"{minutes:02d}:{seconds:02d}/{int(fminutes):02d}:{fseconds:02d}"
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(right=1598, y=889.4)  # Adjust 'right' to align text to the right
        self.__screen.blit(text_surface, text_rect)

        progress = pg.Rect(989.2, 924.6, 608.7 * music.get_current_music_percent(), 5)
        pg.draw.rect(self.__screen, (140, 82, 255), progress)
    
    def draw_day(self):
        font = pg.font.Font("data/Font/MedodicaRegular.otf", 90)
        text = f"DAY  {int(PlayerData().get_day())}"
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(centerx = 1751.9, centery = 956.7)
        self.__screen.blit(text_surface, text_rect)

        
    def draw_mixer(self, mixer : Mixer):

        loc1, loc2 = Config.counter_loc["A"]
        for i in range(mixer.A):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(33.5*(i % 5)),loc1[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc1[0]+(33.5*(i % 5)) + 5,loc1[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(33.5*(i % 5)),loc2[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc2[0]+(33.5*(i % 5)) + 5,loc2[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)
            
            pg.draw.rect(self.__screen,(171, 13, 15),rect_1)
            if i < 10 :
                pg.draw.rect(self.__screen,(64, 0, 0),rect_b)

        loc1, loc2 = Config.counter_loc["B"]
        for i in range(mixer.B):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(33.5*(i % 5)),loc1[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc1[0]+(33.5*(i % 5)) + 5,loc1[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(33.5*(i % 5)),loc2[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc2[0]+(33.5*(i % 5)) + 5,loc2[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)
            
            pg.draw.rect(self.__screen,(249, 199, 81),rect_1)
            if i < 10 :
                pg.draw.rect(self.__screen,(64, 0, 0),rect_b)

        loc1, loc2 = Config.counter_loc["D"]
        for i in range(mixer.D):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(33.5*(i % 5)),loc1[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc1[0]+(33.5*(i % 5)) + 5,loc1[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(33.5*(i % 5)),loc2[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc2[0]+(33.5*(i % 5)) + 5,loc2[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)
            
            pg.draw.rect(self.__screen,(126, 150, 219),rect_1)
            if i < 10 :
                pg.draw.rect(self.__screen,(64, 0, 0),rect_b)
        
        loc1, loc2 = Config.counter_loc["F"]
        for i in range(mixer.F):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(33.5*(i % 5)),loc1[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc1[0]+(33.5*(i % 5)) + 5,loc1[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(33.5*(i % 5)),loc2[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc2[0]+(33.5*(i % 5)) + 5,loc2[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)
            
            pg.draw.rect(self.__screen,(140, 174, 94),rect_1)
            if i < 10 :
                pg.draw.rect(self.__screen,(64, 0, 0),rect_b)

        loc1, loc2 = Config.counter_loc["K"]
        for i in range(mixer.K):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(33.5*(i % 5)),loc1[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc1[0]+(33.5*(i % 5)) + 5,loc1[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(33.5*(i % 5)),loc2[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc2[0]+(33.5*(i % 5)) + 5,loc2[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)
            
            pg.draw.rect(self.__screen,(208, 231, 230),rect_1)
            if i < 10 :
                pg.draw.rect(self.__screen,(64, 0, 0),rect_b)

        loc1, loc2 = Config.counter_loc["shaker"]
        for i in range(mixer.in_mixer()):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(50.6*(i % 5)),loc1[1], Config.shaker_size[0], Config.shaker_size[1])
                rect_b = pg.Rect(loc1[0]+(50.6*(i % 5)) + 5,loc1[1] + 5, Config.shaker_size[0] - 10, Config.shaker_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(50.6*(i % 5)),loc2[1], Config.shaker_size[0], Config.shaker_size[1])
                rect_b = pg.Rect(loc2[0]+(50.6*(i % 5)) + 5,loc2[1] + 5, Config.shaker_size[0] - 10, Config.shaker_size[1] - 10)
            
            pg.draw.rect(self.__screen,(208, 231, 230),rect_1)
            if i < 10 :
                pg.draw.rect(self.__screen,(64, 0, 0),rect_b)
        
        loc = Config.aged_rocks_loc["Aged"]
        if mixer.Aged:
            rect_1 = pg.Rect(loc[0],loc[1], Config.aged_rocks_size[0], Config.aged_rocks_size[1])
            rect_b = pg.Rect(loc[0] + 5,loc[1] + 5, Config.aged_rocks_size[0] - 10, Config.aged_rocks_size[1] - 10)
            pg.draw.rect(self.__screen,(155, 33, 229),rect_1)
            pg.draw.rect(self.__screen,(64, 0, 0),rect_b)

        loc = Config.aged_rocks_loc["Rocks"]
        if mixer.Rock:
            rect_1 = pg.Rect(loc[0],loc[1], Config.aged_rocks_size[0], Config.aged_rocks_size[1])
            rect_b = pg.Rect(loc[0] + 5,loc[1] + 5, Config.aged_rocks_size[0] - 10, Config.aged_rocks_size[1] - 10)
            pg.draw.rect(self.__screen,(122, 247, 255),rect_1)
            pg.draw.rect(self.__screen,(64, 0, 0),rect_b)
