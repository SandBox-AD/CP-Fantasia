import os

import pygame
from models.Entity import Entity


class Player(Entity):
    def __init__(self, x, y):
        super().__init__("./assets/image/doc.png", x, y, (16, 19), 0, 13)
        # self.save_sprites()

    def update(self):
        # Logique de mise à jour du joueur
        pass

    def draw(self, screen):
        screen.blit(self.get_sprite(0), self.rect)

    def move(self, dx: int, dy: int):
        """
        Déplace le joueur horizontalement et verticalement.

        Cette méthode permet de déplacer le joueur horizontalement et/ou
        verticalement en fonction des valeurs de `dx` (déplacement horizontal)
        et `dy` (déplacement vertical). Les valeurs positives de `dx` déplacent
        le joueur vers la droite, les valeurs négatives vers la gauche. Les
        valeurs positives de `dy` déplacent le joueur vers le bas, les valeurs
        négatives vers le haut.

        Args:
            dx (int): Le déplacement horizontal (positif vers la droite,
                négatif vers la gauche).
            dy (int): Le déplacement vertical (positif vers le bas,
                négatif vers le haut).
        """
        # Ajoute le déplacement aux coordonnées du joueur
        self.rect.x += dx
        self.rect.y += dy

        # Ici, tu peux ajouter la logique de gestion
        # des collisions ou des limites
        # de l'écran si nécessaire pour empêcher l
        # e joueur de sortir de l'écran.

    def save_sprites(self):
        """
        Enregistre les sprites découpés dans le dossier ./assets/tmp.

        Cette méthode enregistre les cellules du sprite sheet découpé
        dans le dossier ./assets/tmp sous forme de fichiers image individuels.
        Les fichiers seront nommés sprite0.png, sprite1.png, etc.
        """
        if not os.path.exists("./assets/tmp"):
            os.makedirs("./assets/tmp")

        for i, sprite in enumerate(self.sprites):
            file_name = f"./assets/tmp/sprite{i}.png"
            pygame.image.save(sprite, file_name)
            print(f"Sprite enregistré : {file_name}")

        print("Sprites enregistrés dans ./assets/tmp.")
