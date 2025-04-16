from drawer import *

class Game:
    def __init__(self):
        self.__draw = Draw_manager()
        self.__state = "bar"
        self.__mixer = Mixer()
        self.__drinks = Drinks()
        self.__drink = None

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
                            if self.__mixer.state == 0:
                                self.__mixer.shake()
                            elif self.__mixer.state == 1 or self.__mixer.state == 2:
                                self.__mixer.shake()
                                self.__drink = self.__drinks.get_drink(self.__mixer)
                                print(self.__mixer.A, self.__mixer.B, self.__mixer.D, self.__mixer.F, self.__mixer.K, self.__mixer.Rock, self.__mixer.Aged, self.__mixer.mix_type, self.__drink)
                            elif self.__mixer.state == 3:
                                self.__mixer.reset_mixer()

            self.gameupdate()
            self.__draw.UpdateAll(self.__state)
            self.__draw.mixer(self.__mixer, self.__drink)
            pg.display.flip()
        pg.quit()
        print("Exit Run")

if __name__ == "__main__":
    game = Game()
    game.run()