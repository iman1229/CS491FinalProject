import unittest
import tictactoe
from square_marker import Square_Marker
from win_checker import Win_Checker

class Test_Win_Checker_Integration(unittest.TestCase):
    def test_NoWinnerEmptyBoard(self):
        empty_board = tictactoe.Board()
        win = Win_Checker()
        self.assertEqual(False, win.has_winner(empty_board.board))

    def test_HorizontalWinner(self):
        board = tictactoe.Board()
        win = Win_Checker()
        board.board[0][0] = 'X'
        board.board[0][1] = 'X'
        board.board[0][2] = 'X'

        self.assertEqual(True, win.has_winner(board.board))

    def test_VerticalWinner(self):
        board = tictactoe.Board()
        win = Win_Checker()
        board.board[0][0] = 'X'
        board.board[1][0] = 'X'
        board.board[2][0] = 'X'

        self.assertEqual(True, win.has_winner(board.board))

    def test_DiagonalWinner(self):
        board = tictactoe.Board()
        win = Win_Checker()
        board.board[0][0] = 'X'
        board.board[1][1] = 'X'
        board.board[2][2] = 'X'

        self.assertEqual(True, win.has_winner(board.board))

    def test_NoWinnerTie(self):
        board = tictactoe.Board()
        win = Win_Checker()
        board.board[0][0] = 'X'
        board.board[0][1] = 'O'
        board.board[0][2] = 'X'
        board.board[1][0] = 'X'
        board.board[1][1] = 'O'
        board.board[1][2] = 'O'
        board.board[2][0] = 'O'
        board.board[2][1] = 'X'
        board.board[2][2] = 'O'

        self.assertEqual(False, win.has_winner(board.board))
class mark_square_test_integration(unittest.TestCase):
    def test_outOfBounds(self):
        #arrange
        board = tictactoe.Board()
        row = 4
        column = 3
        player = 'X'
        marker = Square_Marker()

        #act and assert
        self.assertEqual(False, marker.mark_square(board.board, column, row, player))
    def test_badPlayer(self):
        #arrange
        board = tictactoe.Board()
        row = 0
        column = 0
        player = 'b'
        marker = Square_Marker()

        #act and assert
        self.assertEqual(False, marker.mark_square(board.board, column, row, player))
    def test_goodInput(self):
        #arrange
        board = tictactoe.Board()
        row = 0
        column = 0
        player = 'X'
        marker = Square_Marker()

        #act and assert
        self.assertEqual(True, marker.mark_square(board.board, column, row, player))


if __name__ == '__main__':
    unittest.main()