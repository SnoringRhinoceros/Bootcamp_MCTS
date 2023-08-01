
from node import Node

class Tree:
    def __init__(self, board):
        self.root = Node(None, board)
        
    def add_node(self, old_node, new_node):
        old_node.children.append(new_node)
        