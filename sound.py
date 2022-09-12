import pygame

class Sound:
    def __init__(self):
        self.main_music = pygame.mixer_music.load("ZeldaMusic.mp3")
        self.main_music_play = pygame.mixer.music.play(loops=-1)
        self.main_music_volume = pygame.mixer.music.set_volume(0.25)
