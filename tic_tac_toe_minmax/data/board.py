class Board:

    def __init__(self, board_size):
        self.tiles = self.initialize_board(board_size)
        self.player = 'X'
        self.board_size = board_size
        self.win_conditions = self.generate_win_conditions()

    def initialize_board(self, board_size):
        return [[" " for _ in range(board_size)] for _ in range(board_size)]

    def generate_win_conditions(self):
        conditions = []

        for i in range(self.board_size):
            conditions.append([(i, j) for j in range(self.board_size)])
            conditions.append([(j, i) for j in range(self.board_size)])

        # Diagonals
        conditions.append([(i, i) for i in range(self.board_size)])
        conditions.append([(i, self.board_size - 1 - i) for i in range(self.board_size)])

        return conditions

    def check_win(self, player):
        for condition in self.win_conditions:
            if all(self.tiles[row][col] == player for row, col in condition):
                return True, condition
        return False, None

    def check_tie(self):
        return all(self.tiles[row][col] != " " for row in range(3) for col in range(3))

    def switch_player(self):
        self.player = "X" if self.player == "O" else "O"

    def get_possible_moves(self):
        return [(row, col) for row in range(3) for col in range(3) if self.tiles[row][col] == " "]

    def make_move(self, move):
        new_board = Board(self.board_size)
        new_board.tiles = [row[:] for row in self.tiles]
        new_board.player = self.player

        if new_board.tiles[move[0]][move[1]] == " ":
            new_board.tiles[move[0]][move[1]] = self.player
            new_board.switch_player()
        else:
            raise ValueError("Move not allowed.")

        return new_board

    def reset(self):
        self.tiles = self.initialize_board(self.board_size)
        self.player = 'X'
