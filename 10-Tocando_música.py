# Importando a biblioteca do pygame
import pygame
# Iniciando o mixer de aúdios
pygame.mixer.init()
# Carregando a música escolhida
pygame.mixer.music.load("Rise.mp3")
# Tocando a música
pygame.mixer.music.play()
# Definindo que a música só vai parar de tocar quando acabar o tempo da música
while(pygame.mixer.music.get_busy()):
    pass
