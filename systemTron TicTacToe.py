# Tic Tac Toe

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(player):
    # Check rows, columns and diagonals for a win
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]             # diagonals

    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def check_draw():
    return ' ' not in board

def play_game():
    player = 'X'
    while True:
        print_board()
        move = int(input(f"Player {player}, enter your move (1-9): ")) - 1

        if board[move] != ' ':
            print("Invalid move, try again.")
            continue

        board[move] = player

        if check_winner(player):
            print_board()
            print(f"Player {player} wins!")
            break

        if check_draw():
            print_board()
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

play_game()
