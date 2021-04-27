import unittest
import tictactoe
from win_checker import Win_Checker

class Win_Checker_Test(unittest.TestCase):
    def test_NoWinnerEmptyBoard(self):
        win_checker = Win_Checker()
        board = []
        for i in range(3):
            tmpBoard = []
            tmpBoard.append('_')
            tmpBoard.append('_')
            tmpBoard.append('_')
            board.append(tmpBoard)

        self.assertEqual(False, win_checker.has_winner(board))

    def test_HorizontalWinner(self):
        win_checker = Win_Checker()

        board = []
        for i in range(3):
            tmpBoard = []
            tmpBoard.append('_')
            tmpBoard.append('_')
            tmpBoard.append('_')
            board.append(tmpBoard)

        board[0][0] = 'X'
        board[0][1] = 'X'
        board[0][2] = 'X'

        self.assertEqual(True, win_checker.has_winner(board))

    def test_VerticalWinner(self):
        win_checker = Win_Checker()

        board = []
        for i in range(3):
            tmpBoard = []
            tmpBoard.append('_')
            tmpBoard.append('_')
            tmpBoard.append('_')
            board.append(tmpBoard)

        board[0][0] = 'X'
        board[1][0] = 'X'
        board[2][0] = 'X'

        self.assertEqual(True, win_checker.has_winner(board))

    def test_DiagonalWinner(self):
        win_checker = Win_Checker()

        board = []
        for i in range(3):
            tmpBoard = []
            tmpBoard.append('_')
            tmpBoard.append('_')
            tmpBoard.append('_')
            board.append(tmpBoard)

        board[0][0] = 'X'
        board[1][1] = 'X'
        board[2][2] = 'X'

        self.assertEqual(True, win_checker.has_winner(board))

    def test_NoWinnerTie(self):
        win_checker = Win_Checker()

        board = []
        for i in range(3):
            tmpBoard = []
            tmpBoard.append('_')
            tmpBoard.append('_')
            tmpBoard.append('_')
            board.append(tmpBoard)

        board[0][0] = 'X'
        board[0][1] = 'O'
        board[0][2] = 'X'
        board[1][0] = 'X'
        board[1][1] = 'O'
        board[1][2] = 'O'
        board[2][0] = 'O'
        board[2][1] = 'X'
        board[2][2] = 'O'

        self.assertEqual(False, win_checker.has_winner(board))


if __name__ == '__main__':
    unittest.main()