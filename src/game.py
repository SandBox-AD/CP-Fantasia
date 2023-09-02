import pygame

from models.Player import Player


class Game:
    """
    Classe Game pour gérer la logique globale du jeu.

    Cette classe gère la fenêtre Pygame, la boucle de jeu principale et la
    logique
    globale du jeu, telle que la gestion des niveaux, des collisions, des
    événements, etc.

    Attributes:
        running (bool): Indique si le jeu est en cours d'exécution.
        screen (pygame.Surface): La surface de la fenêtre de jeu.
        clock (pygame.time.Clock): L'horloge pour gérer la fréquence d'images.

    Methods:
        initialize: Initialise la fenêtre Pygame et les paramètres du jeu.
        run: Exécute la boucle de jeu principale.
    """

    def __init__(self):
        self.running = False
        self.screen = None
        self.clock = None

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fantasia")

        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(0, 0)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Mettre ici la logique de jeu (
            # gestion des niveaux, collisions, etc.)

            self.screen.fill((0, 0, 0))

            # Mettre ici le code pour dessiner les éléments du jeu
            self.player.update()
            self.player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
