
from node import Node

class Tree:
    def __init__(self, board):
        self.root = Node(None, board)
    
    def add_move(self, old_node, new_move, player_letter):
        new_node = Node(old_node, old_node.board)
        new_node.board.update(new_move, player_letter)
        old_node.children.append(new_node)
    
    def add_node(self, old_node, new_node):
        new_node.parent = old_node
        old_node.children.append(new_node)
    
    def remove_node(self, node):
        node.parent.children.pop(node.parent.children.index(node))
        del node
     
    def expand_node(self, node):
        if len(node.children) == 0:
            for move in node.board.legal_moves:
                self.add_move(node, move, node.board.get_whose_turn())