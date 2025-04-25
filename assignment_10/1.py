import random

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens():
    board = [-1] * 8
    for row in range(8):
        cols = list(range(8))
        random.shuffle(cols)
        for col in cols:
            if is_safe(board, row, col):
                board[row] = col
                break
    return board

solution = solve_n_queens()
print("Queens are placed at columns:", solution)
