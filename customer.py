import random
import pandas as pd
from drinks import *

class Customer:
    def __init__(self):
        self.loc = None
        self.sprite = None
        self.name = None
        self.fdrinks = None
        self.line = None
        self.prevference = None

    def get_info(self):
        return f"Customer Name: {self.name}, Age: {self.age}"
    
    def get_drink(self):
        return self.fdrinks
    
    def get_line(self):
        if len(self.fdrinks) == 1:
            drink = self.fdrinks[0]
            self.line = random.choice([f"Hey there. I’ll have a {drink}, please.",
                                        f"I’ll have a {drink}, please.",
                                        f"I’ll have a {drink}.",
                                        f"Hi, I’ll have a glass of {drink}, please."])
        self.line = random.choice([f"Just got off the grid. I need something {self.prevference}."])
        return self.line


class male_npc(Customer):
    def __init__(self):
        super().__init__()
        self.name = random.choice(["John", "Mike", "Tom"])
        self.sprite = self.get_sprite()
        self.fdrinks = self.randrink()
        self.line = self.get_line()

    def randrink(self):
        chance = random.randint(0, 100)
        if chance < 50:
            self.prevference = "Manly"

        elif chance < 70:
            self.prevference = "Classic"

        elif chance < 90:
            self.prevference = "Promo"

        elif chance < 100:
            self.prevference = "Girly"

        return random.choice([random.choice(Drinks().get_drink_list_w_con(self.prevference)),Drinks().get_drink_list_w_con(self.prevference)])

    def get_sprite(self):
        self.sprite = random.choice([("male1.png", (274.9,254.2)),
                                     ("male1.png", (274.9,254.2)),
                                     ("male1.png", (274.9,254.2))])
        return self.sprite
    
    def __repr__(self):
        return f"Customer Name: {self.name}, Drinks: {self.fdrinks}"


class female_npc(Customer):
    def __init__(self):
        super().__init__()
        self.sprite = self.get_sprite()
        self.fdrinks = self.randrink()
        self.line = self.get_line()

    def randrink(self):
        chance = random.randint(0, 100)
        if chance < 50:
            self.prevference = "Girly"

        elif chance < 70:
            self.prevference = "Promo"

        elif chance < 90:
            self.prevference = "Classic"

        elif chance < 100:
            self.prevference = "Manly"

        return random.choice([random.choice(Drinks().get_drink_list_w_con(self.prevference)),Drinks().get_drink_list_w_con(self.prevference)])

    def get_sprite(self):
        self.sprite = random.choice([("male1.png", (random.randint(57,495),254.2)),
                                     ("male1.png", (random.randint(57,495),254.2)),
                                     ("male1.png", (random.randint(57,495),254.2))])
    
    def __repr__(self):
        return f"Customer Name: {self.name}, Drinks: {self.fdrinks}"

class pixelmiku(Customer):
    def __init__(self):
        super().__init__()
        self.name = "pixelmiku"
        self.fdrinks = ["BlueFairy","Mercuryblast"]
        self.sprite = "pixelmiku.png"

class sans(Customer):
    def __init__(self):
        super().__init__()
        self.name = "sans"
        self.fdrinks = ["Gut_Punch"]
        self.sprite = "sans.png"
