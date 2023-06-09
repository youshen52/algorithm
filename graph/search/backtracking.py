def is_valid(board, row, col):
    # Check if a queen can be placed at the given position (row, col)
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_n_queens(n):
    board = [-1] * n  # Initialize an empty chessboard

    def backtrack(row):
        if row == n:
            # All queens have been successfully placed
            # Process and print the solution
            process_solution(board)
            return

        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col  # Place a queen at (row, col)
                backtrack(row + 1)  # Move to the next row
                board[row] = -1  # Remove the queen (backtrack)

    backtrack(0)  # Start with the first row


def process_solution(board):
    # Print the board configuration
    for row in board:
        line = ["."] * len(board)
        line[row] = "Q"
        print(" ".join(line))
    print()


# Example usage
solve_n_queens(4)
