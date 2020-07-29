# coding: utf-8

# IMPORTS
import pygame
import json

# Code additionnel
from rock import Rock
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
        # Créer les blocs en parcourant la liste
        y = 75
        for rock in self.rock_list:
            x = 0
            for can_break in rock:
                if can_break != None:
                    self.rock_tile = Rock(can_break, x, y)
                    self.all_rocks.add(self.rock_tile)
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

    def update(self, screen):
        """
            Update la position des rochers et des joueurs sur la carte
        """
        # update rock
        for rock in self.all_rocks:
            screen.blit(rock.image, rock.rect)
        # update les joueurs
        for player in self.players:
            screen.blit(player.image, player.rect)
