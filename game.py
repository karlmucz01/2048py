import numpy as np
import random

class Game:
    def __init__(self) -> None:
        self.board = np.zeros((4, 4), dtype=int)
        self.score = 0

    

    def shift(self, direction):
