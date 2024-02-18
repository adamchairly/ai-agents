import argparse
import pygame
import torch

from data.game import Game
from dqn.model import Linear_QNet
from data.config import *


def manual_play(game):
    running = True
    while running:
        action = game.snake.get_direction()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    action = [0, 0, 1, 0]
                elif event.key == pygame.K_s:
                    action = [0, 0, 0, 1]
                elif event.key == pygame.K_a:
                    action = [1, 0, 0, 0]
                elif event.key == pygame.K_d:
                    action = [0, 1, 0, 0]
                elif event.key == pygame.K_r:
                    game.reset()

        _, over, _ = game.step(action)
        if over:
            game.reset()
        screen.fill(BACKGROUND_COLOR)
        game.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def trained_play(game, model):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return

        state_old = game.get_state()
        state_old_tensor = torch.tensor(state_old, dtype=torch.float).unsqueeze(0)

        with torch.no_grad():
            prediction = model(state_old_tensor)
            action_idx = torch.argmax(prediction).item()

        action = [0, 0, 0, 0]
        action[action_idx] = 1

        _, over, _ = game.step(action)
        if over:
            game.reset()

        screen.fill(BACKGROUND_COLOR)
        game.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["manual", "trained"], required=True)
    args = parser.parse_args()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake: " + args.mode.capitalize())
    clock = pygame.time.Clock()

    snake_game = Game()

    if args.mode == "trained":
        model = Linear_QNet(12, 256, 4)
        model.load_state_dict(torch.load('model/model.pth'))
        model.eval()
        trained_play(snake_game, model)
    else:
        manual_play(snake_game)
