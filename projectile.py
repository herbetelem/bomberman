# coding: utf-8

# IMPORTS
import pygame

# definir la classe du projectile du joueur
class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, player, assets):
        super().__init__()
        self.velocity = 8
        self.player = player
        self.image = pygame.image.load(assets)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 5
        self.rect.y = player.rect.y + 5
        self.origin_image = self.image
        self.angle = 0
        
    def move_top(self):
        self.rect.y -= self.velocity
    def move_bot(self):
        self.rect.y += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity
    def move_right(self):
        self.rect.x += self.velocity