import pygame

GRAVITY = 0.2


class Bird:
    bird_up = pygame.image.load("res/yellowbird-upflap.png")
    bird_mid = pygame.image.load("res/yellowbird-midflap.png")
    bird_down = pygame.image.load("res/yellowbird-downflap.png")
    bird_images = [bird_up, bird_mid, bird_down]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 34
        self.height = 34
        self.alive = True
        self.acceleration = 0
        self.max_acceleration = - 5
        self.angle = 0

        self.image_id = 0
        self.increment = 1

        self.point = 0
        self.point_to_add = 0

    def update(self):
        if self.acceleration - GRAVITY < 5:
            self.acceleration += GRAVITY
        self.y += self.acceleration

        self.image_id += self.increment
        if self.image_id >= 2 or self.image_id <= 0:
            self.increment = - self.increment

    def draw(self, window):
        if self.acceleration < 0:
            self.angle = 20
        elif 2 < self.acceleration < 4:
            self.angle = -20
        elif self.acceleration > 4:
            self.angle = -60

        rotated_image = pygame.transform.rotate(self.bird_images[self.image_id],
                                                self.angle)
        window.blit(rotated_image, (self.x, self.y))

        hitbox = self.get_rect()
        pygame.draw.rect(window, (255, 0, 0), hitbox, 2)

    def flap(self):
        if self.acceleration - 3 > - 5:
            self.acceleration -= 3

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
