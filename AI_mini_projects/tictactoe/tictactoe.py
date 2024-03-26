"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_quantity = 0
    o_quantity = 0
    for row in board:
        x_quantity += row.count(X)
        o_quantity += row.count(O)
    return O if x_quantity > o_quantity else X


def actions(board):
    possible_actions = set()
    for y, row in enumerate(board):
        for x, state in enumerate(row):
            if (state == EMPTY):
                possible_actions.add(x, y)
    return possible_actions


def result(board, action):
    if board[action[1], action[0]] != EMPTY:
        raise Exception("WrongPositionError")
    board_copy = copy.deepcopy(board)
    board_copy[action[1]][action[0]] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
