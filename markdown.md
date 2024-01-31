
# Flappy: Q-learning

This project is made as an experiment with Q-learning in a relatively simple enviroment; in the world of Flappy Bird.
The dependencies of the project are `pygame`,  `numpy` and optionally `matplotlib` for plotting the results of a learning period.
The goal was to implement the algorithm in practice and potentially improve on the works I discovered in github; previous experiments by [Cihan](https://github.com/chncyhn/flappybird-qlearning-bot) and [SarvagyaVaish](https://sarvagyavaish.github.io/FlappyBirdRL/).

## Q-learning

- Q-learning is a model-free reinforcement learning algorithm, using a Q-table to store quality values to each state-action pair. Q(s, a)
- The Q-value for a particular state-action pair is updated using the formula:
![hehe](https://latex.codecogs.com/png.latex?Q%28s%2C%20a%29%20%3D%20Q%28s%2C%20a%29%20&plus;%20%5Calpha%20%5Cleft%20%5BR%28s%2C%20a%29%20&plus;%20%5Cgamma%20%5Cmax_%7Ba%27%7DQ%28s%27%2Ca%27%29%20-%20Q%28s%2C%20a%29%20%5Cright%20%5D)
- $Q(s, a)$ is the current value
- $R(s,a)$ is the reward for taking action $a$ in state $s$
-  $max_{a'} Q(s', a')$ is the maximum predicted reward achievable in the new state $s'$, considering all possible actions $a'$.
- $\alpha$ is the learning rate, determining how much the new information overrides old information.
- $\gamma$ is the discount factor, determining the importance of future rewards compared to immediate rewards

### Integrating into the Flappy Bird enviroment

- The reward function I used to evaluate an action taken in a state is the following:
$$ R(s, a) = \begin{cases} 
-1000 & \text{if the bird dies}, \\
+15 & \text{if it passes through a pipe} \\
\end{cases}$$
- The state space consist of:
--   Vertical distance from lower pipe
--   Horizontal distance from next pair of pipes
-- Velocity of the bird
- Given the extensive range of possible values for each state variable, I have implemented a discretization. 
- Given this discretization strategy, the state-space consist of only $10^3$ states.
- Each state is discretized into 10 bins.

## Results

- I've ran several training sessions, and found, that with a relatively low $\alpha$ (0.2), and high $\gamma$ (0.99), the agent is able to converge *very fast*, in about 400 episodes.
- To keep the training time low, I've limited the maximum score of a game to 20.000, and after the agent converges, it keeps hitting it almost constantly.
- Given, that the state-space is relatively small, I kept $\epsilon$ at 0, because I found, that even at really low values (1e-10), the agent performs worse.
