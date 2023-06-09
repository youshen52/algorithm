def knights_tour(n, start):
    # Initialize the chessboard
    chessboard = [[-1 for _ in range(n)] for _ in range(n)]
    chessboard[start[0]][start[1]] = 0

    # Possible moves for the knight
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    # Recursive helper function
    def knight_tour_helper(chessboard, pos, move_number):
        if move_number == n * n - 1:
            return True

        for move in moves:
            next_row = pos[0] + move[0]
            next_col = pos[1] + move[1]

            if (
                0 <= next_row < n
                and 0 <= next_col < n
                and chessboard[next_row][next_col] == -1
            ):
                chessboard[next_row][next_col] = move_number + 1
                if knight_tour_helper(
                    chessboard, (next_row, next_col), move_number + 1
                ):
                    return True
                chessboard[next_row][next_col] = -1

        return False

    # Start the recursive search
    if knight_tour_helper(chessboard, start, 0):
        return chessboard
    else:
        return None
