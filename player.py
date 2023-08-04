
from constants import *
from tree import Tree
import math
import time

class Player:
    def __init__(self, letter, board):
        self.letter = letter
        self.board = board
        
    def UCT_formula(self, node):
        if node.visit_count == 0:
            return float('inf')
        return (node.win_score / node.visit_count) + math.sqrt(2)*math.sqrt(math.log(node.parent.visit_count) / node.visit_count)
    
    def find_best_UCT_node(self, node):
        child_UCB = []
        for child in node.children:
            child_UCB.append(self.UCT_formula(child))
        best_child = max(child_UCB)
        best_child_index = child_UCB.index(best_child)
        return node.children[best_child_index]
        
    def choose_promising_node(self, root_node):
        node = root_node
        while len(node.children) != 0:
            node = self.find_best_UCT_node(node)
        return node
    
    def simulate_random_playout(self, tree, node_to_explore):
        if node_to_explore.board.check_finished() and None != node_to_explore.board.winner != self.letter:
            node_to_explore.parent.win_score = float('-inf')
            return node_to_explore.board.winner
        while not node_to_explore.board.check_finished():
            tree.expand_node(node_to_explore)
            node_to_explore = node_to_explore.get_random_child()
        return node_to_explore.board.winner
    
    def back_propogation(self, node_to_explore, playout):
        temp_node = node_to_explore
        while temp_node:
            temp_node.visit_count += 1
            if self.letter == playout:
                temp_node.win_score += WIN_SCORE
            temp_node = temp_node.parent
    
    def compare_boards(self, old_board, new_board):
        for move in old_board.legal_moves:
            if move not in new_board.legal_moves:
                return move
    
    def choose_best_move(self, board):
        tree = Tree(board)
        tree.expand_node(tree.root)
        timeout_start = time.time()
        while time.time() < timeout_start + END_TIME:
            promising_node = self.choose_promising_node(tree.root)
            if not promising_node.board.check_finished():
                tree.expand_node(promising_node)
            node_to_explore = promising_node
            if promising_node.children:
                node_to_explore = promising_node.get_random_child()
            playout = self.simulate_random_playout(tree, node_to_explore)
            self.back_propogation(node_to_explore, playout)
        
        winner_node = tree.root.get_child_with_max_score()
        result = (self.compare_boards(tree.root.board, winner_node.board), self.letter)
        return result
        