
class Player:
    def __init__(self, letter):
        self.letter = letter
        
    def choose_move(self, legal_moves):
        return int(input("What is " + self.letter + "'s move? " + str(legal_moves))), self.letter