# coding: utf-8

# IMPORTS
import pygame

class Banner(pygame.sprite.Sprite):
    def __init__(self, nb_joueur):
        # Sprite class init
        super().__init__()
        # Load le sprite de l'herbe
        self.path_image = f"assets/map/banner_timer_{nb_joueur}.png"
        self.image = pygame.image.load(self.path_image)
        self.image = pygame.transform.scale(self.image, (1350, 75))
        # Créer le rect
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0