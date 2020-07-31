# coding: utf-8

# IMPORTS
import pygame

# Code additionnel
from bomb import Bomb

# créer la classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y, sprite_ghost):
        super().__init__()
        self.game = game
        self.speed = 5
        self.image = pygame.image.load('assets/favicon.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Créer le groupe des bombes
        self.all_bombs = pygame.sprite.Group()
        # est fantome
        self.is_ghost = False
        self.ghost_path = f"assets/ghost_{sprite_ghost}.png"
        self.ghost_image = pygame.image.load(self.ghost_path)

    # method de delacement
    #   je verifie la direction
    #       si il n'y a pas collision je me deplace
    #           je me deplace de ma speed
    #       sinon
    #           je suis ejecter de ma speed en arriere
    def moove(self, direction):
        if direction == "z":
            self.rect.y -= self.speed
            if not self.is_ghost:
                if self.game.check_collision(self, self.game.rocks_unbreakable):
                    self.rect.y += self.speed
                elif self.game.check_collision(self, self.game.rocks_breakable):
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
                    self.all_bombs.add(bomb)
                else:
                    del bomb
                