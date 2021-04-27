class Square_Marker:
    def mark_square(self, board, column, row, player):

        if player == 'X' or player == 'O':
            if column >= 0 and column <= 2 and row >= 0 and row <= 2 and board[column][row] == '_':
                board[column][row] = player
                return True
            else:
                print("spot already taken or input out of bounds")
                return False
        else:
            print("invalid player value")
            return False