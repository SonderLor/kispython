import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Chaos:
    def __init__(self, mu, state):
        self.mu = mu
        self.state = state
        self.stabilize()

    def next(self):
        pass

    def stabilize(self):
        for _ in range(1000):
            self.next()


class LogisticMap(Chaos):
    def next(self):
        self.state = self.mu * self.state * (1 - self.state)
        return self.state


if __name__ == "__main__":
    logistic_system = LogisticMap(4.0, 0.1)
    values = [logistic_system.next() for _ in range(100000)]
    sns.histplot(values, bins=30, kde=True)
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.title('Гистограмма распределения псевдослучайной величины LogisticMap при mu=4')
    plt.show()

