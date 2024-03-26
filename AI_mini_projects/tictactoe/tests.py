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

board3 = [[X, O, X],
          [O, O, X],
          [O, X, X]]

class PlayerFunctionTest(unittest.TestCase):
    def test_moreX(self):
        result = player(board1)
        self.assertEqual(result, O)

    def test_equalOandX(self):
        result = player(board2)
        self.assertEqual(result, X)

class ActionsFunctionTest(unittest.TestCase):
    def test_board1(self):
        result = actions(board1)
        self.assertEqual(result, {(2,1),(0,2),(1,2),(2,2)})

    def test_board2(self):
        result = actions(board2)
        self.assertEqual(result, {(2,1),(0,2),(2,2)})

    def test_board3(self):
        result = actions(board3)
        self.assertEqual(result, set())

if __name__ == '__main__':
    unittest.main()