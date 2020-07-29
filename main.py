# coding: utf-8

# IMPORT
from math import ceil
import pygame

# Code additionel
from game import Game


# Initialise Pygame
pygame.init()


# Générer la fenetre du jeu
pygame.display.set_caption("Bomberman Homemade")
# Créer la surface d'affichage (En 16/9 !) (1920*1080 OK) (1366*768 OK)
screen = pygame.display.set_mode((1366, 768))
# Charge la Favicon
icon_32x32 = pygame.image.load("assets/favicon.png").convert_alpha()
# Applique la Favicon
pygame.display.set_icon(icon_32x32)

# Importer et charger le background
# background = pygame.image.load('assets/bg.jpg')
# background = pygame.transform.scale(background, screen.get_size())

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
# button_2_shadow = pygame.image.load('assets/button_player_shadow.png')
# button_3_shadow = pygame.image.load('assets/button_player_shadow.png')
# button_4_shadow = pygame.image.load('assets/button_player_shadow.png')
# button_2_shadow = pygame.transform.scale(button_2_shadow, (400, 180))
# button_3_shadow = pygame.transform.scale(button_3_shadow, (400, 180))
# button_4_shadow = pygame.transform.scale(button_4_shadow, (400, 180))

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

# Boucle tant que running est vrai
while running:
    
    # Si la partie n'est pas lancée
    if game_status == False:
        
        # Appliquer la banniere
        screen.blit(banner, (0, 0))
        
        # Appliquer les boutons
        screen.blit(button_2, (ceil(screen.get_width() / 1.4), ceil(screen.get_height() / 2.8)))
        screen.blit(button_3, (ceil(screen.get_width() / 1.4), ceil(screen.get_height() / 1.76)))
        screen.blit(button_4, (ceil(screen.get_width() / 1.4), ceil(screen.get_height() / 1.3)))

        
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
                game = Game(nb_joueur, screen)
                # Charge les rochers
                game.screen_update(screen)
