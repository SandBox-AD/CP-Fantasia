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
        __init__: Initialise une nouvelle entité avec un sprite sheet, des
        coordonnées et un offset.
        update: Méthode abstraite pour mettre à jour le comportement de
        l'entité.
        draw: Méthode abstraite pour dessiner l'entité sur l'écran.
        split_sprites: Découpe le sprite sheet en cellules individuelles.

    Args:
        sprite_sheet_path (str): Le chemin vers le sprite sheet de l'entité.
        x (int): La position horizontale initiale de l'entité.
        y (int): La position verticale initiale de l'entité.
        cell_size (Tuple[int, int]): Les nouvelles dimensions des cellules
        (largeur, hauteur).
        x_offset (int): Le décalage horizontal pour commencer la découpe.
        y_offset (int): Le décalage vertical pour commencer la découpe.
    """

    def __init__(
        self,
        sprite_sheet_path: str,
        x: int,
        y: int,
        cell_size: Tuple[int, int],
        x_offset: int,
        y_offset: int,
    ):
        """
        Initialise une nouvelle instance d'entité.

        Args:
            sprite_sheet_path (str): Le chemin vers le sprite sheet de
            l'entité.
            x (int): La position horizontale initiale de l'entité.
            y (int): La position verticale initiale de l'entité.
            cell_size (Tuple[int, int]): Les nouvelles dimensions des cellules
            (largeur, hauteur).
            x_offset (int): Le décalage horizontal pour commencer la découpe.
            y_offset (int): Le décalage vertical pour commencer la découpe.
        """
        self.sprite_sheet = pygame.image.load(sprite_sheet_path)
        self.rect = pygame.Rect(
            x, y, cell_size[0], cell_size[1]
        )  # Rect pour la position et la taille
        print(
            f"cell_size[0]: {cell_size[0]}, "
            f"cell_size[1]: {cell_size[1]}, "
            f"x_offset: {x_offset}, "
            f"y_offset: {y_offset}"
        )

        self.sprites = self.split_sprites(
            cell_size[0], cell_size[1], x_offset, y_offset
        )

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

    def split_sprites(
        self, width: int, height: int, x_offset: int, y_offset: int
    ) -> Tuple[pygame.Surface]:
        """
        Découpe le sprite sheet en cellules individuelles.

        Cette méthode découpe le sprite sheet en cellules individuelles de la
        taille spécifiée
        et renvoie une liste de surfaces pygame représentant chaque cellule.

        Args:
            width (int): Largeur de chaque cellule.
            height (int): Hauteur de chaque cellule.
            x_offset (int): Décalage horizontal pour commencer la découpe.
            y_offset (int): Décalage vertical pour commencer la découpe.


        Returns:
            Tuple[pygame.Surface]: Tuple de surfaces représentant les cellules
            découpées.
        """
        sprite_width, sprite_height = self.sprite_sheet.get_size()
        sprites = []
        for y in range(y_offset, sprite_height, height):
            for x in range(x_offset, sprite_width, width):
                print(str(x), str(y))
                cell = self.sprite_sheet.subsurface(
                    pygame.Rect(x, y, width, height)
                )
                # Vérifie si la cellule contient au moins un pixel non
                # transparent
                if pygame.mask.from_surface(cell).count() > 0:
                    sprites.append(cell)
        return tuple(sprites)

    def get_sprite(self, index: int) -> pygame.Surface:
        """
        Récupère une cellule spécifique du sprite sheet.

        Cette méthode renvoie une surface pygame représentant une cellule
        spécifique du sprite sheet découpé.

        Args:
            index (int): L'indice de la cellule à récupérer.

        Returns:
            pygame.Surface: Surface représentant la cellule du sprite sheet.
        """
        if 0 <= index < len(self.sprites):
            return self.sprites[index]
        else:
            raise IndexError("Index hors limites")
