# coding: utf-8

# IMPORTS
import pygame

class Banner(pygame.sprite.Sprite):
    def __init__(self):
        # Sprite class init
        super().__init__()
        # Load le sprite de l'herbe
        self.image = pygame.image.load("assets/map/banner_timer.png")
        self.image = pygame.transform.scale(self.image, (1350, 75))
        # Créer le rect
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0