import chess

# Piece values
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 100
}

# Evaluation function
def evaluate_board(board):
    if board.is_checkmate():
        return -10000 if board.turn == chess.WHITE else 10000

    if board.is_game_over():
        return 0

    score = 0

    for piece_type, value in piece_values.items():
        score += len(board.pieces(piece_type, chess.WHITE)) * value
        score -= len(board.pieces(piece_type, chess.BLACK)) * value

    return score


# Min-Max algorithm
def minimax(board, depth):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if board.turn == chess.WHITE:
        best_score = float('-inf')

        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1)
            board.pop()

            best_score = max(best_score, score)

        return best_score

    else:
        best_score = float('inf')

        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1)
            board.pop()

            best_score = min(best_score, score)

        return best_score


# Find best move
def find_best_move(board, depth):
    best_move = None

    if board.turn == chess.WHITE:
        best_score = float('-inf')

        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1)
            board.pop()

            if score > best_score:
                best_score = score
                best_move = move

    else:
        best_score = float('inf')

        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1)
            board.pop()

            if score < best_score:
                best_score = score
                best_move = move

    return best_move


# Main program
board = chess.Board()

print("Initial Chess Board:")
print(board)

move = find_best_move(board, 2)

print("\nBest Move:", move)

if move:
    board.push(move)

print("\nBoard After AI Move:")
print(board)