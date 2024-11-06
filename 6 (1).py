def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board, player):
    """Checks if the given player has won the game."""
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        while True:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                break
            else:
                print("Invalid move. Try again.")

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if " " not in [cell for row in board for cell in row]:
            print_board(board)
            print("It's a draw!")
            break

        turn += 1


# Run the game
tic_tac_toe()
