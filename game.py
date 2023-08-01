
from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.player_x = Player("X")
        self.player_o = Player("O")
        self.players = [self.player_x, self.player_o]
        self.current_player_index = 0
        self.winner = None
        
    def run(self):
        print("Welcome to Tic-Tac-Toe!")
        self.board.show()
        while not self.check_end_con():
            location, letter = self.players[self.current_player_index].choose_move(self.board.legal_moves)
            self.board.update(location, letter)
            self.board.show()
            if self.current_player_index == len(self.players)-1:
                self.current_player_index = 0
            else:
                self.current_player_index += 1
        return
        
    def check_end_con(self):
        if not self.board.legal_moves:
            return True
        
        for combination in self.board.winning_combinations:
            if self.board.values[combination[0]] == self.board.values[combination[1]] == self.board.values[combination[2]]:
                self.winner = self.board.values[combination[0]]
                return True
                
        return False
                

if __name__ == "__main__":
    game = Game()
    game.run()
    if game.winner:
        print(game.winner + " won the game!")
    else:
        print("The game is a tie!")
    print("Thanks for playing!")