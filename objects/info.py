import pygame


class Info:

    def __init__(self, points, vel, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.points = points
        self.font = pygame.font.SysFont('Arial', 30)

    def update(self, points):
        self.points = points

    def draw(self, screen):
        text = self.font.render(f'Score: {self.points}', True, (0, 0, 0))
        screen.blit(text, (0, 0))
