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


# Alpha-Beta Pruning algorithm
def alpha_beta(board, depth, alpha, beta):

    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if board.turn == chess.WHITE:
        max_eval = float('-inf')

        for move in board.legal_moves:
            board.push(move)

            evaluation = alpha_beta(
                board, depth - 1, alpha, beta
            )

            board.pop()

            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)

            # Pruning condition
            if beta <= alpha:
                break

        return max_eval

    else:
        min_eval = float('inf')

        for move in board.legal_moves:
            board.push(move)

            evaluation = alpha_beta(
                board, depth - 1, alpha, beta
            )

            board.pop()

            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)

            # Pruning condition
            if beta <= alpha:
                break

        return min_eval


# Find best move
def find_best_move(board, depth):
    best_move = None

    if board.turn == chess.WHITE:
        best_score = float('-inf')
        alpha = float('-inf')
        beta = float('inf')

        for move in board.legal_moves:
            board.push(move)

            score = alpha_beta(
                board, depth - 1, alpha, beta
            )

            board.pop()

            if score > best_score:
                best_score = score
                best_move = move

            alpha = max(alpha, best_score)

    else:
        best_score = float('inf')
        alpha = float('-inf')
        beta = float('inf')

        for move in board.legal_moves:
            board.push(move)

            score = alpha_beta(
                board, depth - 1, alpha, beta
            )

            board.pop()

            if score < best_score:
                best_score = score
                best_move = move

            beta = min(beta, best_score)

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