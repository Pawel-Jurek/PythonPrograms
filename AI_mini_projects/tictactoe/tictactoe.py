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

def get_winner_from_matrix_rows(board):
    diagonal1 = set()
    diagonal2 = set()
    for i, row in enumerate(board):
        values = set(row)
        if len(values) == 1 and EMPTY not in values:
            return values.pop()
        diagonal1.add(board[i][i])
        diagonal2.add(board[2-i][i])

    if len(diagonal1) == 1 and EMPTY not in diagonal1:
        return diagonal1.pop()
    elif len(diagonal2) == 1 and EMPTY not in diagonal2:
        return diagonal2.pop()
    else:
        return None
    
def winner(board):
    res1 = get_winner_from_matrix_rows(board)
    if res1:
        return res1
    else:
        new_board = pd.DataFrame(board).T.values.tolist()
        return get_winner_from_matrix_rows(new_board)


def terminal(board):
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    winner_sign = winner(board)
    return 1 if winner_sign == X else -1 if winner_sign == O else 0
    

def minimax(board):
    if terminal(board):
        return None
    
    if player(board) == X:
        best_val = float('-inf')
        best_move = None
        alpha = float('-inf')
        for action in actions(board):
            value = min_value(result(board, action), alpha, float('inf'))
            if value > best_val:
                if value == 1:
                    return action
                best_val = value
                best_move = action
            alpha = max(alpha, value)
        return best_move
    else:
        best_val = float('inf')
        best_move = None
        beta = float('inf')
        for action in actions(board):
            value = max_value(result(board, action), float('-inf'), beta)
            if value < best_val:
                if value == -1:
                    return action
                best_val = value
                best_move = action
            beta = min(beta, value)
        return best_move

def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    value = float('-inf')
    for action in actions(board):
        value = max(value, min_value(result(board, action), alpha, beta))
        if value >= beta:
            return value
        alpha = max(alpha, value)
    return value

def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    value = float('inf')
    for action in actions(board):
        value = min(value, max_value(result(board, action), alpha, beta))
        if value <= alpha:
            return value
        beta = min(beta, value)
    return value


