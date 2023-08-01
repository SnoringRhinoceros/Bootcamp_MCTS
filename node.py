
class Node:
    def __init__(self, parent, board):
        self.parent = parent
        self.board = board
        self.children = []
        self.visit_count = 0
        self.win_score = 0
        