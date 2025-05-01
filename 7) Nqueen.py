def is_safe(board, row, col):
    for i in range(row):
        # Check if the column is safe and the diagonals are safe
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board, n)
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(board, row + 1, n):
                return True
            board[row] = -1  # Backtrack
    return False

def print_board(board, n):
    for i in range(n):
        row = ['Q' if j == board[i] else '.' for j in range(n)]
        print(' '.join(row))
    print()

def n_queens(n):
    board = [-1] * n  # Initialize the board with -1
    if not solve_n_queens(board, 0, n):
        print("No solution exists")

# User input for N
n = int(input("Enter the value of N for N-Queens: "))
n_queens(n)
