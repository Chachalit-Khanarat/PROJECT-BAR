import pandas as pd

class Drinks:
    def __init__(self):
        self.drinks = pd.read_csv("menus.csv")
        self.drinks = self.drinks.set_index(self.drinks["Drinks"])
        print(type(self.drinks))
    
    def get_price(self, drink):
        return self.drinks["Price"][drink]
    
    def get_drink(self,A,B,D,F,K,rock,aged,mob):
        filtered = self.drinks[(self.drinks["A"] == A) 
                           & (self.drinks["B"] == B) 
                           & (self.drinks["D"] == D) 
                           & (self.drinks["F"] == F) 
                           & ((self.drinks["K"] == K) | (self.drinks["K"] == -1)) 
                           & (self.drinks["Rocks"] == rock) 
                           & (self.drinks["Aged"] == aged)
                           & (self.drinks["Mix_or_Blend"] == mob)]
        if len(filtered) == 0:
            return "bad"
        return filtered["Drinks"].item()

    def get_des(self, drink):
        return (self.drinks[self.drinks["Drinks"] == drink]["Description"].item())
    
    def get_fla(self, drink):
        return (self.drinks[self.drinks["Drinks"] == drink]["Flavour"].item())
    
    def get_type(self, drink):
        return (self.drinks[self.drinks["Drinks"] == drink]["Type"].item(),self.drinks[self.drinks["Drinks"] == drink]["Sec_Type"].item())
    
    def check_drink(self,drink,ndrink,nfla,ntype):
        return drink == ndrink, nfla == self.get_fla(drink), ntype in self.get_type(drink)
