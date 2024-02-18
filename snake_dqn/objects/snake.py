import pygame
import random

from data.config import *


class Snake:
    def __init__(self):
        self.length = 3
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.positions = None
        self.reset()

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            self.reset()
        else:
            self.direction = point

    def move(self, action):

        if action == [1, 0, 0, 0]:
            self.direction = LEFT
        elif action == [0, 1, 0, 0]:
            self.direction = RIGHT
        elif action == [0, 0, 1, 0]:
            self.direction = UP
        elif action == [0, 0, 0, 1]:
            self.direction = DOWN

        cur = self.get_head_position()
        x, y = self.direction

        new = (cur[0] + (x * BLOCK_SIZE), cur[1] + (y * BLOCK_SIZE))

        if 0 <= new[0] < SCREEN_WIDTH and 0 <= new[1] < SCREEN_HEIGHT:
            if new in self.positions:
                return True, -10
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()
        else:
            return True, -10

        return False, 0

    def reset(self):
        self.length = 3
        self.score = 0
        self.reset_pos()

    def draw(self, surface):
        for index, p in enumerate(self.positions):
            if index == 0:
                head_color = (255, 255, 0)
                r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(surface, head_color, r)
            else:
                body_color = SNAKE_COLOR
                r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(surface, body_color, r)
                pygame.draw.rect(surface, (255, 255, 255), r, 1)

    def reset_pos(self):
        x, y = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        if self.direction == UP:
            self.positions = [(x, y - i * BLOCK_SIZE) for i in range(self.length)]
        elif self.direction == DOWN:
            self.positions = [(x, y + i * BLOCK_SIZE) for i in range(-self.length + 1, 1)]
        elif self.direction == LEFT:
            self.positions = [(x - i * BLOCK_SIZE, y) for i in range(self.length)]
        elif self.direction == RIGHT:
            self.positions = [(x + i * BLOCK_SIZE, y) for i in range(-self.length + 1, 1)]


        self.positions.reverse()

    def get_direction(self):
        if self.direction == LEFT:
            return [1, 0, 0, 0]
        elif self.direction == RIGHT:
            return [0, 1, 0, 0]
        elif self.direction == UP:
            return [0, 0, 1, 0]
        elif self.direction == DOWN:
            return [0, 0, 0, 1]