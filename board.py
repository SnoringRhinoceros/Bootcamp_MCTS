
class Board:
    def __init__(self):
        self.row_size = 3
        self.column_size = 3
        self.values = [num for num in range(1, self.row_size*self.column_size+1)]
        self.legal_moves = self.values.copy()
        self.winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        
        
    def update(self, location, letter):
        self.legal_moves.pop(self.legal_moves.index(location))
        self.values[location-1] = letter
        
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