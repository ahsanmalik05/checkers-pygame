import pygame
import os
from Spritesheet import *

ROWS = 8
COLS = 8
WIDTH, HEIGHT = 800, 800

BOARD_IMG = pygame.image.load(os.path.join('assets/boards', 'board_plain_03.png'))
SCALE_FACT = HEIGHT/BOARD_IMG.get_height()
STARTER_POINT = (7*SCALE_FACT, 7*SCALE_FACT)
BOARD_IMG = pygame.transform.scale(BOARD_IMG, (800, 800))
SPRITE = SpriteSheet("assets/checkers_topDown.png", 16, 16, 1, 4, SCALE_FACT)


class Board:

    def __init__(self, screen):
        self.grid = [['black' for i in range(COLS)] for j in range(ROWS)]
        self.grid[7][1] = 'white'
        self.screen = screen

    def draw(self):
        self.screen.blit(BOARD_IMG, BOARD_IMG.get_rect())
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 'white':
                    self.screen.blit(SPRITE.sprites[0], (STARTER_POINT[0] + 16*SCALE_FACT*col,
                                                         STARTER_POINT[1] + 16*SCALE_FACT*row), SPRITE.sprites[0].get_rect())
                elif self.grid[row][col] == 'black':
                    self.screen.blit(SPRITE.sprites[2], (STARTER_POINT[0] + 16 * SCALE_FACT * col,
                                                         STARTER_POINT[1] + 16 * SCALE_FACT * row),
                                     SPRITE.sprites[1].get_rect())



    def make_move(self, row, col) -> bool:
        """
        Assume selected tile is
        return true if made
        """
        if self.selected_tile:
            player = self.grid[self.selected_tile[0]][self.selected_tile[1]]
            if (abs(self.selected_tile[0]-row)+abs(self.selected_tile[1]-col)) == 4:
                self.grid[self.selected_tile[0]][self.selected_tile[1]] = 0

                if (row > self.selected_tile[0],col > self.selected_tile[0]):
                    self.grid[self.selected_tile[0]+1][self.selected_tile[1]+1] = 0

                elif (row > self.selected_tile[0],col < self.selected_tile[0]):
                    self.grid[self.selected_tile[0]+1][self.selected_tile[1]-1] = 0

                elif (row < self.selected_tile[0],col > self.selected_tile[0]):
                    self.grid[self.selected_tile[0]-1][self.selected_tile[1]+1] = 0

                elif (row < self.selected_tile[0],col < self.selected_tile[0]):
                    self.grid[self.selected_tile[0]-1][self.selected_tile[1]-1] = 0

            self.grid[self.selected_tile[0]][self.selected_tile[1]] = player

            return True






        pass

