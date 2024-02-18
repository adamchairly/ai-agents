import pygame
from data.game import Game
from snake_dqn.dqn.agent import DQNAgent
from dqn.helper import plot

from data.config import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake: DQN")
clock = pygame.time.Clock()

EPISODE_NUMBER = 500


def train(agent, game):
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    episode_number = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        state_old = agent.get_state(game)

        final_move = agent.get_action(state_old, episode_number)

        reward, done, score = game.step(final_move)
        state_new = agent.get_state(game)

        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        agent.remember(state_old, final_move, reward, state_new, done)

        screen.fill(BACKGROUND_COLOR)
        game.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

            print('Game', agent.n_games, 'Score', score, 'Record:', record, 'Epsilon:', agent.epsilon)

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)
            episode_number += 1


if __name__ == '__main__':
    agent = DQNAgent()
    snake_game = Game()

    train(agent, snake_game)
