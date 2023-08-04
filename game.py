
from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.player_x = Player("X", self.board)
        self.player_o = Player("O", self.board)
        self.players = [self.player_x, self.player_o]
        self.current_player_index = 0
        
    def run(self):
        self.board.show()
        while not self.board.check_finished():
            location, letter = self.players[self.current_player_index].choose_best_move(self.board)
            self.board.update(location, letter)
            self.board.show()
            if self.current_player_index == len(self.players)-1:
                self.current_player_index = 0
            else:
                self.current_player_index += 1
        return  

if __name__ == "__main__":
    game = Game()
    game.run()
    if game.board.winner:
        print(game.board.winner + " won the game!")
    else:
        print("The game is a tie!")
    print("Thanks for playing!")