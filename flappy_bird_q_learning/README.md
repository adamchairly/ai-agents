# Flappy: Q-learning

This project is made as an experiment with Q-learning in a relatively simple environment; in the world of Flappy Bird.

The dependencies of the project are `pygame`, `numpy` and optionally `matplotlib` for plotting the results of a learning period.

The goal was to implement the algorithm in practice and potentially improve on the works I discovered in Github; previous experiments by [Cihan](https://github.com/chncyhn/flappybird-qlearning-bot) and [SarvagyaVaish](https://sarvagyavaish.github.io/FlappyBirdRL/).

## Flappy Bird environment

- The state-space consist of:
  - Vertical distance from lower pipe
  - Horizontal distance from next pair of pipes
  - Velocity of the bird
  
- The reward function I used to evaluate an action taken in a state is the following:
  - -1000,  if the bird dies
  - +15,  if the bird passes through a pipe
  
- Given the extensive range of possible values for each state variable, I have implemented a discretization.
- Each state is discretized into 10 bins.
- Given this discretization strategy, the state-space consist of only $10^3$ states.
  

<p align="center">
  <img src=res/readme/play.gif alt="Play" width="45%">
</p>


# Results

- I've run several training sessions, and found, that with a relatively low $\alpha$ (0.2), and high $\gamma$ (0.99), the agent is able to converge *fast*, in about 500 episodes.
- Given, that the state-space is relatively small, I kept $\epsilon$ (the exploration factor) at 0, because I found, that even at really low values (1e-10), the agent performs significantly worse.
- Below is the result of 1000 training episodes, where after 600 episodes the agent averaged above 60000 points per 250 episode. 
- The maximum score was limited to 100000 to keep the running time reasonable. (It was ~9 hours)
- The trained table is available at data/trained.npy
<p align="center">
  <img src=res/readme/result.png alt="Play" width="85%">

</p>


# Running the Application

This project can be executed with customizable parameters via command-line arguments using pythons argparser.

Below are the available options:

| Command            | Description                                                 |
|--------------------|-------------------------------------------------------------|
| `--alpha`          | Learning rate. Default is 0.2.                              |
| `--gamma`          | Discount factor. Default is 0.99.                           |
| `--epsilon`        | Exploration factor. Default is -1.0 (disabled).             |
| `--episode_number` | Number of episodes for training. Default is 1000.           |
| `--plotting`       | Enables result plotting post-training.                      |
| `--frame_skip`     | Frames to skip before screen update. Default is 1000.       |
| `--q_table`        | Path to pre-trained Q-table. Default is 'data/trained.npy'. |

To run a learning session, execute

```
python learn.py
```
To customize parameters, include them as follows:
```
python learn.py --alpha 0.1 --gamma 0.95 --epsilon 0.01 --episode_number 500 --plotting True 
```


To run a playing session with graphical interface, execute

```
python play.py
```
To customize parameters, include them as follows:
```
python play.py --frame_skip 1000 --q_table data/trained.npy
```
# Credits

[Cihan](https://github.com/chncyhn/flappybird-qlearning-bot)

[SarvagyaVaish](https://sarvagyavaish.github.io/FlappyBirdRL/)

[Zhenchao Jin](https://github.com/CharlesPikachu/AIGames/tree/master)
