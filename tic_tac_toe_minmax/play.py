import sys
import argparse
from objects.game import Game


def run(board_size, depth):
    game = Game(board_size=board_size, depth=depth)
    game.run()
    sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--board_size', type=int, default=3)
    parser.add_argument('--depth', type=int, default=9)

    args = parser.parse_args()

    run(board_size=args.board_size, depth=args.depth)
