import pygame
from pygame import mixer

pygame.init()
pygame.mixer.music.load('ze.mp3')
pygame.mixer.music.play()
mixer.music.set_volume(0.1)
mixer.music.play()
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        exit()





