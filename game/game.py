# coding: utf-8

# IMPORTS
import pygame
import json

# Code additionnel
from game.map_objects.map_object import Rock
from game.map_objects.map_object import Grass
from game.map_objects.map_object import Banner
from game.player import Player
from game.menu.avatar_menu import Avatar_menu
from game.menu.avatar_bg import Avatar_bg

# créer la classe game qui vas gerer les parties
class Game:
    
    def __init__(self, nb_joueur):
        # definir si le jeu a commencer ou pas
        self.is_playing = False
        # nombre de joueur
        self.nb_joueur = nb_joueur
        # liste des avatars des joueur
        self.avatar_players = [False] * self.nb_joueur
        # definit si les player et la map on été créer
        self.avatar_set = False
        # Choisis la police d'écriture
        self.game_font = pygame.font.SysFont('Bahnschrift', 30)

        # Créer le groupe de sprites
        self.rocks_breakable = pygame.sprite.Group()
        self.rocks_unbreakable = pygame.sprite.Group()
        self.all_grass = pygame.sprite.Group()
        self.all_avatar = pygame.sprite.Group()

        # appel des fonctions qui créeront la map et les joueurs
        # self.create_player()
        # self.create_map()

        # liste des coordonée et nom de chaque avatar du menu
        #                             alex                 alexandre              aurelia                  hadrien                 laura                melanie              guillaume                   wilfried
        self.avatar_menu_axe = [[230, 120, "alex"], [630, 120, "alexandre"], [1030, 120, "aurelia"], [230, 350, "hadrien"], [630, 350, "laura"], [1030, 350, "melanie"], [230, 560, "guillaume"], [630, 560, "wilfried"], [1030, 560, "alex"]]
        for index in range(9):
            avatar_menu = Avatar_menu(self.avatar_menu_axe[index][0], self.avatar_menu_axe[index][1], self.avatar_menu_axe[index][2])
            self.all_avatar.add(avatar_menu)
        # background du menu
        self.avatar_bg = Avatar_bg()

        # créer la librairie de touche
        self.pressed = {}


    # Fonction qui vas appeler a la creation de la map et des joueur
    def call_map_and_timer(self):
        # Tous les avatars sont choisis
        self.avatar_set = True
        # Créer et affiche la map
        self.create_map()

        # TIMER #
        # initialiser le timer
        self.clock = pygame.time.Clock()
        # La limite de temps est de 10 minutes (en ms)
        self.timer = 600000

    # Fonction qui vas créer la map et les joueurs
    def create_player(self):
        # PLAYERS #
        # Créer la liste des joueurs
        self.players = []
        # Créer le groupe de joueur
        self.all_players = pygame.sprite.Group()
        # Générer les joueurs
        # Position joueurs
        #                P1            P2          P3         P4
        player_x_y = [[50, 125], [1250, 625], [1250, 125], [50, 625]]
        # Créer les joueurs
        for index in range(0, (self.nb_joueur)):
            # Génére un joueur en fonction du nombre de joueur
            player = Player(self, player_x_y[index][0], player_x_y[index][1], (index + 1))
            # Ajoute le joueur crée à la liste des joueurs
            self.players.append(player)

    def create_map(self):
        # MAP #
        # Liste des rochers
        self.rock_list = []
        # Charge la map en fonction du nombre de joueurs
        if self.nb_joueur == 2:
            # Map pour 2 joueurs
            with open("assets/map/2_players_map.json", "r") as load:
                self. rock_list = json.loads(load.read())
        elif self.nb_joueur == 3:
            # Map pour 3 joueurs
            with open("assets/map/3_players_map.json", "r") as load:
                self. rock_list = json.loads(load.read())
        elif self.nb_joueur == 4:
            # Map pour 4 joueurs
            with open("assets/map/4_players_map.json", "r") as load:
                self. rock_list = json.loads(load.read())

        # Créer la banniere en fonction du nombre de joueur
        self.banner = Banner(self.nb_joueur)
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


    def update(self, screen):
        """
            Update la position des rochers et des joueurs sur la carte
        """
        
        if self.avatar_set:
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
            for player in self.players:
                self.status_printer(screen, player)
                    

    def avatar_menu_update(self, screen, i):
        """
            Affiche le menu d'avatar en fonction du joueur qui doit sélectionner
        """
        # Refresh le background
        screen.blit(self.avatar_bg.image, self.avatar_bg.rect)
        # Update le menu
        for avatar in self.all_avatar:
            # Affiche les avatars sur le menu
            screen.blit(avatar.image, avatar.rect)
        # Créer le texte
        avatar_choice_text = self.game_font.render(f"Player {i+1} choose an avatar :", True, (255, 255, 255))
        # Affiche le texte
        screen.blit(avatar_choice_text, (500, 0))

    def check_collision(self, sprite, group):
        """
            Vérifie si un joueur entre en colisions
        """

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def status_printer(self, screen, player):
        """
            Affiche le statut du joueur (vivant / nombres de bombes sur la map)
        """

        # Affiche l'avatar du joueur
        screen.blit(player.image, player.status_position_list[0])
        # Affiche le nombre de bombes sur la map
        for index in range(1, len(player.all_bombs) + 1):
            screen.blit(pygame.image.load("assets/bombs/bomb.png"), player.status_position_list[index])
