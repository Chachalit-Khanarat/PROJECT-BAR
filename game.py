from drawer import *

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