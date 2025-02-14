import pygame
from Spritesheet import *
import os

ROWS = 8
COLS = 8
WIDTH, HEIGHT = 800, 800

BOARD_IMG = pygame.image.load(os.path.join('assets/boards', 'board_plain_03.png'))
SCALE_FACT = HEIGHT/BOARD_IMG.get_height()
PIXEL_SIZE = 16*SCALE_FACT
STARTER_POINT = (7*SCALE_FACT, 7*SCALE_FACT)
BOARD_IMG = pygame.transform.scale(BOARD_IMG, (800, 800))
SPRITE = SpriteSheet("assets/checkers_topDown.png", 16, 16, 1, 4, SCALE_FACT)
PLAYER_IMGS = {
    'white_unselected': SPRITE.sprites[0],
    'white_selected': SPRITE.sprites[1],
    'black_unselected': SPRITE.sprites[2],
    'black_selected': SPRITE.sprites[3]
}
BORDER_OFFSET = 7*SCALE_FACT
SELECT_FILL = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE), pygame.SRCALPHA)
SELECT_FILL.fill((0, 255, 0, 50))
