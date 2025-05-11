import pandas as pd
import random

class PlayerData:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(PlayerData, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.__player_id = int(random.randint(1, 100000000000000))
            self.__money = 100
            self.__day = 0
            self.__mistakes = 0
            self.__drinks = 0
            self.__customers = 0
            self.__items = []
            self.day_mistakes = 0
            self.day_drinks = 0
            self.day_customers = 0
            self.day_money = 0
            self.t_day_money = 0
    
    def get_money(self):
        return self.__money
    
    def reset_day(self):
        self.day_mistakes = 0
        self.day_drinks = 0
        self.day_customers = 0
        self.day_money = 0
        self.t_day_money = 0
        
    def day_end(self, rent : int):
        self.__day += 1
        self.__mistakes += self.day_mistakes
        self.__drinks += self.day_drinks
        self.__customers += self.day_customers

        self.t_day_money += self.day_money
        self.t_day_money += self.money_item_bonus()
        if self.money_day_bonus() != 0:
            self.t_day_money += self.money_day_bonus()

        self.t_day_money -= rent
        self.add_money(self.t_day_money)
        DataManager().add_player_data(self)

    def check_over(self):
        if self.__money < 0:
            return True
        return False

    def get_day(self):
        return self.__day
    def get_mistakes(self):
        return self.__mistakes
    def get_drinks(self):
        return self.__drinks
    

    def money_item_bonus(self):
        bonus = 0
        for i in self.__items:
            bonus += i["Bonus"]/100
        return self.day_money * bonus

    def money_day_bonus(self):
        if self.day_mistakes == 0:
            tips = self.day_drinks * 0.02
            if tips > 0.5:
                tips = 0.2
            return self.day_money * tips
        return 0

    def add_money(self, amount):
        self.__money += amount
    
    def minus_money(self, amount):
        self.__money -= amount
    
    def add_day_money(self, amount):
        self.day_money += amount
    
    def add_day_mistakes(self):
        self.day_mistakes += 1
    
    def add_day_drinks(self):
        self.day_drinks += 1

    def add_day_customers(self):
        self.day_customers += 1
    
    def get_items(self):
        return self.__items
    
    def add_item(self, item):
        if item not in self.__items:
            self.__items.append(item)
        else:
            print(f"Item {item} already exists in the inventory.")

    def __repr__(self):
        return f"PlayerData(money={self.__money}, day={self.__day}, mistakes={self.__mistakes}, drinks={self.__drinks}, customers={self.__customers}, items={self.__items})"

class DataManager:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(DataManager, cls).__new__(cls, *args, **kwargs)
            print("DataManager instance created")
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.cus_data = self.rcsv("data/csv/cus.csv")
            self.player = self.rcsv("data/csv/player.csv")
            self.items = self.rcsv("data/csv/items.csv")
            print("DataManager initialized")
        self.menu = self.rcsv("data/csv/menus.csv")
            
    def rcsv(self, path):
        return pd.read_csv(path)
    
    def get_data(self, want):
        if want == "menu":
            return self.menu
        if want == "player":
            return self.player
        if want == "items":
            return self.items
    
    def add_player_data(self, data : PlayerData):
        self.player = pd.concat([self.player, pd.DataFrame([data.__dict__])], ignore_index=True)
    
    def add_cus_data(self, data):
        self.cus_data = pd.concat([self.cus_data, pd.DataFrame([data.__dict__])], ignore_index=True)
    
    def save_data(self):
        self.cus_data.to_csv("data/csv/cus.csv", index=False)
        self.player.to_csv("data/csv/player.csv", index=False)
        self.items.to_csv("data/csv/items.csv", index=False)
        print("data saved")

