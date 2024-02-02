from data.plotter import Plotter
from objects.pipe import PipeController
from objects.bird import Bird
from objects.background import Background
from objects.info import Info


class Game:
    def __init__(self, screen_width, screen_height, learn=True):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.learn = learn

        self.background = Background(screen_width, screen_height)
        self.pipes = PipeController(screen_width, screen_height)
        self.bird = Bird(screen_width / 3, screen_height / 3)
        self.plotter = Plotter()
        self.over = False

        if not learn:
            self.info = Info(0, 0, screen_width, screen_height)

    def flap(self):
        self.bird.flap()

    def update(self):
        if not self.over:
            self.pipes.update()
            self.bird.update()

            if self.check_collision():
                self.over = True
            self.check_point()

            if not self.learn:
                self.info.update(self.bird.point)

    def draw(self, screen):
        self.background.draw_background(screen)
        self.pipes.draw(screen)
        self.background.draw_base(screen)
        self.bird.draw(screen)

        if not self.learn:
            self.info.draw(screen)

    def check_point(self):
        for pipe in self.pipes.pipes:
            if pipe.bottom_x + pipe.width < self.bird.x and not pipe.passed:
                self.bird.point += 1
                self.bird.point_to_add += 1
                pipe.passed = True

    def check_collision(self):
        bird_rect = self.bird.get_rect()
        for pipe in self.pipes.pipes:
            bottom_rect, top_rect = pipe.get_rects()

            if bird_rect.colliderect(bottom_rect) or bird_rect.colliderect(top_rect):
                for pip in self.pipes.pipes:
                    pip.can_move = False
                return True

        if bird_rect.colliderect(self.background.get_rect()):
            return True

        if self.bird.y <= 0:
            return True

        return False

    def get_closest_pipe(self):
        best_dist_x = 10000
        best_dist_y = 0
        vel = self.bird.acceleration
        for pipe in self.pipes.pipes:
            if best_dist_x > pipe.bottom_x + pipe.width - self.bird.x > 0:
                best_dist_x = pipe.bottom_x + pipe.width - self.bird.x
                best_dist_y = pipe.bottom_y - self.bird.y

        return best_dist_x, best_dist_y, vel

    def reset(self):
        self.background = Background(self.screen_width, self.screen_height)
        self.pipes = PipeController(self.screen_width, self.screen_height)
        self.bird = Bird(self.screen_width / 3, self.screen_height / 3)
        self.over = False

        if not self.learn:
            self.info = Info(0, 0, self.screen_width, self.screen_height)

    def get_reward(self):
        reward = 0
        if self.over:
            reward -= 1000
        else:
            reward += self.bird.point_to_add * 100
            self.bird.point_to_add = 0

        return reward
