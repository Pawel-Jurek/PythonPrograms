"""
Tic Tac Toe Player
"""

import copy
import math
import pandas as pd

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
                possible_actions.add((y, x))
    return possible_actions


def result(board, action):
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("WrongPositionError")
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy

def get_winner_from_half_matrix(board):
    diagonal = []
    for i, row in enumerate(board):
        values = set(row)
        if len(values) == 1 and EMPTY not in values:
            return values.pop()
        diagonal.append(board[i][i])
    diagonal_set = set(diagonal)
    if len(diagonal_set) == 1 and EMPTY not in diagonal_set:
        return diagonal_set.pop()
    else:
        return None
    
def winner(board):
    res1 = get_winner_from_half_matrix(board)
    if res1:
        return res1
    else:
        new_board = pd.DataFrame(board).T.values.tolist()
        return get_winner_from_half_matrix(new_board)


def terminal(board):
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


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
