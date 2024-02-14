import pygame
import os

class Info:

    def __init__(self, points, vel, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.points = points

        self.digit_images = {}
        for digit in range(10):
            image_path = os.path.join('res', 'font', f'{digit}.png')
            self.digit_images[str(digit)] = pygame.image.load(image_path)

    def update(self, points):
        self.points = points

    def draw(self, screen):
        score_str = f'{self.points}'
        num_digits = len(score_str)
        x_offset = self.screen_width / 2 - num_digits * self.digit_images['0'].get_width() / 2
        y_offset = self.screen_height * 0.125
        for digit in score_str:
            screen.blit(self.digit_images[digit], (x_offset, y_offset))
            x_offset += self.digit_images[digit].get_width()
