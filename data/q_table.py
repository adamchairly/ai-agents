import numpy as np
import random


class QTable:
    def __init__(self, num_states_x, num_states_y, num_states_vel, num_actions, alpha, gamma, epsilon):
        self.num_states_x = num_states_x
        self.num_states_y = num_states_y
        self.num_states_vel = num_states_vel
        self.num_actions = num_actions

        self.min_epsilon = 0.000000001
        self.decay_rate = 0.9998395890030878
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        self.table = np.zeros([num_states_x, num_states_y, num_states_vel, num_actions])

    def get_q_value(self, state, action):
        return self.table[state[0], state[1], state[2], action]

    def update(self, state, action, reward, next_state):

        current_q = self.table[state[0], state[1], state[2], action]
        max_future_q = np.max(self.table[next_state[0], next_state[1],  next_state[2], :])

        new_q = (1 - self.alpha) * current_q + self.alpha * (reward + self.gamma * max_future_q)

        self.table[state[0], state[1], state[2], action] = new_q

    def select_action(self, flattened_state):
        if random.uniform(0, 1) < self.epsilon:
            choice = random.choice([0, 1])
            return choice
        else:
            action = np.argmax(self.table[flattened_state[0], flattened_state[1], flattened_state[2]])
            return action

    def discretize_state(self, dist_x, dist_y, vel):

        dist_x = self.discretize_value(dist_x, 0, 240, 10)
        # [480 - gap / 2 (160/2) - bird.height][3 * screen_width / 4]
        dist_y = self.discretize_value(dist_y, -366, 480, 10)
        vel = self.discretize_value(vel, -5, 5, 30)

        return dist_x, dist_y, vel

    def discretize_value(self, value, min_value, max_value, num_bins):

        total_range = max_value - min_value

        bin_size = total_range / num_bins

        bin_index = int((value - min_value) / bin_size)
        bin_index = min(max(bin_index, 0), num_bins - 1)

        return bin_index

    def decay_epsilon(self):
        self.epsilon *= self.decay_rate
        self.epsilon = max(self.epsilon, self.min_epsilon)

    def save(self, filename="data/q_table.npy"):
        try:
            np.save(filename, self.table)
            print(f"Q-table saved to {filename}")
        except Exception as e:
            print(f"Error saving Q-table: {e}")

    def load(self, filename="data/q_table.npy"):
        try:
            self.table = np.load(filename)
            print(f"Loaded Q-table from {filename}")
        except IOError:
            print(f"No existing Q-table found at {filename}, starting fresh.")

