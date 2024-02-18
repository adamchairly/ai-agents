import numpy as np

from objects.food import Food
from objects.snake import Snake
from data.config import *

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.positions)

        self.score = 0
        self.over = False

    def step(self, action):

        game_over, reward = self.snake.move(action)
        self.over = game_over

        if self.snake.get_head_position() == self.food.position:
            reward += 10
            self.snake.length += 1
            self.score += 1
            self.food.randomize_position(self.snake.positions)

        return reward, self.over, self.score

    def draw(self, surface):
        self.snake.draw(surface)
        self.food.draw(surface)

    def reset(self):
        self.score = 0
        self.over = False
        self.snake.reset()
        self.food.reset()

    def get_state(self):

        head_x, head_y = self.snake.get_head_position()
        point_left = (head_x - BLOCK_SIZE, head_y)
        point_right = (head_x + BLOCK_SIZE, head_y)
        point_up = (head_x, head_y - BLOCK_SIZE)
        point_down = (head_x, head_y + BLOCK_SIZE)

        danger_left = (point_left in self.snake.positions or point_left[0] <= 0)
        danger_right = (point_right in self.snake.positions or point_right[0] >= SCREEN_WIDTH)
        danger_up = (point_up in self.snake.positions or point_up[1] <= 0)
        danger_down = (point_down in self.snake.positions or point_down[1] >= SCREEN_HEIGHT)

        # [left, right, up, down]
        direction_left = self.snake.direction == LEFT
        direction_right = self.snake.direction == RIGHT
        direction_up = self.snake.direction == UP
        direction_down = self.snake.direction == DOWN

        food_left = self.food.position[0] < head_x
        food_right = self.food.position[0] > head_x
        food_up = self.food.position[1] < head_y
        food_down = self.food.position[1] > head_y

        state = [
            int(danger_left), int(danger_right), int(danger_up), int(danger_down),
            int(direction_left), int(direction_right), int(direction_up), int(direction_down),
            int(food_left), int(food_right), int(food_up), int(food_down)
        ]

        return np.array(state, dtype=int)