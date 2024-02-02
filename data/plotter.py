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
        plt.plot(np.convolve(self.episode_scores, np.ones(200) / 200, mode='same'), color='blue', linewidth=2)

        # Set the labels for the axes
        plt.xlabel('Iteration')
        plt.ylabel('Score')

        # Enable grid with a light grey color
        plt.grid(True, color='lightgrey', linestyle='-', linewidth=1)
        # Set the face (background) color of the axes
        plt.gca().set_facecolor('whitesmoke')

        plt.show()
