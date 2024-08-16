def create_board():
    return [' ' for _ in range(9)]

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def is_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)  # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_draw(board):
    return ' ' not in board

def make_move(board, player, position):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

def switch_player(current_player):
    return 'O' if current_player == 'X' else 'X'

def tic_tac_toe():
    board = create_board()
    current_player = 'X'
    
    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")
        
        try:
            position = int(input("Choose a position from 1 to 9: ")) - 1
            if position < 0 or position > 8:
                print("Invalid position. Choose a number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        if not make_move(board, current_player, position):
            print("Position already taken. Choose another position.")
            continue

        if is_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_draw(board):
            display_board(board)
            print("The game is a draw!")
            break

        current_player = switch_player(current_player)

tic_tac_toe()

