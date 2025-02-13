from Player import Player
class Move:
    def __init__(self, player, board, row: int, col: int):
        self.row = row
        self.col = col
        self.player = player

    def get_row(self) -> int:
        return self.row

    def get_col(self) -> int:
        return self.col

    def get_player(self):
        return self.player

    def __str__(self):
        return f"{self.player.getName()} placed at ({self.row}, {self.col})"
