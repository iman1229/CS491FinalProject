#Note: Although the skeleton below is in Python, you may use any programming language you want so long as the language supports object-oriented programming, 
#          and you make use of relevant object-oriented design principles.

from square_marker import Square_Marker
import win_checker

class Board(object):
    
    
    board = []
    

    # Initializes the Board of size 3x3
    def __init__(self):

       self.win_checker = win_checker.Win_Checker()
       self.square_marker = Square_Marker()

       self.board.clear()
       
       for i in range(3):
           tmpBoard = []
           tmpBoard.append('_')
           tmpBoard.append('_')
           tmpBoard.append('_')
           self.board.append(tmpBoard)
           

    def play_game(self):
        
        #Takes moves from raw_input as comma-separated list in form (column, row, player)
        #    and makes a move. When a winner has been determined, the game ends
        #:return: (str) the letter representing the player who won
        lastPlayer = '_'
        counter = 0
        while(not(self.win_checker.has_winner(self.board))):
            print(self.board[0][0] + '|' + self.board[1][0] + '|' + self.board[2][0])
            print(self.board[0][1] + '|' + self.board[1][1] + '|' + self.board[2][1])
            print(self.board[0][2] + '|' + self.board[1][2] + '|' + self.board[2][2])
            
            column=int(input("enter a column: "))
            row = int(input("enter a row: "))
            lastPlayer = input("enter player: ")
            self.square_marker.mark_square(self.board, column, row, lastPlayer)
            
        
        print(self.board[0][0] + '|' + self.board[1][0] + '|' + self.board[2][0])
        print(self.board[0][1] + '|' + self.board[1][1] + '|' + self.board[2][1])
        print(self.board[0][2] + '|' + self.board[1][2] + '|' + self.board[2][2])

        return lastPlayer
        #pass
        
if __name__ == '__main__':
    board = Board()
    winner = board.play_game()
    print("{} has won!".format(winner))
