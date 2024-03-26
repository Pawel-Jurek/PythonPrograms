import unittest

from tictactoe import *
X = "X"
O = "O"
EMPTY = None
board1 = [[X, X, X],
          [O, O, EMPTY],
          [EMPTY, EMPTY, EMPTY]]

board2 = [[X, O, X],
          [O, O, EMPTY],
          [EMPTY, X, EMPTY]]

class TestSum(unittest.TestCase):
    def test_player_function(self):
        result = player(board1)
        self.assertEqual(result, O)
        result = player(board2)
        self.assertEqual(result, X)

if __name__ == '__main__':
    unittest.main()