from models.Entity import Entity


class Player(Entity):
    def __init__(self, x, y):
        super().__init__("./assets/image/doc.png", x, y)

    def update(self):
        # Logique de mise à jour du joueur
        pass

    def draw(self, screen):
        screen.blit(self.sprite_sheet, self.rect)
