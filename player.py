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
            if not self.game.check_collision(self, self.game.all_rocks):
                self.rect.y -= self.speed
            else:
                self.rect.y += 5
        elif direction == "s":
            if not self.game.check_collision(self, self.game.all_rocks):
                self.rect.y += self.speed
            else:
                self.rect.y -= 5
        elif direction == "q":
            if not self.game.check_collision(self, self.game.all_rocks):
                self.rect.x -= self.speed
            else:
                self.rect.x += 5
        elif direction == "d":
            if not self.game.check_collision(self, self.game.all_rocks):
                self.rect.x += self.speed
            else:
                self.rect.x -= 5