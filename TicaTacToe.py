# Min-Max Algorithm for Tic-Tac-Toe

board = [' ' for _ in range(9)]


def print_board():
    print()
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()


def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if (board[combination[0]] == player and
            board[combination[1]] == player and
            board[combination[2]] == player):
            return True

    return False


def is_board_full():
    return ' ' not in board


def minimax(is_maximizing):
    if check_winner('O'):
        return 1

    if check_winner('X'):
        return -1

    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(best_score, score)

        return best_score


def best_move():
    best_score = -float('inf')
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move


print("Tic-Tac-Toe using Min-Max Algorithm")
print("You are X and Computer is O")

while True:
    print_board()

    position = int(input("Enter your position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != ' ':
        print("Invalid move. Try again.")
        continue

    board[position] = 'X'

    if check_winner('X'):
        print_board()
        print("You win!")
        break

    if is_board_full():
        print_board()
        print("It's a draw!")
        break

    computer_move = best_move()
    board[computer_move] = 'O'

    print("Computer chose position:", computer_move + 1)

    if check_winner('O'):
        print_board()
        print("Computer wins!")
        break

    if is_board_full():
        print_board()
        print("It's a draw!")
        break