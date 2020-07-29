# coding: utf-8

# IMPORTS
import pygame

# Code additionnel
from rock import Rock
from player import Player

# créer la classe game qui vas gerer les parties
class Game:
    
    def __init__(self, nb_joueur, screen):
        # definir si le jeu a commencer ou pas
        self.is_playing = False
        # MAP #
        # Charge la map

        # Liste des rochers
        self.rock_list = [
                        # Ligne 1
                        #   1     2      3      4      5      6      7      8      9      10     11     12     13     14     15     16     17     18     19     20     21     22     23     24     25     26     27
                        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
                        # Ligne 2
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, None, None, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, None, None, False],
                        # Ligne 3
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, None, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, None, False],
                        # Ligne 4
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False],
                        # Ligne 5
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False],
                        # Ligne 6
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False],
                        # Ligne 7
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False],
                        # Ligne 8
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False],
                        # Ligne 9
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False],
                        # Ligne 10
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False],
                        # Ligne 11
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, None, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, None, False],
                        # Ligne 12
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, None, None, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, None, None, False],
                        # Ligne 13
                        #   1     2     3    4      5     6     7     8     9    10    11    12    13    14    15    16    17    18    19    20    21    22    23    24    25    26    27
                        [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],    
        ]
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
        for index in range(0, nb_joueur):
            player = Player(self)
            self.players.append(player)
            self.all_players.add(player)

    def update(self, screen):
        # update rock
        for rock in self.all_rocks:
            screen.blit(rock.image, rock.rect)
        # update les joueurs
        for player in self.players:
            screen.blit(player.image, player.rect)