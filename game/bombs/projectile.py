# coding: utf-8

# IMPORTS
import pygame
from game.map_objects.map_object import Grass

# definir la classe du projectile du joueur
class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, bomb, assets, direction):
        super().__init__()
        self.velocity = 8
        self.bomb = bomb
        self.image = pygame.image.load(assets)
        self.rect = self.image.get_rect()
        if direction == "top":
            self.rect.x = bomb.rect.x + 5
            self.rect.y = bomb.rect.y - 30
        elif direction == "bot":
            self.rect.x = bomb.rect.x + 5
            self.rect.y = bomb.rect.y + 32
        elif direction == "left":
            self.rect.x = bomb.rect.x - 30
            self.rect.y = bomb.rect.y + 5
        elif direction == "right":
            self.rect.x = bomb.rect.x + 32
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
        # si le projectile touche un joueur
        temps = [""] * 4
        temps[0] = pygame.sprite.groupcollide(self.bomb.all_projectiles_top, self.bomb.player.game.all_players, True, True)
        temps[1] = pygame.sprite.groupcollide(self.bomb.all_projectiles_bot, self.bomb.player.game.all_players, True, True)
        temps[2] = pygame.sprite.groupcollide(self.bomb.all_projectiles_left, self.bomb.player.game.all_players, True, True)
        temps[3] = pygame.sprite.groupcollide(self.bomb.all_projectiles_right, self.bomb.player.game.all_players, True, True)
        
        for temp in temps:
            for players in temp:
                for player in temp[players]:
                    # pygame.sprite.Sprite.kill(player)
                    player.image = player.ghost_image
                    player.is_ghost = True

        # si le projectile touche un block indesctructible, supprime juste le projectile
        pygame.sprite.groupcollide(self.bomb.all_projectiles_top, self.bomb.player.game.rocks_unbreakable, True, False)
        pygame.sprite.groupcollide(self.bomb.all_projectiles_bot, self.bomb.player.game.rocks_unbreakable, True, False)
        pygame.sprite.groupcollide(self.bomb.all_projectiles_left, self.bomb.player.game.rocks_unbreakable, True, False)
        pygame.sprite.groupcollide(self.bomb.all_projectiles_right, self.bomb.player.game.rocks_unbreakable, True, False)

        # # si le projectile touche une bombe
        for player in self.bomb.player.game.players:
            pygame.sprite.groupcollide(self.bomb.all_projectiles_top, player.all_bombs, True, False)
            pygame.sprite.groupcollide(self.bomb.all_projectiles_bot, player.all_bombs, True, False)
            pygame.sprite.groupcollide(self.bomb.all_projectiles_left, player.all_bombs, True, False)
            pygame.sprite.groupcollide(self.bomb.all_projectiles_right, player.all_bombs, True, False)

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
                    # son mur qui casse
                    son = pygame.mixer.Sound("assets/sounds/break.ogg")
                    son.play()

