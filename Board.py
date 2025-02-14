import pygame
import os

from Piece import *
from Spritesheet import *
from load_assets import *
class Board:

    def __init__(self, screen):
        self.screen = screen
        self.get_start_grid()
        self.grid[4][2] = Piece(4, 2, 'black', self.screen)
        self.selected_tile = None


    def get_start_grid(self):
        self.grid = [[0 for c in range(COLS)] for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                if (r % 2 == c % 2):
                    if r in (0, 1, 2):
                        self.grid[r][c] = Piece(r, c, 'black', self.screen)
                    elif r in (5, 6, 7):
                        self.grid[r][c] = Piece(r, c, 'white', self.screen)

    def draw(self):
        self.screen.blit(BOARD_IMG, BOARD_IMG.get_rect())
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] != 0:
                    if (self.selected_tile is not None and
                            self.selected_tile != 0 and
                            self.selected_tile.get_pos() == (row, col)):
                        self.grid[row][col].draw(selected=True)
                    else:
                        self.grid[row][col].draw()

    def select(self, x, y, player):
        """
        select a tile
        """
        if x < BORDER_OFFSET or x >= WIDTH - BORDER_OFFSET:
            self.selected_tile = None
            return
        if y < BORDER_OFFSET or y >= HEIGHT - BORDER_OFFSET:
            self.selected_tile = None
            return

        col = int((x - BORDER_OFFSET) // PIXEL_SIZE)
        row = int((y - BORDER_OFFSET) // PIXEL_SIZE)

        if self.selected_tile and self.selected_tile != 0:
            temp = self.get_legal_moves(*self.selected_tile.get_pos(), self.selected_tile.team, self.selected_tile.upgraded)
            print(temp)
            if (row, col) in temp and self.selected_tile.team == player:
                self.make_move(row, col)
                self.selected_tile = None
            else:
                self.selected_tile = self.grid[row][col]
        else:
            self.selected_tile = self.grid[row][col]
    def make_move(self, row, col) -> bool:
        """
        Assume selected tile is
        return true if made
        also take care of king upgrades
        """
        pass

    def get_legal_moves(self, row, col, team, upgraded):
        """
        Find all legal moves of this piece in form of (row, col) and return a list of them
        """
        moves = []
        if upgraded:
            directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        elif team == 'black':
            directions = [(1, 1), (1, -1)]
        elif team == 'white':
            directions = [(-1, -1), (-1, 1)]

        for direction in directions:
            new_r, new_c = (row + direction[0],
                            col + direction[1])
            if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                if self.grid[new_r][new_c] == 0:
                    moves.append((new_r, new_c))
                elif self.grid[new_r][new_c].team != team:
                    kill_r, kill_c = new_r+direction[0], new_c+direction[1]
                    if 0 <= kill_r < ROWS and 0 <= kill_c < COLS:
                        moves.append((kill_r, kill_c))
                        moves.extend(self.get_legal_moves(kill_r, kill_c, team, upgraded))

        return moves
