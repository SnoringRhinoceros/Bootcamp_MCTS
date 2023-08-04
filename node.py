
import random
from board import Board

class Node:
    def __init__(self, parent, board):
        self.parent = parent
        self.board = Board(values=board.values.copy())
        self.children = []
        self.visit_count = 0
        self.win_score = 0
    
    def get_child_with_max_score(self):
        result = self.children[0]
        for child in self.children:
            if child.win_score > result.win_score:
                result = child
        return result
    
    def get_random_child(self):
        return random.choice(self.children)