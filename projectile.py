# coding: utf-8

# IMPORTS
import pygame
from grass import Grass

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
        # si le projectile touche un block indesctructible, supprime juste le projectile
        pygame.sprite.groupcollide(self.bomb.all_projectiles_top, self.bomb.player.game.rocks_unbreakable, True, False)
        pygame.sprite.groupcollide(self.bomb.all_projectiles_bot, self.bomb.player.game.rocks_unbreakable, True, False)
        pygame.sprite.groupcollide(self.bomb.all_projectiles_left, self.bomb.player.game.rocks_unbreakable, True, False)
        pygame.sprite.groupcollide(self.bomb.all_projectiles_right, self.bomb.player.game.rocks_unbreakable, True, False)

        # si le projectile touche un block desctructible, supprime le projectile et le rocher
        temps = [""]*4
        temps[0] = pygame.sprite.groupcollide(self.bomb.all_projectiles_top, self.bomb.player.game.rocks_breakable, True, True)
        temps[1] = pygame.sprite.groupcollide(self.bomb.all_projectiles_bot, self.bomb.player.game.rocks_breakable, True, True)
        temps[2] = pygame.sprite.groupcollide(self.bomb.all_projectiles_left, self.bomb.player.game.rocks_breakable, True, True)
        temps[3] = pygame.sprite.groupcollide(self.bomb.all_projectiles_right, self.bomb.player.game.rocks_breakable, True, True)

        # Remplace les rochers par de l'herbe
        for temp in temps:
            for rocks in temp:
                for rock in temp[rocks]:
                    # Récupére la position du rocher détruit et créer un objet herbe
                    self.bomb.player.game.all_grass.add(Grass(rock.rect.x, rock.rect.y))

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
