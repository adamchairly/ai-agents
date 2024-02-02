import pygame
import argparse

from data.config import *
from data.game import Game
from data.q_table import QTable


class Application:
    def __init__(self, frame_skip=1000, q_table_path='data/trained.npy'):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy: Q-Learning")

        self.frame_skip = frame_skip
        self.game = Game(WIDTH, HEIGHT)
        self.q = QTable(BIN_SIZE_X, BIN_SIZE_Y, BIN_VELOCITY, 2, 0.2, 0.99, -1.0)
        self.q.load(q_table_path)

    def run(self):
        frame = 0
        while not self.game.over:

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

            if frame % self.frame_skip == 0:
                self.screen.fill((255, 255, 255))
                self.game.draw(self.screen)
                pygame.display.flip()
            frame += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame_skip', type=int, default=1000)
    parser.add_argument('--q_table', type=str, default='data/trained.npy')

    args = parser.parse_args()

    application = Application(frame_skip=args.frame_skip, q_table_path=args.q_table)
    application.run()
