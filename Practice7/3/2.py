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
    o = LogisticMap(2, 0.1)
    o.next(), o.next(), o.next()
    print(o.next(), o.next(), o.next())
