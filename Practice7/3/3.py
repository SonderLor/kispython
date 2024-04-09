import graphviz


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


def draw(vertices, edges):
    dot = graphviz.Digraph()
    for v in vertices:
        dot.node(str(v[0]), v[1])
    for e in edges:
        dot.edge(str(e[0]), str(e[1]))
    dot.render('graph3', format='png', cleanup=True)


def visualize(logistic_map: LogisticMap):
    vertices = list()
    edges = list()
    i: int = 1
    for i in range(1, 5):
        vertices.append((i, str(logistic_map.next())))
    for i in range(1, 4):
        edges.append((i, i + 1))
    edges.append((i + 1, 1))
    draw(vertices, edges)


if __name__ == "__main__":
    visualize(LogisticMap(3.5, 0.1))
