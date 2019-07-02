import pygame

def soundMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("pokemon.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue