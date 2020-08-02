# coding: utf-8

# IMPORTS
import pygame

class Avatar_menu(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        # Sprite class init
        super().__init__()
        # Load le sprite de l'herbe
        self.path_image = f"assets/avatar/{name}.png"
        self.image = pygame.image.load(self.path_image)
        self.image = pygame.transform.scale(self.image, (100, 100))
        # Créer le rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y