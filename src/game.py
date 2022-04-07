from typing import List

class Game(object):
    sizeX: int = 0
    sizeY: int = 0
    matrix: List[List[bool]] = None

    def __init__(self, sizeX: int, sizeY: int = None, initial_matrix: List[List[bool]] = None):
        self.sizeX = sizeX

        # TODO: refactor, add sizeY
        if (sizeY != None):
            self.sizeY = sizeY

        if(initial_matrix):
            self.matrix = initial_matrix.copy()
        else:
            self.matrix = [[False for x in range(sizeX)] for y in range(sizeX)]

    def get_cell(self, x:int , y:int) -> bool:
        return self.matrix[x][y]

    def set_cell(self, x:int, y:int, value:bool):
        self.matrix[x][y] = value

    def get_sizeX(self):
        return self.sizeX

    def get_sizeY(self):
        return self.sizeY


