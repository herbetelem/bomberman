import pygame

# créer la classe game qui vas gerer les parties
class Game:
    
    def __init__(self, nb_joueur):
        # definir si le jeu a commencer ou pas
        self.is_playing = False
        # créer la liste des joueurs
        self.players = []
        # créer le groupe de joueur
        self.all_players = pygame.sprite.Group()
        # generer les joueurs
        for index in range(0, nb_joueur):
            # player = Player(self)
            # self.players.append(player)
            # self.all_players.add(self.player)
            pass