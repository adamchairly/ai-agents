import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


class Plotter:
    def __init__(self):
        self.episode_scores = []

    def plot_scores(self):
        plt.style.use('classic')

        plt.scatter(range(len(self.episode_scores)), self.episode_scores, s=10, color='black')
        plt.plot(np.convolve(self.episode_scores, np.ones(250) / 250, mode='same'), color='blue', linewidth=2)

        plt.xlabel('Iteration')
        plt.ylabel('Score')

        plt.grid(True, color='lightgrey', linestyle='-', linewidth=1)
        plt.gca().set_facecolor('whitesmoke')

        plt.show()
