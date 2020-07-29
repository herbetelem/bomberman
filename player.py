# coding: utf-8

import pygame

# créer la classe joueur
class Player(pygame.sprite.Sprite):
    
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.speed = 5
        self.image = pygame.image.load('assets/favicon.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    # method de delacement
    #   je verifie la direction
    #       si il n'y a pas collision je me deplace
    #           je me deplace de ma speed
    #       sinon
    #           je suis ejecter de ma speed en arriere
    def moove(self, direction):
        if direction == "z":
            self.rect.y -= self.speed
            if self.game.check_collision(self, self.game.all_rocks):
                self.rect.y += self.speed
        elif direction == "s":
            self.rect.y += self.speed
            if self.game.check_collision(self, self.game.all_rocks):
                self.rect.y -= self.speed
        elif direction == "q":
            self.rect.x -= self.speed
            if self.game.check_collision(self, self.game.all_rocks):
                self.rect.x += self.speed
        elif direction == "d":
            self.rect.x += self.speed
            if self.game.check_collision(self, self.game.all_rocks):
                self.rect.x -= self.speed