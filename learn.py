from data.game import Game
from data.q_table import QTable
from data.config import *

game = Game(WIDTH, HEIGHT)
q = QTable(BIN_SIZE_X, BIN_SIZE_Y, BIN_VELOCITY, 2, 0.2, 1.0, -1.0)


def run():
    episode_number = 8000

    for i in range(episode_number):
        game.reset()
        episode_reward, episode_score = run_episode(i)
        game.info.episode_scores.append(episode_score)
        q.decay_epsilon()

    q.save('q_table.npy')
    game.info.plot_scores()


def run_episode():
    episode_reward = 0

    while not game.over:
        state = game.get_closest_pipe()
        discretized_state = q.discretize_state(state[0], state[1], state[2])

        action = q.select_action(discretized_state)
        if action == 1:
            game.flap()

        game.update()

        new_state = game.get_closest_pipe()
        discretized_new_state = q.discretize_state(new_state[0], new_state[1], new_state[2])

        reward = game.get_reward()
        episode_reward += reward

        q.update(discretized_state, action, reward, discretized_new_state)

    episode_score = game.bird.point

    return episode_reward, episode_score


run()
