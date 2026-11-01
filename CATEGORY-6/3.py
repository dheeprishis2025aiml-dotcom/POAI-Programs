import math

board = [" "] * 9

# Display board
def display_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()


# Check winner
def check_winner():
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


# Min-Max algorithm
def minimax(is_maximizing):

    winner = check_winner()

    if winner == "X":
        return 1

    if winner == "O":
        return -1

    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(False)

                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(True)

                board[i] = " "
                best_score = min(best_score, score)

        return best_score


# Find best AI move
def best_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


# Main game
print("TIC-TAC-TOE")
print("AI = X, Human = O")
print("Enter positions from 1 to 9")

while True:
    display_board()

    # AI turn
    ai_move = best_move()

    if ai_move is not None:
        board[ai_move] = "X"
        print("AI chooses:", ai_move + 1)

    if check_winner() == "X":
        display_board()
        print("AI Wins!")
        break

    if " " not in board:
        display_board()
        print("Game Draw!")
        break

    display_board()

    # Human turn
    try:
        human_move = int(input("Enter your move (1-9): ")) - 1

        if human_move < 0 or human_move >= 9 or board[human_move] != " ":
            print("Invalid position! Try again.")
            continue

        board[human_move] = "O"

    except ValueError:
        print("Please enter a valid number.")
        continue

    if check_winner() == "O":
        display_board()
        print("Human Wins!")
        break

    if " " not in board:
        display_board()
        print("Game Draw!")
        break