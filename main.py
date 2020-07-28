import pygame

pygame.init()


# generer la fenetre du jeu
pygame.display.set_caption("Bomberman Homemade")
screen = pygame.display.set_mode((1920, 1080))
icon_32x32 = pygame.image.load("assets/favicon.png").convert_alpha()
pygame.display.set_icon(icon_32x32)

# importer et charger le background
background = pygame.image.load('assets/bg.jpg')
background = pygame.transform.scale(background, (1920, 1080))

# importer la bannier
banner = pygame.image.load('assets/bg_nav.png')
banner = pygame.transform.scale(banner, (1920, 1080))

# importer les boutons nav
button_2 = pygame.image.load('assets/button_player_2.png')
button_3 = pygame.image.load('assets/button_player_3.png')
button_4 = pygame.image.load('assets/button_player_4.png')
button_2 = pygame.transform.scale(button_2, (400, 180))
button_3 = pygame.transform.scale(button_3, (400, 180))
button_4 = pygame.transform.scale(button_4, (400, 180))

# importer les shadows des boutons nav
button_2_shadow = pygame.image.load('assets/button_player_shadow.png')
button_3_shadow = pygame.image.load('assets/button_player_shadow.png')
button_4_shadow = pygame.image.load('assets/button_player_shadow.png')
button_2_shadow = pygame.transform.scale(button_2_shadow, (400, 180))
button_3_shadow = pygame.transform.scale(button_3_shadow, (400, 180))
button_4_shadow = pygame.transform.scale(button_4_shadow, (400, 180))

# créer les rect des boutons
button_2_rect = button_2.get_rect()
button_3_rect = button_3.get_rect()
button_4_rect = button_4.get_rect()
button_2_rect.x = 1400
button_3_rect.x = 1400
button_4_rect.x = 1400
button_2_rect.y = 400
button_3_rect.y = 600
button_4_rect.y = 800


# le jeux est en cour
running = True
# nombre de joueur dans la parti
nb_joueur = 0
# une parti est en cour
game_status = False

# boucle tant que running est vrai
while running:
    
    # appliquer le background
    screen.blit(background, (0, 0))
    
    # si la parti n''est pas lancé
    if game_status == False:
        
        # appliquer la banniere
        screen.blit(banner, (0, 0))
        
        # appliquer les boutons
        screen.blit(button_2, (1400, 400))
        screen.blit(button_3, (1400, 600))
        screen.blit(button_4, (1400, 800))
        
    # update le screen
    pygame.display.flip()
    
    # pour chaque event qui arrive
    for event in pygame.event.get():
        
        # check que l'event est le fait de fermer la fenetre
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