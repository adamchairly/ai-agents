import pygame


class Background:

    background_image = pygame.image.load("res/background.png")
    base_image = pygame.image.load("res/base.png")

    def __init__(self, screen_width, screen_height):
        self.base_width = screen_width
        self.base_height = screen_height / 4

        self.background_image = pygame.transform.scale(self.background_image,
                                                       (screen_width, screen_height))
        self.base_image = pygame.transform.scale(self.base_image, (self.base_width, self.base_height))

    def draw_background(self, screen):
        screen.blit(self.background_image, (0, 0))

    def draw_base(self, screen):
        screen.blit(self.base_image, (0, 3 * self.base_height))

        base_hitbox = self.get_rect()  # Get the base's hitbox
        pygame.draw.rect(screen, (0, 255, 0), base_hitbox, 2)

    def get_rect(self):
        return pygame.Rect(0, 3 * self.base_height, self.base_width, self.base_height)
