import pygame as pg
import random
import threading

from customer import *
from drinks import *
from game_config import *
from drawer import *
from sound import *
from data_manager import *
from shop_ui import *
from menus import *

class Game:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Game, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, mode="endless"):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.__data = DataManager()
            self.__draw = Draw_manager()
            self.__mixer = Mixer()
            self.__drinks = Drinks()
            self.__sound = SoundManager()
            self.__player = PlayerData()

            self.__mode = mode
            self.__state = "talk"
            self.start_ticks = pg.time.get_ticks()
            self.timer = 1000 * 60 * 2

            self.rent = 150

            self.__shop = None
            self.__drink = None
            self.__customer = None

    @classmethod
    def get_instance(cls):
        return cls.__instance

    def get_state(self):
        return self.__state

    def get_sound(self):
        return self.__sound
    
    def new_rent(self):
        self.rent = self.rent * 1.75 
        # print(f"New Rent: {self.rent}")
    
    def game_reset(self):
        self.__state = "talk"
        self.start_ticks = pg.time.get_ticks()
        self.__drink = None
        self.__customer = None
        self.__mixer.reset_mixer()
        self.__draw.reset_cus_alpha()
        self.__draw.reset_line_alpha()
        self.__player.reset_day()

    def gameupdate(self):
        try :
            self.__draw.UpdateAll(self.__state)
        except pg.error:
            print("Error loading image.")
        if self.__state == "bar" or self.__state == "talk":
            self.__draw.mixer(self.__mixer, self.__drink)
            self.__draw.draw_day()

            if self.__customer is not None:
                self.__draw.draw_time(self.get_time_left())
                try :
                    self.__draw.draw_customer(self.__customer)
                except pg.error:
                    print("Error loading customer image.")
                # print(self.__state, self.__customer.state)
                if (pg.time.get_ticks() - self.start_ticks) >= self.timer:
                    self.day_end()
                    self.start_ticks = pg.time.get_ticks()
            else:
                self.__draw.draw_chat("Welcome to the HelHelm! \nPress SPACE to open the Bar.")

            if not pg.mixer_music.get_busy() and self.__sound.get_state():
                self.__sound.next_music()
            
            elif self.__customer is None:
                self.__draw.draw_time(self.timer)
                self.start_ticks = pg.time.get_ticks()
            
        elif self.__state == "end":
            pg.mixer_music.stop()
            try :
                self.__draw.draw_end(self.__player, self.rent)
            except pg.error:
                print("Error loading end image.")
        
        elif self.__state == "over":
            try :
                self.__draw.draw_over(self.__player)
            except pg.error:
                print("Error loading over image.")

    def get_time_left(self):
        return self.timer - (pg.time.get_ticks() - self.start_ticks)

    def day_end(self):
        self.__player.day_end(self.rent)
        pg.mixer_music.stop()
        self.__state = "end"
        print(self.__player)

    def customer_update(self):
            if self.__customer is not None:
                self.__customer.state += 1
            
            if self.__customer is not None and self.__customer.state == 2:
                self.__draw.reset_line_alpha()

            if self.__customer is not None and self.__customer.state == 3:
                self.__customer = None

            if self.__customer is None:
                self.__draw.reset_line_alpha()
                self.__customer = Customer.get_customer()
                try :
                    self.__customer = self.__customer()
                    # print(self.__customer)
                except TypeError:
                    self.__customer = Customer.get_customer()
                    self.__customer = self.__customer()

            if self.__customer.state == 1:
                self.__state = "bar"

    def drink_update(self):
        if self.__mixer.state == 0:
            self.__mixer.shake()
        elif self.__mixer.state == 1 or self.__mixer.state == 2:
            self.__mixer.shake()
            self.__drink = self.__drinks.get_drink(self.__mixer)
        elif self.__mixer.state == 3:
            if self.__drink == "bad":
                self.__mixer.reset_mixer()
                return
            # print(self.__drink, self.__mixer.A, self.__mixer.B, self.__mixer.D, self.__mixer.F, self.__mixer.K)
            if not self.__customer.give_drink(self.__drink):
                self.__player.add_day_mistakes()
            else :
                self.__player.add_day_money(self.__drinks.get_price(self.__drink))

            self.__data.add_cus_data(self.__customer)
            self.__customer.state += 1
            self.__player.add_day_drinks()
            self.__player.add_day_customers()
            self.__mixer.reset_mixer()
            self.__state = "talk"

    def run(self):
        print("RUN")
        running = True
        self.__sound.play_music()
        self.__state = "talk"
        while running:
            for ev in pg.event.get():

                if ev.type == pg.QUIT:
                    running = False

                if self.__state == 'shopping':
                    self.__state = "talk"
                    self.__shop = ShopGUI()
                    self.__shop.mainloop()
                    self.game_reset()

                if ev.type == pg.KEYDOWN:
                    if self.__state == 'bar':
                        if ev.key == pg.K_q:
                            self.__mixer.add_A()
                        if ev.key == pg.K_w:
                            self.__mixer.add_B()
                        if ev.key == pg.K_e:
                            self.__mixer.add_D()
                        if ev.key == pg.K_r:
                            self.__mixer.add_F()
                        if ev.key == pg.K_t:
                            self.__mixer.add_K()
                        if ev.key == pg.K_a:
                            self.__mixer.set_rock()
                        if ev.key == pg.K_s:
                            self.__mixer.set_ages()
                        if ev.key == pg.K_SPACE:
                            self.drink_update()
                        if ev.key == pg.K_LCTRL:
                            self.__mixer.reset_mixer()
                            self.__drink = None

                    elif self.__state == 'talk':
                        if ev.key == pg.K_SPACE:
                            self.customer_update()

                    elif self.__state == 'end':
                        
                        self.new_rent()
                        if ev.key == pg.K_SPACE:
                            if self.__player.check_over():
                                self.__state = "over"
                            else :
                                self.__state = "shop"
                    
                    elif self.__state == 'shop':
                        if ev.key == pg.K_SPACE:
                            self.__state = "shopping"

                    elif self.__state == 'over':
                        if ev.key == pg.K_SPACE:
                            running = False

                    if ev.key == pg.K_RIGHT:
                        self.__sound.next_music()
                    if ev.key == pg.K_LEFT:
                        self.__sound.prev_music()
                    if ev.key == pg.K_DOWN:
                        self.__sound.music_ctrl()
                            

            self.gameupdate()
            pg.display.flip()
    
        self.__data.save_data()
        pg.quit()
        print("Exit")

    def __repr__(self):
        return f"Game State: {self.__state}, Mode: {self.__mode}"

if __name__ == "__main__":
    pg.init()
    game = Game()
    game.run()