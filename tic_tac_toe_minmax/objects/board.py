import pygame

win_conditions = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]


class Board:
    x_img = pygame.image.load('res/x.png')
    o_img = pygame.image.load('res/o.png')

    def __init__(self):
        self.tiles = self.initialize_board()
        self.player = 'X'

    def initialize_board(self):
        return [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self, window):
        width, height = window.get_size()
        window.fill((255, 255, 255))

        for i in range(1, 3):
            pygame.draw.line(window, (0, 0, 0), (0, i * height // 3), (width, i * height // 3))
            pygame.draw.line(window, (0, 0, 0), (i * width // 3, 0), (i * width // 3, height))
        for row in range(3):
            for col in range(3):
                cell_top_left_x = col * width // 3
                cell_top_left_y = row * height // 3
                if self.tiles[row][col] == 'X':
                    window.blit(self.x_img, (cell_top_left_x, cell_top_left_y))
                elif self.tiles[row][col] == 'O':
                    window.blit(self.o_img, (cell_top_left_x, cell_top_left_y))

    def check_win(self):
        for condition in win_conditions:
            if all(self.tiles[row][col] == self.player for row, col in condition):
                return True
        return False

    def check_tie(self):
        return all(self.tiles[row][col] != " " for row in range(3) for col in range(3))

    def switch_player(self):
        self.player = "X" if self.player == "O" else "O"
