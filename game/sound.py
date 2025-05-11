import mutagen.flac
import pygame as pg
import os
import random
import mutagen

class SoundManager:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(SoundManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            pg.mixer.init()
            self.initialized = True
            self.background_music_list = os.listdir("data/music")
            self.music_state = True
            self.current_music_index = 0
            self.music_lenfgt = 0
    
    def play_music(self):
        music_file = os.path.join("data/music", self.background_music_list[self.current_music_index])
        pg.mixer.music.load(music_file)
        pg.mixer.music.play()
    
    def next_music(self):
        self.current_music_index = (self.current_music_index + 1) % len(self.background_music_list)
        self.play_music()
    
    def music_ctrl(self):
        if self.music_state:
            pg.mixer.music.pause()
            self.music_state = False
        elif not self.music_state:
            pg.mixer.music.unpause()
            self.music_state = True

    def prev_music(self):
        self.current_music_index = (self.current_music_index - 1) % len(self.background_music_list)
        self.play_music()
    
    def get_state(self):
        return self.music_state
    
    def get_music_data(self):
        music_file = os.path.join("data/music", self.background_music_list[self.current_music_index])
        audio = mutagen.File(music_file)
        return audio.info.length if audio and audio.info else 0

    def get_music_name(self):
        return self.background_music_list[self.current_music_index].replace(".flac", "").replace("_", " ").title()

    def get_current_music_percent(self):
        if self.music_lenfgt == 0:
            self.music_lenfgt = self.get_music_data()
        current_pos = pg.mixer.music.get_pos() / 1000
        return (current_pos / self.music_lenfgt)

    def get_music_time(self):
        self.music_lenfgt = self.get_music_data()
        current_pos = pg.mixer.music.get_pos() / 1000
        return current_pos, self.music_lenfgt
    
    def get_artist(self):
        music_file = os.path.join("data/music", self.background_music_list[self.current_music_index])
        audio = mutagen.File(music_file)
        if audio and "artist" in audio:
            return audio["artist"][0]



