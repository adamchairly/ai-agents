from ..objects.food import Food
from ..objects.snake import Snake


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

        self.over = False

    def step(self):
        self.snake.move()

        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.snake.score += 1
            self.food.randomize_position()

    def draw(self, surface):
        self.snake.draw(surface)
        self.food.draw(surface)
