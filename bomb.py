# coding: utf-8

# IMPORTS
import pygame

# Code additionnel
from toolbox import set_timeout

class Bomb(pygame.sprite.Sprite):
    """
        Architecture de base de l'objet bombe. Explose aprés 2 secondes et détruit les murs destructibles.
    """

    def __init__(self, player):
        super().__init__()
        self.player = player
        # Délais la bombe de 2 secondes
        self.boom = set_timeout(self.explosion, 2)
        self.image = pygame.image.load("assets/bomb.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        

    def explosion(self):
        """
            Fait des dégats dans quatres directions, tue les joueurs et casse les murs
        """

        # Change l'image de la bombe
        self.image = pygame.image.load("assets/boom.png")
        # La bombe se supprime aprés 0.5sec
        set_timeout(self.remove, 0.5)


    def remove(self):
        """
            Suppresion basique de l'objet bombe
        """
        # Supprime la bombe de la liste des bombes et de la carte
        self.player.all_bombs.remove(self)
