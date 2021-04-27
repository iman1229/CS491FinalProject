class Win_Checker(object):

    def has_winner(self, board):

        for i in range(3):
            if board[i][i] != '_':
                if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                    return True
                elif board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                    return True
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1]!='_':
            return True
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1]!='_':
            return True
        else:
            return False
