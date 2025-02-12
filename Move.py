class Move:

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def get_row(self) -> int:
        return self.row

    def get_col(self) -> int:
        return self.col
