from customer import *
import pygame as pg
from drinks import *
from game_config import *
from Game_ui import *

class Draw_manager:

    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Draw_manager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    @classmethod
    def get_instance(cls):
        return cls.__instance

    @staticmethod
    def GetColor(k):
        return Config.game_color[k]

    def __init__(self):
        if not hasattr(self, 'initialized'):
            pg.init()
            self.initialized = True
            self.__screen = pg.display.set_mode((Config.game_width, Config.game_height))
            self.__clock = pg.time.Clock()
            self.__ui = Game_UI()
            self.__cus_alpha = 0
            self.__line_alpha = 0

    def get_screen(self):
        return self.__screen
    
    def reset_cus_alpha(self):
        if self.__cus_alpha >= 0:
            self.__cus_alpha -= 5
        if self.__cus_alpha < 0:
            self.__cus_alpha = 0
        return self.__cus_alpha == 0

    def reset_line_alpha(self):
        self.__line_alpha = 0
        
    def draw(self, state):
        self.__screen.fill(self.GetColor('PP'))
        self.background(state)
        if state == "bar" or state == "talk":
            self.__ui.draw_track()
            self.__ui.draw_money()

    def mixer(self, mixer: Mixer, drink=None):
        self.__ui.draw_mixer(mixer)
        self.__ui.draw_shaker(mixer, drink)

    def background(self, state):
        if state == "bar" or state == "talk":
            pic = pg.image.load("data/Scene/Bar.png").convert()
        
            self.__screen.blit(pic, (0, 0))
        elif state == "end":
            pic = pg.image.load("data/Scene/day_end.png").convert()
            self.__screen.blit(pic, (0, 0))
        elif state == "shop":
            pic = pg.image.load("data/Scene/shop.png").convert()
            self.__screen.blit(pic, (0, 0))
        elif state == "over":
            pic = pg.image.load("data/Scene/over.png").convert()
            self.__screen.blit(pic, (0, 0))

    def draw_end(self,player : PlayerData, rent : int):
        try :
            font = pg.font.Font("data/Font/Architype Aubette W90.otf", 60)
            text_surface = font.render(f"{int(player.day_drinks)}", True, (255, 255, 255))
            text_rect = text_surface.get_rect(right = 1370, centery = 245.95)
            self.__screen.blit(text_surface, text_rect)

            font = pg.font.Font("data/Font/Architype Aubette W90.otf", 60)
            text_surface = font.render(f"{int(player.day_money)}", True, (255, 255, 255))
            text_rect = text_surface.get_rect(right = 1370, centery = 245.95 + 72.7)
            self.__screen.blit(text_surface, text_rect)

            font = pg.font.Font("data/Font/Architype Aubette W90.otf", 60)
            text_surface = font.render(f"{int(player.money_item_bonus())}", True, (255, 255, 255))
            text_rect = text_surface.get_rect(right = 1370, centery = 245.95 + 72.7 * 2)
            self.__screen.blit(text_surface, text_rect)

            font = pg.font.Font("data/Font/Architype Aubette W90.otf", 60)
            text_surface = font.render(f"{int(player.day_mistakes)}", True, (255, 255, 255))
            text_rect = text_surface.get_rect(right = 1370, centery = 573.05)
            self.__screen.blit(text_surface, text_rect)

            font = pg.font.Font("data/Font/Architype Aubette W90.otf", 60)
            text_surface = font.render(f"{int(player.money_day_bonus())}", True, (255, 255, 255))
            text_rect = text_surface.get_rect(right = 1370, centery = 573.05 + 72.7)
            self.__screen.blit(text_surface, text_rect)

            font = pg.font.Font("data/Font/Architype Aubette W90.otf", 60)
            text_surface = font.render(f"{int(rent)}", True, (255, 255, 255))
            text_rect = text_surface.get_rect(right = 1370, centery = 831.55)
            self.__screen.blit(text_surface, text_rect)

            font = pg.font.Font("data/Font/Architype Aubette W90.otf", 60)
            text_surface = font.render(f"{int(player.get_money())}", True, (255, 255, 255))
            text_rect = text_surface.get_rect(right = 1370, centery = 831.55 + 72.7)
            self.__screen.blit(text_surface, text_rect)
        except TypeError:
            print("Error in drawing end screen, player data might be None.")
    
    def draw_over(self, player : PlayerData):
        try :
            font = pg.font.Font("data/Font/Architype Aubette W90.otf", 170)
            text_surface = font.render(f"{int(player.get_day())}", True, (255, 255, 255))
            text_rect = text_surface.get_rect(right = 1786.3, centery = 305.1)
            self.__screen.blit(text_surface, text_rect)

            font = pg.font.Font("data/Font/Architype Aubette W90.otf", 170)
            text_surface = font.render(f"{int(player.get_drinks())}", True, (255, 255, 255))
            text_rect = text_surface.get_rect(right = 1786.3, centery = 305.1 + 194.3)
            self.__screen.blit(text_surface, text_rect)

            font = pg.font.Font("data/Font/Architype Aubette W90.otf", 170)
            text_surface = font.render(f"{int(len(player.get_items()))}", True, (255, 255, 255))
            text_rect = text_surface.get_rect(right = 1786.3, centery = 305.1 + 194.3 * 2)
            self.__screen.blit(text_surface, text_rect)

            font = pg.font.Font("data/Font/Architype Aubette W90.otf", 170)
            text_surface = font.render(f"{int(player.get_mistakes())}", True, (255, 255, 255))
            text_rect = text_surface.get_rect(right = 1786.3, centery = 305.1 + 194.3 * 3)
            self.__screen.blit(text_surface, text_rect)
        except TypeError:
            print("Error in drawing over screen, player data might be None.")
    
    def draw_day(self):
        self.__ui.draw_day()


    def draw_chat(self, text):
        font = pg.font.Font("data/Font/MedodicaRegular.otf", Config.Text_size)
        text = text.split(" ")
        lines = []
        current_line = ""
        for word in text:
            test_line = f"{current_line} {word}".strip()
            text_surface = font.render(test_line, True, (255, 255, 255))
            if text_surface.get_width() > 800 or "\n" in word:
                lines.append(current_line)
                current_line = word.replace("\n", "")  # Remove newline character from the word
            else:
                current_line = test_line
        if current_line:
            lines.append(current_line)

        y_offset = Config.Text_loc[1]
        max_alpha = 255  # Maximum alpha value for smooth transition
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, (255, 255, 255))
            text_width = text_surface.get_width()
            visible_width = min(self.__line_alpha, text_width)
            cropped_surface = pg.Surface((visible_width, text_surface.get_height()), pg.SRCALPHA)
            cropped_surface.blit(text_surface, (0, 0), (0, 0, visible_width, text_surface.get_height()))
            
            # Apply alpha blending for smoother transition
            alpha_surface = pg.Surface(cropped_surface.get_size(), pg.SRCALPHA)
            alpha_surface.fill((255, 255, 255, min(self.__line_alpha, max_alpha)))
            cropped_surface.blit(alpha_surface, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
            
            self.__screen.blit(cropped_surface, (Config.Text_loc[0], y_offset))
            y_offset += text_surface.get_height() + 5  # Add spacing between lines

            if self.__line_alpha < text_width:
                break  # Stop rendering further lines until the current one is fully visible

        if self.__line_alpha < max(font.render(line, True, (255, 255, 255)).get_width() for line in lines):
            pg.display.update()
            self.__line_alpha += 10
    
    def draw_character(self, character, state):
        pic = pg.image.load(f"sprite/customer/{character[0]}").convert_alpha()
        if state in [0,1,2]:
            if self.__cus_alpha < 255:
                pic.set_alpha(self.__cus_alpha)
                self.__screen.blit(pic, character[1])
                pg.display.update()
                self.__cus_alpha += 10
            else:
                pic.set_alpha(255)
                self.__screen.blit(pic, character[1])
        elif state == 4:
            if self.__cus_alpha >= 0:
                pic.set_alpha(self.__cus_alpha)
                self.__screen.blit(pic, character[1])
                pg.display.update()
                self.__cus_alpha -= 10
            else:
                self.__cus_alpha = 0
                pic.set_alpha(0)
                self.__screen.blit(pic, character[1])

    def draw_time(self, time):
        self.__ui.draw_timer(time)

    def draw_customer(self, customer : Customer):
        if customer.sprite:
            self.draw_character(customer.sprite, customer.state)
        if customer.line:
            self.draw_chat(customer.line)

    def UpdateAll(self, state):
        self.draw(state)
        
        self.__clock.tick(Config.fps)

