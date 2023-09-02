import pygame
from abc import ABC, abstractmethod
from typing import Tuple


class Entity(ABC):
    """
    Classe abstraite pour représenter une entité dans le jeu.

    Attributes:
        sprite_sheet (pygame.Surface): La surface du sprite sheet de l'entité.
        rect (pygame.Rect): Le rectangle de collision de l'entité.

    Methods:
        __init__: Initialise une nouvelle entité avec un sprite sheet et
        des coordonnées.
        update: Méthode abstraite pour mettre à jour le comportement de
        l'entité.
        draw: Méthode abstraite pour dessiner l'entité sur l'écran.
        split_sprites: Découpe le sprite sheet en cellules individuelles.

    Args:
        sprite_sheet_path (str): Le chemin vers le sprite sheet de l'entité.
        x (int): La position horizontale initiale de l'entité.
        y (int): La position verticale initiale de l'entité.
    """

    def __init__(self, sprite_sheet_path: str, x: int, y: int):
        """
        Initialise une nouvelle instance d'entité.

        Args:
            sprite_sheet_path (str): Le chemin vers le sprite sheet de
            l'entité.
            x (int): La position horizontale initiale de l'entité.
            y (int): La position verticale initiale de l'entité.
        """
        self.sprite_sheet = pygame.image.load(sprite_sheet_path)
        self.rect = pygame.Rect(
            x, y, 32, 32
        )  # Rect pour la position et la taille

    @abstractmethod
    def update(self):
        """
        Méthode abstraite pour mettre à jour le comportement de l'entité.
        Cette méthode doit être implémentée par les sous-classes.
        """
        pass

    @abstractmethod
    def draw(self, screen: pygame.Surface):
        """
        Méthode abstraite pour dessiner l'entité sur l'écran.
        Cette méthode doit être implémentée par les sous-classes.

        Args:
            screen (pygame.Surface): La surface de l'écran sur laquelle
            dessiner l'entité.
        """
        pass

    def split_sprites(self, width: int, height: int) -> Tuple[pygame.Surface]:
        """
        Découpe le sprite sheet en cellules individuelles.

        Cette méthode découpe le sprite sheet en cellules individuelles de la
        taille spécifiée
        et renvoie une liste de surfaces pygame représentant chaque cellule.

        Args:
            width (int): Largeur de chaque cellule.
            height (int): Hauteur de chaque cellule.

        Returns:
            Tuple[pygame.Surface]: Tuple de surfaces représentant les cellules
            découpées.
        """
        sprite_width, sprite_height = self.sprite_sheet.get_size()
        sprites = []
        for y in range(0, sprite_height, height):
            for x in range(0, sprite_width, width):
                cell = self.sprite_sheet.subsurface(
                    pygame.Rect(x, y, width, height)
                )
                sprites.append(cell)
        return tuple(sprites)
