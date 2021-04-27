import unittest
from square_marker import Square_Marker

class mark_square_test(unittest.TestCase):
    def test_outOfBounds(self):
        #arrange
        board = []
        for i in range(3):
           tmpBoard = []
           tmpBoard.append('_')
           tmpBoard.append('_')
           tmpBoard.append('_')
           board.append(tmpBoard)
        row = 4
        column = 3
        player = 'X'
        marker = Square_Marker()

        #act and assert
        self.assertEqual(False, marker.mark_square(board, column, row, player))
    def test_badPlayer(self):
        #arrange
        board = []
        for i in range(3):
           tmpBoard = []
           tmpBoard.append('_')
           tmpBoard.append('_')
           tmpBoard.append('_')
           board.append(tmpBoard)
        row = 0
        column = 0
        player = 'b'
        marker = Square_Marker()

        #act and assert
        self.assertEqual(False, marker.mark_square(board, column, row, player))
    def test_goodInput(self):
        #arrange
        board = []
        for i in range(3):
           tmpBoard = []
           tmpBoard.append('_')
           tmpBoard.append('_')
           tmpBoard.append('_')
           board.append(tmpBoard)
        row = 0
        column = 0
        player = 'X'
        marker = Square_Marker()

        #act and assert
        self.assertEqual(True, marker.mark_square(board, column, row, player))

if __name__ == '__main__':
    unittest.main()
