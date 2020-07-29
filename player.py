import pygame

# créer la classe joueur
class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.speed = 5
        self.image = pygame.image.load('assets/favicon.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 55
        self.rect.y = 130