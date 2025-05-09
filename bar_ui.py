from drinks import *
from game_config import *
from game import *
import pygame as pg
import time
import math

class Game_UI:
    def __init__(self):
        self.shaker_frame = 0

    def draw_shaker(self, mixer: Mixer, screen, drink = None):
        pic = pg.image.load("data/Shaker.png").convert_alpha()

        original_pos = (1314.6, 486.6)

        if mixer.state == 0:
            screen.blit(pic, original_pos)
            

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
            screen.blit(rotated_pic, rotated_rect)

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
            screen.blit(rotated_pic, rotated_rect)

        elif mixer.state == 3:
            if drink:
                pic = pg.image.load(f"sprite/drink_img/{drink}.png").convert_alpha()
                screen.blit(pic, (1302.7,486.6))
                font = pg.font.Font("data/Font/norwester.otf", 35)
                drink = drink.replace("_", " ").title()
                text = font.render(drink, True, (255, 255, 255))
                text_rect = text.get_rect(center=(1302.7 + pic.get_width() / 2, 486.6 + pic.get_height() / 2), y = 669.5)
                screen.blit(text, text_rect)

    
    def draw_customer(self, customer, screen):
        if customer.sprite:
            pic = pg.image.load(f"data/{customer.sprite[0]}").convert_alpha()
            screen.blit(pic, customer.sprite[1])
            font = pg.font.Font(None, 30)
            text = font.render(customer.line, True, (255, 255, 255))
            screen.blit(text, (customer.sprite[1][0], customer.sprite[1][1] - 20))

    def draw_mixer(self, mixer : Mixer, screen):

        loc1, loc2 = Config.counter_loc["A"]
        for i in range(mixer.A):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(33.5*(i % 5)),loc1[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc1[0]+(33.5*(i % 5)) + 5,loc1[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(33.5*(i % 5)),loc2[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc2[0]+(33.5*(i % 5)) + 5,loc2[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)
            
            pg.draw.rect(screen,(171, 13, 15),rect_1)
            if i < 10 :
                pg.draw.rect(screen,(64, 0, 0),rect_b)

        loc1, loc2 = Config.counter_loc["B"]
        for i in range(mixer.B):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(33.5*(i % 5)),loc1[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc1[0]+(33.5*(i % 5)) + 5,loc1[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(33.5*(i % 5)),loc2[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc2[0]+(33.5*(i % 5)) + 5,loc2[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)
            
            pg.draw.rect(screen,(249, 199, 81),rect_1)
            if i < 10 :
                pg.draw.rect(screen,(64, 0, 0),rect_b)

        loc1, loc2 = Config.counter_loc["D"]
        for i in range(mixer.D):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(33.5*(i % 5)),loc1[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc1[0]+(33.5*(i % 5)) + 5,loc1[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(33.5*(i % 5)),loc2[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc2[0]+(33.5*(i % 5)) + 5,loc2[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)
            
            pg.draw.rect(screen,(126, 150, 219),rect_1)
            if i < 10 :
                pg.draw.rect(screen,(64, 0, 0),rect_b)
        
        loc1, loc2 = Config.counter_loc["F"]
        for i in range(mixer.F):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(33.5*(i % 5)),loc1[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc1[0]+(33.5*(i % 5)) + 5,loc1[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(33.5*(i % 5)),loc2[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc2[0]+(33.5*(i % 5)) + 5,loc2[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)
            
            pg.draw.rect(screen,(140, 174, 94),rect_1)
            if i < 10 :
                pg.draw.rect(screen,(64, 0, 0),rect_b)

        loc1, loc2 = Config.counter_loc["K"]
        for i in range(mixer.K):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(33.5*(i % 5)),loc1[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc1[0]+(33.5*(i % 5)) + 5,loc1[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(33.5*(i % 5)),loc2[1], Config.counter_size[0], Config.counter_size[1])
                rect_b = pg.Rect(loc2[0]+(33.5*(i % 5)) + 5,loc2[1] + 5, Config.counter_size[0] - 10, Config.counter_size[1] - 10)
            
            pg.draw.rect(screen,(208, 231, 230),rect_1)
            if i < 10 :
                pg.draw.rect(screen,(64, 0, 0),rect_b)

        loc1, loc2 = Config.counter_loc["shaker"]
        for i in range(mixer.in_mixer()):
            if i < 5 or 10 <= i < 15:
                rect_1 = pg.Rect(loc1[0]+(50.6*(i % 5)),loc1[1], Config.shaker_size[0], Config.shaker_size[1])
                rect_b = pg.Rect(loc1[0]+(50.6*(i % 5)) + 5,loc1[1] + 5, Config.shaker_size[0] - 10, Config.shaker_size[1] - 10)

            elif i < 10 or 15 <= i < 20 :
                rect_1 = pg.Rect(loc2[0]+(50.6*(i % 5)),loc2[1], Config.shaker_size[0], Config.shaker_size[1])
                rect_b = pg.Rect(loc2[0]+(50.6*(i % 5)) + 5,loc2[1] + 5, Config.shaker_size[0] - 10, Config.shaker_size[1] - 10)
            
            pg.draw.rect(screen,(208, 231, 230),rect_1)
            if i < 10 :
                pg.draw.rect(screen,(64, 0, 0),rect_b)
        
        loc = Config.aged_rocks_loc["Aged"]
        if mixer.Aged:
            rect_1 = pg.Rect(loc[0],loc[1], Config.aged_rocks_size[0], Config.aged_rocks_size[1])
            rect_b = pg.Rect(loc[0] + 5,loc[1] + 5, Config.aged_rocks_size[0] - 10, Config.aged_rocks_size[1] - 10)
            pg.draw.rect(screen,(155, 33, 229),rect_1)
            pg.draw.rect(screen,(64, 0, 0),rect_b)

        loc = Config.aged_rocks_loc["Rocks"]
        if mixer.Rock:
            rect_1 = pg.Rect(loc[0],loc[1], Config.aged_rocks_size[0], Config.aged_rocks_size[1])
            rect_b = pg.Rect(loc[0] + 5,loc[1] + 5, Config.aged_rocks_size[0] - 10, Config.aged_rocks_size[1] - 10)
            pg.draw.rect(screen,(122, 247, 255),rect_1)
            pg.draw.rect(screen,(64, 0, 0),rect_b)
