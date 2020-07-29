# coding: utf-8

# IMPORTS
import pygame
import json

# Code additionnel
from rock import Rock
from rock import Grass
from player import Player

# créer la classe game qui vas gerer les parties
class Game:
    
    def __init__(self, nb_joueur):
        # definir si le jeu a commencer ou pas
        self.is_playing = False
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
        self.all_rocks = pygame.sprite.Group()
        self.all_grass = pygame.sprite.Group()
        # Créer les blocs en parcourant la liste
        y = 75
        for rock in self.rock_list:
            x = 0
            for can_break in rock:
                if can_break != None:
                    self.rock_tile = Rock(can_break, x, y)
                    self.all_rocks.add(self.rock_tile)
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
            player = Player(self, player_x_y[index][0], player_x_y[index][1])
            self.players.append(player)
            self.all_players.add(player)
            
        # créer la librairie de touche
        self.pressed = {}

    def update(self, screen):
        """
            Update la position des rochers et des joueurs sur la carte
        """
        # update rock
        for rock in self.all_rocks:
            screen.blit(rock.image, rock.rect)
        # update grass
        for grass in self.all_grass:
            screen.blit(grass.image, grass.rect)
        # update les joueurs
        for player in self.players:
            screen.blit(player.image, player.rect)

        # check ver la ou le joueur 1 veu aller
        # IMPORTANT #
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

        # check ver la ou le joueur 2 veu aller
        # IMPORTANT #
        # pygame prend les touches en qwerty donc w->z a->q
        if self.pressed.get(pygame.K_i):
            if (self.players[1].rect.y) > 130:
                self.players[1].moove("z")
        elif self.pressed.get(pygame.K_j):
            if (self.players[1].rect.x) > 50:
                self.players[1].moove("q")
        elif self.pressed.get(pygame.K_k):
            if (self.players[1].rect.y + self.players[0].rect.width) < (screen.get_height() - 50):
                self.players[1].moove("s")
        elif self.pressed.get(pygame.K_l):
            if (self.players[1].rect.x + self.players[0].rect.width) < (screen.get_width() - 50):
                self.players[1].moove("d")
    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)