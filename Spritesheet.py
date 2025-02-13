import pygame

class SpriteSheet:

    def __init__(self, filename, piece_width, piece_height, rows, cols, scale=1):
        self.sprite_sheet = pygame.image.load(filename)
        self.piece_width = piece_width
        self.piece_height = piece_height
        self.rows = rows
        self.cols = cols
        self.scale = scale
        self.sprites = self.extract_sprites()


    def extract_sprites(self):
        """Extracts individual pieces from the sprite sheet."""
        sprites = []
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.piece_width
                y = row * self.piece_height
                sprite = pygame.transform.scale(self.sprite_sheet.subsurface(pygame.Rect(x, y, self.piece_width, self.piece_height)), (16*self.scale, 16*self.scale))
                sprites.append(sprite)

        return sprites