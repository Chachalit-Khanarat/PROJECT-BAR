from customer import *
import pygame as pg
import random
from drinks import *
from game_config import *
from drawer import *
from sound import *

class Game:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Game, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, mode="endless"):
        self.__draw = Draw_manager()
        self.__mixer = Mixer()
        self.__drinks = Drinks()
        self.__sound = SoundManager()

        self.__mode = mode
        self.__state = "bar"

        self.__drink = None
        self.__customer = None
        self._initialized = True

    @classmethod
    def get_instance(cls):
        return cls.__instance

    def get_state(self):
        return self.__state

    def gameupdate(self):
        self.__draw.UpdateAll(self.__state)
        self.__draw.mixer(self.__mixer, self.__drink)

        if self.__customer is None:
            self.__customer = random.choice([male_npc, female_npc])
            self.__customer = self.__customer()
            print(self.__customer)

        self.__draw.draw_customer(self.__customer)

    def drink_update(self):
        if self.__mixer.state == 0:
            self.__mixer.shake()
        elif self.__mixer.state == 1 or self.__mixer.state == 2:
            self.__mixer.shake()
            self.__drink = self.__drinks.get_drink(self.__mixer)
        elif self.__mixer.state == 3:
            print(self.__drink, self.__mixer.A, self.__mixer.B, self.__mixer.D, self.__mixer.F, self.__mixer.K)
            self.__mixer.reset_mixer()
            self.__customer.give_drink(self.__drink)

    def run(self):
        print("RUN")
        running = True
        self.__sound.play_music()
        while running:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    running = False
                if ev.type == pg.KEYDOWN:
                    if game.__state == 'bar':
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
                        if ev.key == pg.K_RCTRL:
                            self.__mixer.reset_mixer()
                            self.__drink = None
                    if game.__state == 'talk':
                        if ev.key == pg.K_SPACE:
                            self.__customer.get_order()
                            self.__state = "bar"
                            self.__draw.reset_alpha()
                            self.__customer = None
                            self.__drink = None
                    if ev.key == pg.K_RIGHT:
                        self.__sound.next_music()
                    if ev.key == pg.K_LEFT:
                        self.__sound.prev_music()
                    if ev.key == pg.K_DOWN:
                        self.__sound.pause_music()
                    if ev.key == pg.K_UP:
                        self.__sound.continue_music()

            self.gameupdate()
            pg.display.flip()

        pg.quit()
        print("Exit")

    def __repr__(self):
        return f"Game State: {self.__state}, Mode: {self.__mode}"

if __name__ == "__main__":
    game = Game()
    game.run()