# Tic-Tac-Toe: Minimax

This project is an exploration of the Minimax algorithm applied to the classic game of Tic-Tac-Toe. 
The only dependency is `pygame`.

## Minimax algorithm

The Minimax algorithm is a decision rule for minimizing the possible loss for a worst-case scenario.\
Great, and in-depth explanation of the algorithm can be found at [Wikipedia](https://en.wikipedia.org/wiki/Minimax).   

In the specific case of a 3x3 Tic-Tac-Toe board, the algorithm theoretically needs to evaluate 9! possible states for the first move.\
With alpha-beta pruning the performance can be improved significantly, however with large state-spaces, the algorithm falls back.

<p align="center">
  <img src=res/tictactoe.gif alt="Play" width="45%">
</p>


# Running the Application

This project can be executed with customizable parameters via command-line arguments using pythons argparser.

Below are the available options:

| Command        | Description                                   |
|----------------|-----------------------------------------------|
| `--board_size` | Board size, by default 3x3.                   |
| ` --depth`     | Depth of the minimax algorithm, by default 9. |

To run the application:

```
python play.py
```
To customize parameters, include them as follows:
```
python learn.py --board_size=4 --depth=9
```

# Credits

[SVGRepo](https://www.svgrepo.com/)
