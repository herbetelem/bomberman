# coding: utf-8

# IMPORTS
import pygame
import json

# Code additionnel
from rock import Rock
from grass import Grass
from banner import Banner
from player import Player

# créer la classe game qui vas gerer les parties
class Game:
    
    def __init__(self, nb_joueur):
        # definir si le jeu a commencer ou pas
        self.is_playing = False
        self.nb_joueur = nb_joueur
        # MAP #
        # Liste des rochers
        self.rock_list = []
        # Charge la map en fonction du nombre de joueurs
        if nb_joueur == 2:
            # Map pour 2 joueurs
            with open("assets/map/2_players_map.json", "r") as load:
                self. rock_list = json.loads(load.read())
        elif nb_joueur == 3:
            # Map pour 3 joueurs
            with open("assets/map/3_players_map.json", "r") as load:
                self. rock_list = json.loads(load.read())
        elif nb_joueur == 4:
            # Map pour 4 joueurs
            with open("assets/map/4_players_map.json", "r") as load:
                self. rock_list = json.loads(load.read())

        # Créer le groupe de sprites
        self.rocks_breakable = pygame.sprite.Group()
        self.rocks_unbreakable = pygame.sprite.Group()
        self.all_grass = pygame.sprite.Group()
        self.banner = Banner()
        # Créer les blocs en parcourant la liste
        y = 75
        for rock in self.rock_list:
            x = 0
            for can_break in rock:
                if can_break != None:
                    self.rock_tile = Rock(can_break, x, y)
                    if can_break:
                        self.rocks_breakable.add(self.rock_tile)
                    else:
                        self.rocks_unbreakable.add(self.rock_tile)
                else:
                    self.grass_tile = Grass(x, y)
                    self.all_grass.add(self.grass_tile)
                x += 50
            y += 50

        # PLAYERS #
        # Créer la liste des joueurs
        self.players = []
        # Créer le groupe de joueur
        self.all_players = pygame.sprite.Group()
        # Générer les joueurs
        # Position joueurs
        #                P1            P2          P3         P4
        player_x_y = [[55, 130], [1255, 630], [1255, 130], [55, 630]]
        for index in range(0, nb_joueur):
            player = Player(self, player_x_y[index][0], player_x_y[index][1], (index + 1))
            self.players.append(player)
            self.all_players.add(player)
            
        # TIMER #
        # initialiser le timer
        self.clock = pygame.time.Clock() 
        # La limite de temps est de 10 minutes (en ms)
        self.timer = 600000
        # Choisis la police d'écriture
        self.game_font = pygame.font.SysFont('Bahnschrift', 30)
        
        # créer la librairie de touche
        self.pressed = {}


    def update(self, screen):
        """
            Update la position des rochers et des joueurs sur la carte
        """
        
        # Section timer
        # Enléve le temps passé au temps restant
        self.timer -= self.clock.tick(60)
        # Créer l'objet de texte
        timer_text = self.game_font.render(str(round(self.timer / 1000)), True, (255, 255, 255))
        # update rock
        for rock in self.rocks_unbreakable:
            screen.blit(rock.image, rock.rect)
        for rock in self.rocks_breakable:
            screen.blit(rock.image, rock.rect)
        # update grass
        for grass in self.all_grass:
            screen.blit(grass.image, grass.rect)
        # Update les bombes
        for player in self.players:
            for bomb in player.all_bombs:
                screen.blit(bomb.image, bomb.rect)
                # recuperer les projectiles du joeur
                for projectiles in bomb.all_projectiles_top:
                    projectiles.move_top()
                    screen.blit(projectiles.image, projectiles.rect)
                for projectiles in bomb.all_projectiles_bot:
                    projectiles.move_bot()
                    screen.blit(projectiles.image, projectiles.rect)
                for projectiles in bomb.all_projectiles_left:
                    projectiles.move_left()
                    screen.blit(projectiles.image, projectiles.rect)
                for projectiles in bomb.all_projectiles_right:
                    projectiles.move_right()
                    screen.blit(projectiles.image, projectiles.rect)
        # update les joueurs
        for player in self.players:
            screen.blit(player.image, player.rect)
        # update la banniere
        screen.blit(self.banner.image, self.banner.rect)
        # Affiche le timer
        screen.blit(timer_text, (screen.get_width() / 2.05, 19))
        # Affiche les joueurs et le nombre de bombes
        # Joueur 1
        self.status_printer(screen, self.players[0])
        # Joueur 2
        self.status_printer(screen, self.players[1])
        # Joueur 3
        if self.nb_joueur == 3:
            self.status_printer(screen, self.players[2])
        # Joueur 4
        if self.nb_joueur == 4:
            self.status_printer(screen, self.players[2])
            self.status_printer(screen, self.players[3])

        # check ver la ou le joueur 1 veut aller
        # pygame prend les touches en qwerty donc w->z a->q
        if self.pressed.get(pygame.K_w):
            if (self.players[0].rect.y) > 130:
                self.players[0].moove("z")
        elif self.pressed.get(pygame.K_a):
            if (self.players[0].rect.x) > 50:
                self.players[0].moove("q")
        elif self.pressed.get(pygame.K_s):
            if (self.players[0].rect.y + self.players[0].rect.width) < (screen.get_height() - 50):
                self.players[0].moove("s")
        elif self.pressed.get(pygame.K_d):
            if (self.players[0].rect.x + self.players[0].rect.width) < (screen.get_width() - 50):
                self.players[0].moove("d")

        # check ver la ou le joueur 2 veut aller
        if self.pressed.get(pygame.K_i):
            if (self.players[1].rect.y) > 130:
                self.players[1].moove("z")
        elif self.pressed.get(pygame.K_j):
            if (self.players[1].rect.x) > 50:
                self.players[1].moove("q")
        elif self.pressed.get(pygame.K_k):
            if (self.players[1].rect.y + self.players[1].rect.width) < (screen.get_height() - 50):
                self.players[1].moove("s")
        elif self.pressed.get(pygame.K_l):
            if (self.players[1].rect.x + self.players[1].rect.width) < (screen.get_width() - 50):
                self.players[1].moove("d")

        # check ver la ou le joueur 3 veut aller
        try:
            if self.pressed.get(pygame.K_KP8):
                if (self.players[2].rect.y) > 130:
                    self.players[2].moove("z")
            elif self.pressed.get(pygame.K_KP4):
                if (self.players[2].rect.x) > 50:
                    self.players[2].moove("q")
            elif self.pressed.get(pygame.K_KP5):
                if (self.players[2].rect.y + self.players[2].rect.width) < (screen.get_height() - 50):
                    self.players[2].moove("s")
            elif self.pressed.get(pygame.K_KP6):
                if (self.players[2].rect.x + self.players[2].rect.width) < (screen.get_width() - 50):
                    self.players[2].moove("d")
        except IndexError:
            pass

        # check ver la ou le joueur 4 veut aller
        try:
            if self.pressed.get(pygame.K_UP):
                if (self.players[3].rect.y) > 130:
                    self.players[3].moove("z")
            elif self.pressed.get(pygame.K_LEFT):
                if (self.players[3].rect.x) > 50:
                    self.players[3].moove("q")
            elif self.pressed.get(pygame.K_DOWN):
                if (self.players[3].rect.y + self.players[3].rect.width) < (screen.get_height() - 50):
                    self.players[3].moove("s")
            elif self.pressed.get(pygame.K_RIGHT):
                if (self.players[3].rect.x + self.players[3].rect.width) < (screen.get_width() - 50):
                    self.players[3].moove("d")
        except IndexError:
            pass
    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def status_printer(self, screen, player):
        """
            Affiche le statut du joueur (vivant / nombres de bombes sur la map)
        """
        # Affiche l'avatar du joueur
        screen.blit(player.image, player.status_position_list[0])
        # Affiche les bombes du joueur
        if len(player.all_bombs) == 1:
            # Le joueur a 1 bombe sur la map
            screen.blit(pygame.image.load("assets/bomb.png"), player.status_position_list[1])
        elif len(player.all_bombs) == 2:
            # Le joueur a 2 bombe sur la map
            screen.blit(pygame.image.load("assets/bomb.png"), player.status_position_list[1])
            screen.blit(pygame.image.load("assets/bomb.png"), player.status_position_list[2])
        elif len(player.all_bombs) == 3:
            # Le joueur a 3 bombe sur la map
            screen.blit(pygame.image.load("assets/bomb.png"), player.status_position_list[1])
            screen.blit(pygame.image.load("assets/bomb.png"), player.status_position_list[2])
            screen.blit(pygame.image.load("assets/bomb.png"), player.status_position_list[3])
