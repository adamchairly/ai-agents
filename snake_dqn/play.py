import pygame
import sys

from snake_dqn.data.game import Game
from data.config import *


class Application:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake: DQN")
        self.clock = pygame.time.Clock()

        self.game = Game()

    def run(self):
        while not self.game.over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.game.snake.turn(UP)
                    elif event.key == pygame.K_s:
                        self.game.snake.turn(DOWN)
                    elif event.key == pygame.K_a:
                        self.game.snake.turn(LEFT)
                    elif event.key == pygame.K_d:
                        self.game.snake.turn(RIGHT)

            self.game.step()

            self.screen.fill(BACKGROUND_COLOR)
            self.game.draw(self.screen)
            pygame.display.flip()

            self.clock.tick(FPS)


if __name__ == "__main__":
    app = Application()
    app.run()
