# coding: utf-8

# IMPORTS
import pygame

class Avatar_bg(pygame.sprite.Sprite):
    def __init__(self):
        # Sprite class init
        super().__init__()
        # Load le sprite de l'herbe
        self.path_image = f"assets/avatar/bg.png"
        self.image = pygame.image.load(self.path_image)
        self.image = pygame.transform.scale(self.image, (1366, 768))
        # Créer le rect
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0