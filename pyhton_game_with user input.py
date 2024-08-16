def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    # Define the win conditions: rows, columns, diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]

    # Check if any win condition is satisfied
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    game_running = True

    while game_running:
        display_board(board)
        try:
            choice = int(input(f"Player {current_player}, make your choice [1-9]: "))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 9.")
            continue

        if choice < 1 or choice > 9:
            print("Invalid choice! Please select a number between 1 and 9.")
            continue

        # Convert the choice to board index
        index = choice - 1

        if board[index] in "XO":
            print("That spot is already taken. Choose another.")
            continue

        # Place the player's marker
        board[index] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            game_running = False
        elif all(spot in "XO" for spot in board):
            display_board(board)
            print("It's a tie!")
            game_running = False
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"

# Start the game
tic_tac_toe()

