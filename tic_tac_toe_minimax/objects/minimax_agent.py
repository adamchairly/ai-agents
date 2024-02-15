class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def minimax(self, board, depth, maximizing_player):
        if depth == 0 or board.check_win('X')[0] or board.check_win('O')[0] or board.check_tie():
            return self.evaluate(board)

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in board.get_possible_moves():
                new_board = board.make_move(move)
                value = self.minimax(new_board, depth - 1, False)[0]
                if value > max_eval:
                    max_eval = value
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in board.get_possible_moves():
                new_board = board.make_move(move)
                value = self.minimax(new_board, depth - 1, True)[0]
                if value < min_eval:
                    min_eval = value
                    best_move = move
            return min_eval, best_move

    def evaluate(self, board):
        if board.check_win('X')[0]:
            return -1, None
        elif board.check_win('O')[0]:
            return 1, None
        else:
            return 0, None

    def find_best_move(self, board):
        _, best_move = self.minimax(board, self.depth, True)  # computer is maximizing
        return best_move
