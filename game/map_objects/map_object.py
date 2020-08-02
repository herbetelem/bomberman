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
        
# créer la class banniere
class Banner(pygame.sprite.Sprite):
    def __init__(self, nb_joueur):
        # Sprite class init
        super().__init__()
        # Load la sprite de la banniere
        self.path_image = f"assets/map/banner_timer_{nb_joueur}.png"
        self.image = pygame.image.load(self.path_image)
        self.image = pygame.transform.scale(self.image, (1350, 75))
        # Créer le rect
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0