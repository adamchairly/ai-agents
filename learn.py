import argparse
from data.game import Game
from data.q_table import QTable
from data.config import *


def run(alpha, gamma, epsilon, episode_number, plotting):

    game = Game(WIDTH, HEIGHT)
    q = QTable(BIN_SIZE_X, BIN_SIZE_Y, BIN_VELOCITY, 2, alpha, gamma, epsilon)

    for i in range(episode_number):
        game.reset()
        score = run_episode(game, q)
        game.plotter.episode_scores.append(score)
        print(f"Episode {i}: Score {score}")

    if plotting:
        game.plotter.plot_scores()
    q.save('data/trained.npy')


def run_episode(game, q):

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

        q.update(discretized_state, action, reward, discretized_new_state)
        if game.bird.point >= 100000:
            game.over = True

    episode_score = game.bird.point

    return episode_score


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--alpha', type=float, default=0.2)
    parser.add_argument('--gamma', type=float, default=0.99)
    parser.add_argument('--epsilon', type=float, default=-1.0)
    parser.add_argument('--episode_number', type=int, default=1001)
    parser.add_argument('--plotting', type=bool, default=True)

    args = parser.parse_args()

    run(args.alpha, args.gamma, args.epsilon, args.episode_number, args.plotting)
