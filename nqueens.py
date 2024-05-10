def is_safe(board, row, col):
    # Check if there is a queen in the same row to the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower-left diagonal
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    # Base case: If all queens are placed, return True
    if col == n:
        return True

    # Try placing a queen in each row of the current column
    for i in range(n):
        # Check if it's safe to place a queen in this row and column
        if is_safe(board, i, col):
            # Place the queen and recursively solve for the next column
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, n):
                return True
            # If placing the queen doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If no solution is found, return False
    return False

def print_solution(board):
    # Print the board configuration
    for row in board:
        print(row)

def solve_n_queens(n):
    # Initialize the board as an n x n grid filled with zeros
    board = [[0] * n for _ in range(n)]

    # Call the recursive utility function to solve the N-Queens problem
    if solve_n_queens_util(board, 0, n) == False:
        print("Solution does not exist")
        return False

    # If a solution is found, print the board configuration
    print_solution(board)
    return True

# Call the solve_n_queens function with N=8 to solve the 8-Queens problem
solve_n_queens(4)
