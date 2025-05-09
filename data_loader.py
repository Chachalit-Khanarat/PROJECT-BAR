import pygame

class DataLoader:

    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(DataLoader, cls).__new__(cls)
            cls.__instance.load_data()
        return cls.__instance
    
    def __init__(self):
        pass

    def load_background(self, file_path):
        self.background = pygame.image.load(file_path).convert()
        return self.background