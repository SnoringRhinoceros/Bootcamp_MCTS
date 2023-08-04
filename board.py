
class Board:
    def __init__(self, values=[num for num in range(1, 10)]):
        self.row_size = 3
        self.column_size = 3
        self.values = values
        self.legal_moves = [num for num in self.values if str(num).isdigit()]
        self.winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.winner = None
        self.current_player_turn = self.get_whose_turn()
        
    def update(self, location, letter):
        self.legal_moves.pop(self.legal_moves.index(location))
        self.values[location-1] = letter
        if self.current_player_turn == "X":
            self.current_player_turn = "O"
        else:
            self.current_player_turn = "X"
        
    def show(self):
        # print(self.values)
        current_value_index = 0
        for column in range(self.column_size):
            for row in range(self.row_size):
                print(self.values[current_value_index], end='')
                if row != self.row_size-1:
                    print('|', end='')
                current_value_index += 1
            if column != self.column_size-1:
                print('\n-+-+-')
            else:
                print('\n')
                
    def get_whose_turn(self):
        player_move_count = {}
        for value in self.values:
            if not str(value).isdigit():
                if value not in player_move_count.keys():
                    player_move_count[value] = 1
                else:
                    player_move_count[value] += 1
        if player_move_count:
            if len(player_move_count) == 1:
                return "O"
            elif player_move_count["X"] == player_move_count["O"]:
                return "X"
            return min(player_move_count, key=player_move_count.get)
        return "X"
    
    def check_finished(self):
        for combination in self.winning_combinations:
            if self.values[combination[0]] == self.values[combination[1]] == self.values[combination[2]]:
                self.winner = self.values[combination[0]]
                return True
        
        if not self.legal_moves:
            return True
                
        return False