class Game(object):
    size: int = 0

    def __init__(self, size: int):
        self.size = size

    def get_size(self) -> int:
        return self.size