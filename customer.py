import random
from drinks import Drinks


class Customer:
    def __init__(self):
        self.loc = None
        self.sprite = None
        self.name = None
        self.fdrinks = []
        self.line = None
        self.prevference = None

    def __repr__(self):
        return f"Customer Name: {self.name}, Drinks: {self.fdrinks}"
    
    def get_drink(self):
        return self.fdrinks

    def get_order(self):
        print(self.name, self.fdrinks, len(self.fdrinks))
        if len(self.fdrinks) == 1:
            drink = self.fdrinks[0]
            self.line = random.choice([f"Hey there. I’ll have a {drink}, please.",
                                        f"I’ll have a {drink}, please.",
                                        f"I’ll have a {drink}.",
                                        f"Hi, I’ll have a glass of {drink}, please."]).replace("_", " ")
        elif len(self.fdrinks) > 1:
            self.line = random.choice([f"Just got off the grid. I need something {self.prevference}."])
        self.line = self.name + " : " + self.line

    def give_drink(self, drink):
        if drink in self.fdrinks:
            self.line = random.choice([f"Wow, this is exactly what I wanted!",
                                        f"This is perfect!",
                                        f"This is exactly what I wanted!",
                                        f"Wow, this is amazing!"])
        else:
            self.line = random.choice([f"This is not what I ordered.",
                                        f"This is not what I wanted.",
                                        f"This is not what I expected."])


class male_npc(Customer):
    def __init__(self):
        super().__init__()
        self.name = random.choice(["John", "Mike", "Tom", "Jack", "Alex", "Chris"])
        self.sprite = self.get_sprite()
        print(self)
        self.randrink()
        self.get_order()

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

        self.fdrinks = random.choice([[random.choice(Drinks().get_drink_list_w_con(self.prevference))],Drinks().get_drink_list_w_con(self.prevference)])

    def get_sprite(self):
        self.sprite = random.choice([("male1.png", (210.6,132.6)),
                                     ("male2.png", (161.8,47.2)),
                                     ("male1.png", (210.6,132.6))])
        return self.sprite

class female_npc(Customer):
    def __init__(self):
        super().__init__()
        self.name = random.choice(["Ant" ,"Lele" ,"Lucy" ,"Raven" ,"Mia" ,"Luna"])
        self.sprite = self.get_sprite()
        print(self)
        self.randrink()
        self.get_order()

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

        self.fdrinks = random.choice([random.choice(Drinks().get_drink_list_w_con(self.prevference)),Drinks().get_drink_list_w_con(self.prevference)])

    def get_sprite(self):
        self.sprite = random.choice([("male1.png", (210.6,132.6)),
                                     ("male2.png", (161.8,47.2)),
                                     ("male1.png", (210.6,132.6))])
        return self.sprite

class pixelmiku(Customer):
    def __init__(self):
        super().__init__()
        self.name = "Pixelated Miku"
        self.fdrinks = ["BlueFairy","Mercuryblast"]
        self.sprite = "pixelmiku.png"

class sans(Customer):
    def __init__(self):
        super().__init__()
        self.name = "Sans Undertale"
        self.fdrinks = ["Gut_Punch"]
        self.sprite = "sans.png"

class mark(Customer):
    def __init__(self):
        super().__init__()
        self.name = "mark"
        self.fdrinks = ["Piano_Man"]
        self.sprite = "mark.png"
