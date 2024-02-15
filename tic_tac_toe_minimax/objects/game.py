import pygame
from data.board import Board
from objects.minimax_agent import MinimaxAgent


class Game:
    x_img = pygame.image.load('res/x.png')
    o_img = pygame.image.load('res/o.png')

    def __init__(self, board_size, depth):
        pygame.init()
        self.window_size = 600
        self.window = pygame.display.set_mode((self.window_size, self.window_size))
        pygame.display.set_caption('Tic-tac-toe minimax')

        self.board_size = board_size
        self.cell_size = self.window_size // self.board_size
        self.x_img = pygame.transform.scale(self.x_img, (self.cell_size, self.cell_size))
        self.o_img = pygame.transform.scale(self.o_img, (self.cell_size, self.cell_size))

        self.game_board = Board(board_size)
        self.minimax_agent = MinimaxAgent(depth)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.game_board.reset()
                        continue
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    row = y // self.cell_size
                    col = x // self.cell_size

                    # Player turn
                    if self.game_board.tiles[row][col] == " " and self.game_board.player == 'X':
                        self.game_board.tiles[row][col] = self.game_board.player
                        if not (self.game_board.check_win('X')[0] or self.game_board.check_tie()):
                            self.game_board.switch_player()

                            # Minimax agent's response
                            best_move = self.minimax_agent.find_best_move(self.game_board)
                            if best_move is not None:
                                self.game_board.tiles[best_move[0]][best_move[1]] = self.game_board.player
                                if not (self.game_board.check_win('O')[0] or self.game_board.check_tie()):
                                    self.game_board.switch_player()

            self.draw_board()

            for player in ['X', 'O']:
                win_condition = self.game_board.check_win(player)[1]
                if win_condition:
                    start_pos, end_pos = get_line_start_end(win_condition, self.window_size, self.board_size)
                    pygame.draw.line(self.window, (0, 0, 0), start_pos, end_pos, 10)

            pygame.display.update()

    def draw_board(self):
        width, height = self.window.get_size()
        cell_size = width // self.board_size
        self.window.fill((255, 255, 255))

        for i in range(1, self.board_size):
            pygame.draw.line(self.window, (0, 0, 0), (0, i * cell_size), (width, i * cell_size))
            pygame.draw.line(self.window, (0, 0, 0), (i * cell_size, 0), (i * cell_size, height))

        for row in range(self.board_size):
            for col in range(self.board_size):
                cell_top_left_x = col * cell_size
                cell_top_left_y = row * cell_size
                if self.game_board.tiles[row][col] == 'X':
                    self.window.blit(self.x_img, (cell_top_left_x, cell_top_left_y))
                elif self.game_board.tiles[row][col] == 'O':
                    self.window.blit(self.o_img, (cell_top_left_x, cell_top_left_y))


def get_line_start_end(win_condition, window_size, board_size):
    cell_size = window_size // board_size
    start_row, start_col = win_condition[0]
    end_row, end_col = win_condition[-1]

    start_pos = (start_col * cell_size + cell_size // 2, start_row * cell_size + cell_size // 2)
    end_pos = (end_col * cell_size + cell_size // 2, end_row * cell_size + cell_size // 2)

    return start_pos, end_pos
