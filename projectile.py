# coding: utf-8

# IMPORTS
import pygame

# definir la classe du projectile du joueur
class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, bomb, assets):
        super().__init__()
        self.velocity = 8
        self.bomb = bomb
        self.image = pygame.image.load(assets)
        self.rect = self.image.get_rect()
        self.rect.x = bomb.rect.x + 5
        self.rect.y = bomb.rect.y + 5
        self.origin_image = self.image
        self.angle = 0
        
    def move_top(self):
        self.rect.y -= self.velocity
        self.check_collision()
    def move_bot(self):
        self.rect.y += self.velocity
        self.check_collision()
    def move_left(self):
        self.rect.x -= self.velocity
        self.check_collision()
    def move_right(self):
        self.rect.x += self.velocity
        self.check_collision()
        
    def check_collision(self):
        # si le projectile touche un block indesctructible
        for bloc in self.bomb.player.game.check_collision(self, self.bomb.player.game.rocks_unbreakable):
            self.remove()
            self.velocity = 0
            self.rect.x = -50
        
        # si le projectile touche un block desctructible
        for bloc in self.bomb.player.game.check_collision(self, self.bomb.player.game.rocks_breakable):
            self.remove()
            self.velocity = 0
            self.rect.x = -50
            
            # SUPRIME LA LIGNE SANS S'ARRETER
            # del self
            # break
            
        # si le projectile touche une bomb
        # for player_bomb in self.bomb.player.game.players:
        #     if self.bomb.player.game.check_collision(self, player_bomb.all_bombs):
        #         self.remove()
        #         self.velocity = 0
        
        for player in self.bomb.player.game.check_collision(self, self.bomb.player.game.players):
                self.remove()
                self.velocity = 0
                self.rect.x = -50
                print("game over")