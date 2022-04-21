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
            self.matrix = [[False for x in range(self.size_x)] for y in range(self.size_y)]

    def get_cell(self, x: int, y: int) -> bool:
        return self.matrix[x][y]

    def set_cell(self, x: int, y: int, value: bool):
        self.matrix[x][y] = value

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y

    def next_status(self):
        matrix_snapshot = self.matrix_deep_copy()

        for x in range(self.size_x):
            for y in range(self.size_y):
                num_of_neighbours = self.get_num_of_alive_neighbours(matrix_snapshot, x, y)
                # TODO: refactor with underpopulation_rule
                if num_of_neighbours < 2:
                    self.matrix[x][y] = False
                if num_of_neighbours > 3:
                    self.matrix[x][y] = False

    def matrix_deep_copy(self) -> List[List[bool]]:

        matrix_snapshot = [[False for x in range(self.size_x)] for y in range(self.size_y)]

        for x in range(self.size_x):
            for y in range(self.size_y):
                matrix_snapshot[x][y] = self.matrix[x][y]

        return matrix_snapshot

    def get_num_of_alive_neighbours(self, matrix_snapshot, x, y):
        num_of_neighbours = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if self._neighbours_x_y_is_on_range(x + i, y + j) and self._neighbours_x_y_is_not_itself(i, j):
                    if matrix_snapshot[x + i][y + j]:
                        num_of_neighbours += 1
        return num_of_neighbours

    def _neighbours_x_y_is_on_range(self, n_x, n_y) -> bool:
        return 0 <= n_x < self.size_x and 0 <= n_y < self.size_y

    @staticmethod
    def _neighbours_x_y_is_not_itself(i, j) -> bool:
        return not(i == 0 and j == 0)
