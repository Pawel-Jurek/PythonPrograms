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

board4 = [[X, X, O],
          [O, O, X],
          [O, X, X]]

board5 = [[X, O, X],
          [O, X, O],
          [O, X, X]]

board6 = [[O, X, X],
          [O, O, O],
          [O, X, X]]

board7 = [[X, EMPTY, X],
          [O, X, O],
          [EMPTY, O, X]]

board8 = [[X, EMPTY, EMPTY],
          [EMPTY, X, EMPTY],
          [EMPTY, EMPTY, X]]

board9 = [[EMPTY, EMPTY, O],
          [EMPTY, O, EMPTY],
          [O, EMPTY, EMPTY]]

board10 = [[X, O, X],
           [X, O, O],
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
        self.assertEqual(result, {(1,2),(2,0),(2,1),(2,2)})

    def test_board2(self):
        result = actions(board2)
        self.assertEqual(result, {(1,2),(2,0),(2,2)})

    def test_board3(self):
        result = actions(board3)
        self.assertEqual(result, set())


class ResultFunctionTest(unittest.TestCase):
    def test_correctO(self):
        res = result(board1, (2,0))
        self.assertEqual(res,  [[X, X, X],
                                [O, O, EMPTY],
                                [O, EMPTY, EMPTY]])

    def test_correctX(self):
        res = result(board2, (1,2))
        self.assertEqual(res,  [[X, O, X],
                                [O, O, X],
                                [EMPTY, X, EMPTY]])

    def test_incorrectO(self):
        try:
            result(board3, (2,0))
            exception = False
        except:
            exception = True
        finally:
            self.assertTrue(exception)
    
    def test_incorrectX(self):
        try:
            result(board1, (0,0))
            exception = False
        except:
            exception = True
        finally:
            self.assertTrue(exception)


class WinnerFunctionTest(unittest.TestCase):
    def test_winningX1(self):
        result = winner(board1)
        self.assertEqual(result, X)

    def test_no_winner(self):
        result = winner(board2)
        self.assertEqual(result, None)

    def test_winningX2(self):
        result = winner(board3)
        self.assertEqual(result, X)

    def test_winningO1(self):
        result = winner(board4)
        self.assertEqual(result, O)

    def test_winningX3(self):
        result = winner(board5)
        self.assertEqual(result, X)

    def test_winningO2(self):
        result = winner(board6)
        self.assertEqual(result, O)

    def test_winningX4(self):
        result = winner(board7)
        self.assertEqual(result, X)
    
    def test_winningX5(self):
        result = winner(board8)
        self.assertEqual(result, X)

    def test_winningO3(self):
        result = winner(board9)
        self.assertEqual(result, O)


class TerminalFunctionTest(unittest.TestCase):
    def test_end_with_winner(self):
        result = terminal(board1)
        self.assertEqual(result, True)
    
    def test_end_with_winner2(self):
        result = terminal(board9)
        self.assertEqual(result, True)

    def test_end_with_full(self):
        result = terminal(board10)
        self.assertEqual(result, True)

    def test_end_with_moves1(self):
        result = terminal(board2)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()