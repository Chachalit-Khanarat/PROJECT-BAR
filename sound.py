import pygame as pg
import os
import random

class SoundManager:

    def __init__(self):
        pg.mixer.init()
        self.background_music_list = os.listdir("data/music")
        self.current_music_index = 0
    
    def play_music(self):
        music_file = os.path.join("data/music", self.background_music_list[self.current_music_index])
        pg.mixer.music.load(music_file)
        pg.mixer.music.play(-1)
    
    def next_music(self):
        self.current_music_index = (self.current_music_index + 1) % len(self.background_music_list)
        self.play_music()
    
    def pause_music(self):
        pg.mixer.music.pause()
    
    def prev_music(self):
        self.current_music_index = (self.current_music_index - 1) % len(self.background_music_list)
        self.play_music()
    
    def continue_music(self):
        pg.mixer.music.unpause()

