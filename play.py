import pygame

from data.config import *
from data.game import Game
from data.q_table import QTable


class Application:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy: Q-Learning")
        self.clock = pygame.time.Clock()

        self.game = Game(WIDTH, HEIGHT)
        self.q = QTable(BIN_SIZE_X, BIN_SIZE_Y, BIN_VELOCITY, 2, 0.2, 1.0, -1.0)
        self.q.load('q_table.npy')

    def run(self):
        while not self.game.over:
            self.clock.tick(60)

            state = self.game.get_closest_pipe()
            discretized_state = self.q.discretize_state(state[0], state[1], state[2])

            action = self.q.select_action(discretized_state)
            if action == 1:
                self.game.flap()

            self.game.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game.flap()

            self.screen.fill((255, 255, 255))
            self.game.draw(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    application = Application()
    application.run()
