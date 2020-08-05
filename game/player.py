# coding: utf-8

# IMPORTS
import pygame

# Code additionnel
from game.bombs.bomb import Bomb

# créer la classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y, sprite_ghost):
        super().__init__()
        self.game = game
        # Vitesse du joueur
        self.speed = 5
        # Image de base du joueur
        self.image = pygame.image.load("assets/favicon.png")
        self.image_win = pygame.image.load("assets/favicon.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Créer le groupe des bombes
        self.all_bombs = pygame.sprite.Group()
        self.nb_bombs = 0
        # Est fantome
        self.is_ghost = False
        # Change l'image du joueur en fantome
        self.ghost_path = f"assets/ghost/ghost_{sprite_ghost}.png"
        self.ghost_image = pygame.image.load(self.ghost_path)
        # Utilise le numéro de joueur pour lui assigner des datas
        if sprite_ghost == 1:
            # J1
            # Positions de l'avatar et des bombes du statut
            self.status_position_list = [(10, 15), (65, 20), (105, 20), (145, 20)]
        elif sprite_ghost == 2:
            # J2
            # Positions de l'avatar et des bombes du statut
            self.status_position_list = [(325, 15), (390, 20), (430, 20), (470, 20)]
        try:
            # Evite les erreurs quand il n'y a que 2 joueurs
            if sprite_ghost == 3:
                # J3
                # Positions de l'avatar et des bombes du statut
                self.status_position_list = [(950, 15), (910, 20), (870, 20), (830, 20)]
            elif sprite_ghost == 4:
                # J4
                # Positions de l'avatar et des bombes du statut
                self.status_position_list = [(1295, 15), (1255, 20), (1215, 20), (1175, 20)]
        except:
            pass

    def moove(self, direction):
        #   je verifie la direction
        if direction == "z":
        #   je deplace le bonhomme
            self.rect.y -= self.speed
        #   je verifie que le joueur ne soit pas un ghost car "i'm afraid no ghost"
            if not self.is_ghost:
        #       si collision avez un rocher incassable
                if self.game.check_collision(self, self.game.rocks_unbreakable):
        #           je revien en arriere
                    self.rect.y += self.speed
        #       si collision avez un rocher cassable
                elif self.game.check_collision(self, self.game.rocks_breakable):
        #           je revien en arriere
                    self.rect.y += self.speed
        elif direction == "s":
            self.rect.y += self.speed
            if not self.is_ghost:
                if self.game.check_collision(self, self.game.rocks_unbreakable):
                    self.rect.y -= self.speed
                elif self.game.check_collision(self, self.game.rocks_breakable):
                    self.rect.y -= self.speed
        elif direction == "q":
            self.rect.x -= self.speed
            if not self.is_ghost:
                if self.game.check_collision(self, self.game.rocks_unbreakable):
                    self.rect.x += self.speed
                elif self.game.check_collision(self, self.game.rocks_breakable):
                    self.rect.x += self.speed
        elif direction == "d":
            self.rect.x += self.speed
            if not self.is_ghost:
                if self.game.check_collision(self, self.game.rocks_breakable):
                    self.rect.x -= self.speed
                elif self.game.check_collision(self, self.game.rocks_unbreakable):
                    self.rect.x -= self.speed

    def drop_bomb(self):
        """
            Laisse le joueur poser une bombe au sol (Max : 3)
        """
        if not self.is_ghost:
            if len(self.all_bombs) < 3:
                # Si le joueur n'a pas posé 3 bombes
                # Pose une bombe
                bomb = Bomb(self)
                if not self.game.check_collision(bomb, self.all_bombs):
                    self.nb_bombs += 1
                    self.all_bombs.add(bomb)
                else:
                    del bomb
                