# coding: utf-8

import pygame

# créer la classe des herbes
class Grass(pygame.sprite.Sprite):
    """
        Architecture de l'herbe
    """

    def __init__(self, x, y):
        # Sprite class init
        super().__init__()
        # Load le sprite de l'herbe
        self.image = pygame.image.load("assets/map/no_rock.png")
        # Créer le rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
