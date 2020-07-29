# coding: utf-8

import pygame

# Créer les rochers destructibles ou non
class Rock(pygame.sprite.Sprite):
    """
        Architecture des rochers, destructibles ou non
    """

    def __init__(self, can_break, x, y):
        # Sprite class init
        super().__init__()
        # Le rocher est-il destructible ?
        self.can_break = can_break
        # Load l'image en fonction de can_break
        if can_break:
            # Load le sprite du rocher cassable
            self.image = pygame.image.load("assets/map/rock_weak.png")
        else:
            # Load le sprite du rocher incassable
            self.image = pygame.image.load("assets/map/rock_strong.png")
        # Créer le rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Grass(pygame.sprite.Sprite):
    """
        Architecture de l'herbe
    """

    def __init__(self, x, y):
        # Sprite class init
        super().__init__()
        # Load le sprite du rocher incassable
        self.image = pygame.image.load("assets/map/no_rock.png")
        # Créer le rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
