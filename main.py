# coding: utf-8

# IMPORT
from math import ceil
import random
import pygame

# Code additionel
from game import Game


# Initialise Pygame
pygame.init()
# Initialise Font
pygame.font.init()


# Générer la fenetre du jeu
pygame.display.set_caption("Bomberman Homemade")
# Créer la surface d'affichage (En 16/9 !) (1920*1080 OK) (1366*768 OK)
screen = pygame.display.set_mode((1350, 725))
# Charge la Favicon
icon_32x32 = pygame.image.load("assets/favicon.png").convert_alpha()
# Applique la Favicon
pygame.display.set_icon(icon_32x32)

# Choisis la police d'écriture
font = pygame.font.SysFont('Bahnschrift', 30)
replay_text = font.render("Replay", True, (255, 255, 255))

# importer la bannier
banner = pygame.image.load('assets/bg_nav.png')
banner = pygame.transform.scale(banner, screen.get_size())

# importer les boutons nav
button_2 = pygame.image.load('assets/button_player_2.png')
button_3 = pygame.image.load('assets/button_player_3.png')
button_4 = pygame.image.load('assets/button_player_4.png')
# Change la taille des boutons pour
button_2 = pygame.transform.scale(button_2, (ceil(screen.get_width() / 5.5), ceil(screen.get_height() / 6)))
button_3 = pygame.transform.scale(button_3, (ceil(screen.get_width() / 5.5), ceil(screen.get_height() / 6)))
button_4 = pygame.transform.scale(button_4, (ceil(screen.get_width() / 5.5), ceil(screen.get_height() / 6)))

# Importer les shadows des boutons nav
button_2_shadow = pygame.image.load('assets/button_player_shadow.png')
button_3_shadow = pygame.image.load('assets/button_player_shadow.png')
button_4_shadow = pygame.image.load('assets/button_player_shadow.png')
button_2_shadow = pygame.transform.scale(button_2_shadow, (ceil(screen.get_width() / 5.5), ceil(screen.get_height() / 6)))
button_3_shadow = pygame.transform.scale(button_3_shadow, (ceil(screen.get_width() / 5.5), ceil(screen.get_height() / 6)))
button_4_shadow = pygame.transform.scale(button_4_shadow, (ceil(screen.get_width() / 5.5), ceil(screen.get_height() / 6)))

# Créer les rect des boutons
button_2_rect = button_2.get_rect()
button_3_rect = button_3.get_rect()
button_4_rect = button_4.get_rect()
button_2_rect.x = ceil(screen.get_width() / 1.4)
button_3_rect.x = ceil(screen.get_width() / 1.4)
button_4_rect.x = ceil(screen.get_width() / 1.4)
button_2_rect.y = ceil(screen.get_height() / 2.8)
button_3_rect.y = ceil(screen.get_height() / 1.76)
button_4_rect.y = ceil(screen.get_height() / 1.3)


# le jeux est en cours
running = True
# Nombre de joueur dans la partie
nb_joueur = 0
# Une partie est en cour
game_status = False
# la musique nav est lancé
music_nav = False
# la musique game est lancé
music_game = False
# la musique win est lancé
music_win = False
# la musique lost est lancé
music_lost = False
# Fin de partie
end_game_win = False
end_game_lost = False

# Créer le bouton replay
button_replay = pygame.draw.rect(screen, (74, 85, 102), (630, 645, 110, 50))

# créer la liste pour la manette
joysticks = []

# créer les mannette
for index in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(index))
    joysticks[-1].init()

# Boucle tant que running est vrai
while running:
    
    # Si la partie n'est pas lancée
    if game_status == False and not music_win and not music_lost:

        # Appliquer la banniere
        screen.blit(banner, (0, 0))
        
        # Appliquer les ombres des boutons
        screen.blit(button_2_shadow, (ceil(screen.get_width() / 1.4 - 5), ceil(screen.get_height() / 2.8 + 5)))
        screen.blit(button_3_shadow, (ceil(screen.get_width() / 1.4 - 5), ceil(screen.get_height() / 1.76 + 5)))
        screen.blit(button_4_shadow, (ceil(screen.get_width() / 1.4 - 5), ceil(screen.get_height() / 1.3 + 5)))
        # Appliquer les boutons
        screen.blit(button_2, (ceil(screen.get_width() / 1.4), ceil(screen.get_height() / 2.8)))
        screen.blit(button_3, (ceil(screen.get_width() / 1.4), ceil(screen.get_height() / 1.76)))
        screen.blit(button_4, (ceil(screen.get_width() / 1.4), ceil(screen.get_height() / 1.3)))

        if music_nav == False:
            pygame.mixer.init()
            pygame.mixer.music.load("assets/sounds/nav.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.01)
            music_nav = True
    # si la parti est lancée
    elif game_status:
        # Stoper la musique du nav
        if music_nav:
            pygame.mixer.music.stop()
            music_nav = False
            pygame.mixer.music.load("assets/sounds/game.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.01)
        
        # Refresh l'affichage
        game.update(screen)

        # Conditions de victoire
        if len(game.all_players) == 1 or game.timer <= 0:
            # Stop la musique du jeu
            music_game = False
            pygame.mixer.music.stop()
            # Stop la partie
            game_status = False

            if len(game.all_players) == 1:
                # Déclare la fin de partie
                end_game_win = True
            elif game.timer <= 0:
                # Déclare la fin de partie
                end_game_lost = True


    if end_game_win and not music_win and not music_lost:
        # Un seul joueur restant et la musique de victoire n'est pas lancée
        music_win = True
        # Choisis une musique en random
        victory_sounds = ["assets/sounds/victory.logg", "assets/sounds/victory_2.ogg"]
        victory_sound = random.choice(victory_sounds)
        pygame.mixer.music.load(victory_sound)
        # Lance la musique
        pygame.mixer.music.play()
        # Régle le son de la musique
        if victory_sound == "assets/sounds/victory_2.ogg":
            pygame.mixer.music.set_volume(0.15)
        else:
            pygame.mixer.music.set_volume(0.06)
        # Affiche l'écran de victoire
        # Fond noir
        screen.fill((0, 0, 0))
        for player in game.players:
            # Regarde dans la liste de joueur celui qui est vivant
            if player.alive():
                # Le joueur est vivant, récupére son image
                winner = player.image
        # Affiche l'avatar du gagnant
        screen.blit(winner, (screen.get_width() / 2.1, screen.get_height() / 2.1))
        # Affiche le bouton replay
        pygame.draw.rect(screen, (74, 85, 102), (620, 645, 110, 50))
        screen.blit(replay_text, (630, 650))

    elif end_game_lost and not music_lost and not music_win:
        # Le timer est arrivé à 0 et la musique de defaite n'est pas lancée
        # Lance la musique de victoire
        music_lost = True
        pygame.mixer.music.load("assets/sounds/lost.ogg")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.05)
        # Fond noir
        screen.fill((0, 0, 0))
        # Affiche l'écran de défaite
        game_over = pygame.image.load("assets/game_over.jpg")
        screen.blit(game_over, (35, 0))
        # Affiche le bouton replay
        pygame.draw.rect(screen, (74, 85, 102), (620, 645, 110, 50))
        screen.blit(replay_text, (630, 650))


    # Update le screen
    pygame.display.flip()

    # Pour chaque event qui arrive
    for event in pygame.event.get():
        
        # Check que l'event est le fait de fermer la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu ce ferme")
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            # verifier que la souris est appyer au bon endroit
            # si le click est sur un nombre de joueur
            # je lance une game
            # je def le nombre de joueur
            
            if button_2_rect.collidepoint(event.pos):
                game_status = True
                nb_joueur = 2
            elif button_3_rect.collidepoint(event.pos):
                game_status = True
                nb_joueur = 3
            elif button_4_rect.collidepoint(event.pos):
                game_status = True
                nb_joueur = 4
                
            # appliquer le backrgound et créer la game a chaque lancement de parti
            if button_2_rect.collidepoint(event.pos) or button_3_rect.collidepoint(event.pos) or button_4_rect.collidepoint(event.pos):
                # Appliquer le background
                screen.fill((56, 135, 0))
                # Lance la partie avec le nombre de joueurs choisis
                game = Game(nb_joueur)
                # Charge les rochers
                game.update(screen)
            if button_replay.collidepoint(event.pos) and (end_game_lost or end_game_win):
                end_game_win = False
                end_game_lost = False
                music_win = False
                music_lost = False

        if game_status:
            # detecter si un joueur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                # Joueur 1
                if event.key == pygame.K_q:
                    # Le joueur 1 appuis sur A => Pose une bombe
                    game.players[0].drop_bomb()
                # Joueur 2
                elif event.key == pygame.K_u:
                    # Le joueur 2 appuis sur U => Pose une bombe
                    game.players[1].drop_bomb()
                # Joueur 3
                try:
                    if event.key == pygame.K_KP0:
                        # Le joueur 3 appuis sur 0 (Pavé numérique) => Pose une bombe
                        game.players[2].drop_bomb()
                except IndexError:
                    pass
                # Joueur 4
                try:
                    if event.key == pygame.K_SPACE:
                        # Le joueur 4 appuis sur ESPACE => Pose une bombe
                        game.players[3].drop_bomb()
                except IndexError:
                    pass
                else:
                    # Autres touches
                    game.pressed[event.key] = True
        
            # detecter si un joueur lache une touche
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
                
            # detecter la manette
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 4 or event.button == 5:
                    game.players[0].drop_bomb()
            
            if event.type == pygame.JOYHATMOTION:
                if event.value[0] == 1:
                    game.players[0].moove("d")
                if event.value[0] == -1:
                    game.players[0].moove("q")
                if event.value[1] == -1:
                    game.players[0].moove("s")
                if event.value[1] == 1:
                    game.players[0].moove("z")