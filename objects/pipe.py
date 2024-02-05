import random
import pygame

INITIAL_OFFSET = 34
SPEED = 2
class Pipe:

    pipe_image = pygame.image.load("res/pipe-green.png")

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.width = screen_width / 9
        self.height = screen_height / 2
        self.gap = self.height / 2
        self.distance = screen_width / 2 + self.width
        self.bottom_x, self.bottom_y, self.top_x, self.top_y = self.generate_coords()

        self.passed = False

    def draw(self, window):

        window.blit(self.pipe_image, (self.bottom_x, self.bottom_y))
        top_image = pygame.transform.rotate(self.pipe_image, 180)
        window.blit(top_image, (self.top_x, self.top_y))
        bottom_rect, top_rect = self.get_rects()
        pygame.draw.rect(window, (0, 0, 255), bottom_rect, 2)  # Blue outline for bottom pipe
        pygame.draw.rect(window, (0, 0, 255), top_rect, 2)

    def update(self):
        self.bottom_x -= SPEED
        self.top_x -= SPEED

    def generate_coords(self):
        bottom_x = (self.screen_width / 2 + self.width)
        bottom_y = random.uniform(self.gap + self.width, self.screen_height - self.gap)
        top_y = bottom_y - self.gap - self.height
        top_x = bottom_x

        return bottom_x, bottom_y, top_x, top_y

    def get_rects(self):
        bottom_rect = pygame.Rect(self.bottom_x, self.bottom_y, self.width, self.height)
        top_rect = pygame.Rect(self.top_x, self.top_y, self.width, self.height)
        return bottom_rect, top_rect

    def set_new_position(self, last_pipe_x):
        self.bottom_x = last_pipe_x + self.distance
        self.top_x = self.bottom_x
        self.bottom_y = random.uniform(self.gap + self.width, self.screen_height - self.gap)
        self.top_y = self.bottom_y - self.gap - self.height
        self.passed = False

class PipeController:
    def __init__(self,screen_width, screen_height):
        pipe1 = Pipe(screen_width, screen_height)
        pipe1.set_new_position(INITIAL_OFFSET)
        pipe2 = Pipe(screen_width, screen_height)
        pipe2.set_new_position(pipe1.bottom_x)
        pipe3 = Pipe(screen_width, screen_height)
        pipe3.set_new_position(pipe2.bottom_x)

        self.pipes = [pipe1, pipe2, pipe3]

    def update(self):
        last_pipe_x = max(pipe.bottom_x for pipe in self.pipes)

        for pipe in self.pipes:
            pipe.update()
            if pipe.bottom_x + pipe.width < 0:
                pipe.set_new_position(last_pipe_x)

    def draw(self, window):
        for pipe in self.pipes:
            pipe.draw(window)
