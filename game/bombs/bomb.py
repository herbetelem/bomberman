# coding: utf-8

# IMPORTS
import pygame
from game.bombs.projectile import Projectile

# Code additionnel
from game.toolbox import set_timeout

class Bomb(pygame.sprite.Sprite):
    """
        Architecture de base de l'objet bombe. Explose aprés 2 secondes et détruit les murs destructibles.
    """

    def __init__(self, player):
        super().__init__()
        self.player = player
        # Délais la bombe de 2 secondes
        self.animation_1 = set_timeout(self.hot_1, 0.5)
        self.animation_1 = set_timeout(self.hot_2, 1)
        self.animation_1 = set_timeout(self.hot_3, 1.5)
        self.boom = set_timeout(self.explosion, 2)
        self.image = pygame.image.load("assets/bombs/bomb.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        # Créer les groups de projectiles
        self.all_projectiles_top = pygame.sprite.Group()
        self.all_projectiles_bot = pygame.sprite.Group()
        self.all_projectiles_left = pygame.sprite.Group()
        self.all_projectiles_right = pygame.sprite.Group()


    def hot_1(self):
        # chagement de la sprite en fonction de l'étape
        self.image = pygame.image.load("assets/bombs/bomb_hot_1.png")
    def hot_2(self):
        # chagement de la sprite en fonction de l'étape
        self.image = pygame.image.load("assets/bombs/bomb_hot_2.png")
    def hot_3(self):
        # chagement de la sprite en fonction de l'étape
        self.image = pygame.image.load("assets/bombs/bomb_hot_3.png")


    def explosion(self):
        """
            Fait des dégats dans quatres directions, tue les joueurs et casse les murs
        """

        # son explosion
        son = pygame.mixer.Sound("assets/sounds/boom.ogg")
        son.play()
        # Change l'image de la bombe
        self.image = pygame.image.load("assets/bombs/boom.png")
        # La bombe se supprime aprés 1sec
        set_timeout(self.remove, 1)
        # créer les 4 flammes
        self.all_projectiles_top.add(Projectile(self, "assets/bombs/projectile.png", "top"))
        self.all_projectiles_bot.add(Projectile(self, "assets/bombs/projectile.png", "bot"))
        self.all_projectiles_left.add(Projectile(self, "assets/bombs/projectile.png", "left"))
        self.all_projectiles_right.add(Projectile(self, "assets/bombs/projectile.png", "right"))


    def remove(self):
        """
            Suppresion basique de l'objet bombe
        """
        # Supprime la bombe de la liste des bombes et de la carte
        self.player.all_bombs.remove(self)
        self.player.nb_bombs -= 1
