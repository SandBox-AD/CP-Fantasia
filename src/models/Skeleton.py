from src.models.Entity import Entity


class Skeleton(Entity):
    def __init__(self, x, y):
        super().__init__("player_sprite_sheet.png", x, y)

    def update(self):
        # Logique de mise à jour du joueur
        pass

    def draw(self, screen):
        screen.blit(self.sprite_sheet, self.rect)
