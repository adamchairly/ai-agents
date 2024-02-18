import torch
import random
import numpy as np

from snake_dqn.data.config import *
from collections import deque
from snake_dqn.dqn.model import Linear_QNet, QTrainer

MAX_MEMORY = 100000
BATCH_SIZE = 1000
LR = 0.001


class DQNAgent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = Linear_QNet(12, 256, 4)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

        self.current_action_index = 0

    def get_state(self, game):

        head_x, head_y = game.snake.get_head_position()
        point_left = (head_x - BLOCK_SIZE, head_y)
        point_right = (head_x + BLOCK_SIZE, head_y)
        point_up = (head_x, head_y - BLOCK_SIZE)
        point_down = (head_x, head_y + BLOCK_SIZE)

        danger_left = (point_left in game.snake.positions or point_left[0] <= 0)
        danger_right = (point_right in game.snake.positions or point_right[0] >= SCREEN_WIDTH)
        danger_up = (point_up in game.snake.positions or point_up[1] <= 0)
        danger_down = (point_down in game.snake.positions or point_down[1] >= SCREEN_HEIGHT)

        # [left, right, up, down]
        direction_left = game.snake.direction == LEFT
        direction_right = game.snake.direction == RIGHT
        direction_up = game.snake.direction == UP
        direction_down = game.snake.direction == DOWN

        food_left = game.food.position[0] < head_x
        food_right = game.food.position[0] > head_x
        food_up = game.food.position[1] < head_y
        food_down = game.food.position[1] > head_y

        state = [
            int(danger_left), int(danger_right), int(danger_up), int(danger_down),
            int(direction_left), int(direction_right), int(direction_up), int(direction_down),
            int(food_left), int(food_right), int(food_up), int(food_down)
        ]

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state, episode_number):
        self.epsilon = 100 - episode_number
        final_move = [0, 0, 0, 0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 3)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move

    def decay_epsilon(self):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)