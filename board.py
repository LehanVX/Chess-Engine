
class Board:
    def __init__(self):
        self.board = [
                  ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                  ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                  ['.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.', '.', '.', '.'],
                  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                  ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
            ]
        
    def print_board(self):
        print()
        for row_index in range(8) : 
            print(8- row_index, end=" ")
            print (' '.join(self.board[row_index]))
        print("  a b c d e f g h")
        print()

# Black is lowercase. White is uppercase.