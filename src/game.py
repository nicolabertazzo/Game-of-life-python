from typing import List


class Game(object):
    size_x: int = 0
    size_y: int = 0
    matrix: List[List[bool]] = None

    def __init__(self, size_x: int, size_y: int = None, initial_matrix: List[List[bool]] = None):
        self.size_x = size_x

        # TODO: refactor, add sizeY
        if size_y is not None:
            self.size_y = size_y
        else:
            self.size_y = size_x

        if initial_matrix:
            self.matrix = initial_matrix.copy()
        else:
            self.matrix = [[False for x in range(size_x)] for y in range(size_x)]

    def get_cell(self, x: int, y: int) -> bool:
        return self.matrix[x][y]

    def set_cell(self, x: int, y: int, value: bool):
        self.matrix[x][y] = value

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y
