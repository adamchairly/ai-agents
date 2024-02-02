from data.game import Game
from data.q_table import QTable
from data.config import *

game = Game(WIDTH, HEIGHT, True)
q = QTable(BIN_SIZE_X, BIN_SIZE_Y, BIN_VELOCITY, 2, 0.18, 0.99, -1.0)


def run():
    episode_number = 5001

    for i in range(episode_number):
        game.reset()
        _, score = run_episode()
        game.plotter.episode_scores.append(score)
        q.decay_alpha()
        print("Episode {}: Score {} Epsilon: {}".format(i, score, q.epsilon))

    game.plotter.plot_scores()
    q.save('q_table.npy')


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
        if game.bird.point >= 100000:
            game.over = True

    episode_score = game.bird.point

    return episode_reward, episode_score


run()
