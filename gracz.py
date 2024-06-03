import pygame

class Gracz:
    def __init__(self, szerokosc_okna, wysokosc_okna):
        self.szerokosc = szerokosc_okna
        self.wysokosc = wysokosc_okna

        self.wyglad = pygame.Surface((50, 50))
        self.wyglad.fill((0, 0, 0))
        self.kwadrat = self.wyglad.get_rect(center=(self.szerokosc, self.wysokosc - 70))
        # zastąpić kwadrat wczytaniem obrazu

    def draw(self, powierzchnia):
        powierzchnia.blit(self.wyglad, self.kwadrat)