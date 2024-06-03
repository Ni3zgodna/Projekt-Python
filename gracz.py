import pygame

class Gracz:
    def __init__(self, szerokosc_okna, wysokosc_okna):
        self.szerokosc = szerokosc_okna
        self.wysokosc = wysokosc_okna

        self.wyglad = pygame.Surface((50, 50))
        self.wyglad.fill((0, 0, 0))
        self.kwadrat = self.wyglad.get_rect(center=(self.szerokosc, self.wysokosc - 70))
        # zastąpić kwadrat wczytaniem obrazu
        
        self.predkosc = 10

    def move(self, klawisze):
        if klawisze[pygame.K_LEFT] and self.kwadrat.left > 0:
            self.kwadrat.x -= self.predkosc
        if klawisze[pygame.K_RIGHT] and self.kwadrat.right < self.szerokosc:
            self.kwadrat.x += self.predkosc

    def draw(self, powierzchnia):
        powierzchnia.blit(self.wyglad, self.kwadrat)