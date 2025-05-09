from customer import *
import pygame as pg
from drinks import *
from game_config import *
from bar_ui import Game_UI

class Draw_manager:

    @staticmethod
    def GetColor(k):
        return Config.game_color[k]

    def __init__(self):
        pg.init()
        self.__screen = pg.display.set_mode((Config.game_width, Config.game_height))
        self.__clock = pg.time.Clock()
        self.__ui = Game_UI()
        self.__cus_alpha = 0
        self.__line_alpha = 0
    
    @classmethod
    def reset_alpha(cls):
        # cls.__cus_alpha = 0
        cls.__line_alpha = 0

    def mixer(self, mixer: Mixer, drink=None):
        self.__ui.draw_mixer(mixer, self.__screen)
        self.__ui.draw_shaker(mixer, self.__screen, drink)

    def background(self, state):
        if state == "bar":
            pic = pg.image.load("data/Bartending.png").convert()
        self.__screen.blit(pic, (0, 0))

    def draw(self, state):
        self.__screen.fill(self.GetColor('PP'))
        self.background(state)

    def draw_customer(self, customer : Customer):
        if customer.sprite:
            pic = pg.image.load(f"sprite/customer/{customer.sprite[0]}").convert_alpha()
            if self.__cus_alpha < 255:
                pic.set_alpha(self.__cus_alpha)
                self.__screen.blit(pic, customer.sprite[1])
                pg.display.update()
                self.__cus_alpha += 5
            else:
                pic.set_alpha(255)
                self.__screen.blit(pic, customer.sprite[1])

        if customer.line:
            font = pg.font.Font("data/Font/MedodicaRegular.otf", Config.Text_size)
            words = customer.line.split(' ')
            lines = []
            current_line = ""
            for word in words:
                test_line = f"{current_line} {word}".strip()
                text_surface = font.render(test_line, True, (255, 255, 255))
                if text_surface.get_width() > 949.4:
                    lines.append(current_line)
                    current_line = word
                else:
                    current_line = test_line
            if current_line:
                lines.append(current_line)

            y_offset = Config.Text_loc[1]
            for line in lines:
                text_surface = font.render(line, True, (255, 255, 255))
                text_width = text_surface.get_width()
                visible_width = min(self.__line_alpha, text_width)
                cropped_surface = pg.Surface((visible_width, text_surface.get_height()), pg.SRCALPHA)
                cropped_surface.blit(text_surface, (0, 0), (0, 0, visible_width, text_surface.get_height()))
                self.__screen.blit(cropped_surface, (Config.Text_loc[0], y_offset))
                y_offset += text_surface.get_height() + 5  # Add spacing between lines

            if self.__line_alpha < max(font.render(line, True, (255, 255, 255)).get_width() for line in lines):
                pg.display.update()
                self.__line_alpha += 5

    def UpdateAll(self, state):
        self.draw(state)
        self.__clock.tick(Config.fps)

