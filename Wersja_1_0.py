import pygame
import time

pygame.init()

szerokosc_okna = 800
wysokosc_okna = 600
okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))

trwanie = True

while trwanie:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            trwanie = False

    okno.fill((255, 255, 255))

    pygame.display.flip()

pygame.quit()