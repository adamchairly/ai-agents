from ..data.config import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, FOOD_COLOR
import random
import pygame
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (SCREEN_WIDTH-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                         random.randint(0, (SCREEN_HEIGHT-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, FOOD_COLOR, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)