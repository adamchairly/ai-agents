import pygame
import sys
from objects.board import Board


def main():
    pygame.init()
    window_size = 600
    window = pygame.display.set_mode((window_size, window_size))
    game_board = Board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                row = y // (window_size // 3)
                col = x // (window_size // 3)
                if game_board.tiles[row][col] == " ":
                    game_board.tiles[row][col] = game_board.player
                    if game_board.check_win() or game_board.check_tie():
                        print("Game Over")
                        running = False
                    else:
                        game_board.switch_player()
        game_board.draw_board(window)
        pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
