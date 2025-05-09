import pandas as pd
import time

class Mixer :
    def __init__(self):
        self.A = 0
        self.B = 0
        self.D = 0
        self.F = 0
        self.K = 0
        self.Rock = False
        self.Aged = False
        self.shake_time = 0
        self.mix_type = None
        self.state = 0

    def reset_mixer(self):
        self.A = 0
        self.B = 0
        self.D = 0
        self.F = 0
        self.K = 0
        self.Rock = False
        self.Aged = False
        self.shake_time = 0
        self.mix_type = None
        self.state = 0

    def in_mixer(self):
        return self.A + self.B + self.D + self.F + self.K
    
    def add_A(self):
        if self.in_mixer() >= 20:
            return False
        self.A += 1
        return True
    
    def add_B(self):
        if self.in_mixer() >= 20:
            return False
        self.B += 1
        return True
    
    def add_D(self):
        if self.in_mixer() >= 20:
            return False
        self.D += 1
        return True
    
    def add_F(self):
        if self.in_mixer() >= 20:
            return False
        self.F += 1
        return True
    
    def add_K(self):
        if self.in_mixer() >= 20:
            return False
        self.K += 1
        return True
    
    def set_rock(self):
        if self.Rock:
            self.Rock = False
        elif not self.Rock:
            self.Rock = True

    def set_ages(self):
        if self.Aged:
            self.Aged = False
        elif not self.Aged:
            self.Aged = True

    def shake(self):
        if self.shake_time == 0:
            self.state = 1
            self.shake_time = time.time()
        else :
            time_shaken = time.time() - self.shake_time
            if time_shaken < 5:
                self.mix_type = "mixed"
            elif time_shaken > 5:
                self.mix_type = "blended"
            self.shake_time = 0
            self.state = 3


class Drinks:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Drinks, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.drinks = pd.read_csv("data\menus.csv")
        self.drinks = self.drinks.set_index(self.drinks["Drinks"])
    
    def get_price(self, drink):
        return self.drinks["Price"][drink]
    
    def get_drink(self, mixer : Mixer):
        filtered = self.drinks[((self.drinks["A"] == mixer.A))
                           & (self.drinks["B"] == mixer.B)
                           & (self.drinks["D"] == mixer.D)
                           & (self.drinks["F"] == mixer.F)
                           & ((self.drinks["K"] == mixer.K) | (self.drinks["K"] == -1))
                           & (self.drinks["Rocks"] == mixer.Rock)
                           & (self.drinks["Aged"] == mixer.Aged)
                           & (self.drinks["Mix_or_Blend"] == mixer.mix_type)]

        if len(filtered) == 1:
            return filtered["Drinks"].item()

        filtered2 = self.drinks[((self.drinks["A"] == mixer.A//2))
                           & (self.drinks["B"] == mixer.B//2)
                           & (self.drinks["D"] == mixer.D//2)
                           & (self.drinks["F"] == mixer.F//2)
                           & ((self.drinks["K"] == mixer.K//2) | (self.drinks["K"] == -1))
                           & (self.drinks["Rocks"] == mixer.Rock)
                           & (self.drinks["Aged"] == mixer.Aged)
                           & (self.drinks["Mix_or_Blend"] == mixer.mix_type)]

        if len(filtered2) == 1:
            return ("Big " + str(filtered2["Drinks"].item()))

        return "bad"

    def get_des(self, drink):
        return (self.drinks[self.drinks["Drinks"] == drink]["Description"].item())
    
    def get_fla(self, drink):
        return (self.drinks[self.drinks["Drinks"] == drink]["Flavour"].item())
    
    def get_type(self, drink):
        return (self.drinks[self.drinks["Drinks"] == drink]["Type"].item(),
                self.drinks[self.drinks["Drinks"] == drink]["Sec_Type"].item())
    
    def check_drink(self,drink,ndrink,nfla,ntype):
        return drink == ndrink, nfla == self.get_fla(drink), ntype in self.get_type(drink)
    
    def get_drink_list_w_con(self, condition):
        return self.drinks[
                            (self.drinks["Type"] == condition)
                           |(self.drinks["Sec_Type"] == condition)
                           |(self.drinks["Flavour"] == condition)
                           ]["Drinks"].tolist()
