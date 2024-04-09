import numpy as np
import matplotlib.pyplot as plt


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
    mu_values = np.linspace(1.0, 4.0, 100)
    states = list()
    for mu in mu_values:
        x = 0.5
        logistic_system = LogisticMap(mu, x)
        logistic_system.stabilize()
        states.append(logistic_system.next())
    plt.scatter(mu_values, states, s=0.5)
    plt.xlabel('Параметр бифуркации (mu)')
    plt.ylabel('Состояние системы')
    plt.title('Диаграмма бифуркаций логистического отображения')
    plt.show()
