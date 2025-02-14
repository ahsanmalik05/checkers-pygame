from load_assets import *


class Piece:

    def __init__(self, row, col, team, screen):
        self.row = row
        self.col = col
        self.team = team
        self.screen = screen
        self.upgraded = False

    def get_pos(self):
        return (self.row, self.col)

    def update_pos(self, row, col):
        self.row, self.col = row, col

    def draw(self, selected=False):
        key = self.team + "_" + ("selected" if selected else "unselected")
        self.screen.blit(PLAYER_IMGS[key],
                         (STARTER_POINT[0] + 16 * SCALE_FACT * self.col,
                          STARTER_POINT[1] + 16 * SCALE_FACT * self.row),
                         PLAYER_IMGS[key].get_rect())

    def upgrade(self):
        """
        upgrades the currrent piece to be a king
        """
        self.upgraded = True

    def move(self, row, col):
        self.row, self.col = row, col