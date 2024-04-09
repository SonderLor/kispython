import math
from typing import Callable

import matplotlib.pyplot as plt


def distance1(y: list, z: list) -> float:
    return math.sqrt(sum((yi - zi) ** 2 for yi, zi in zip(y, z)))


def distance2(y: list, z: list) -> float:
    return sum(abs(yi - zi) for yi, zi in zip(y, z))


def distance3(y: list, z: list) -> float:
    m = None
    for yi, zi in zip(y, z):
        if not m or abs(yi - zi) > m:
            m = abs(yi - zi)
    return m


def distance4(y: list, z: list) -> float:
    return sum((yi - zi) ** 2 for yi, zi in zip(y, z))


def distance5(y: list, z: list) -> float:
    h = 5
    return sum(abs(yi - zi) ** h for yi, zi in zip(y, z)) ** (1 / h)


def visualize(distance_metrics: list[Callable], y: list[int], z: list[int], move: float = 1):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = plt.subplots()
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])
    plt.show()


def main() -> None:
    visualize([distance1, distance2, distance3, distance4, distance5],
              [1, 0.5, 1], [0.5, 2, 1], move=0.01)
    visualize([distance1, distance2, distance3, distance4, distance5],
              [1, 0.5, 1], [0.5, 2, 1], move=1.0)
    visualize([distance1, distance2, distance3, distance4, distance5],
              [1, 0.5, 1], [0.5, 2, 1], move=10)


if __name__ == "__main__":
    main()
