import math


def main(z: list[float], y: list[float], x: list[float]) -> float:
    result = 0
    n = min(map(len, (z, y, x)))
    for i in range(1, n + 1):
        result += 77 * (88 * z[math.ceil(i / 2) - 1] +
                        y[n - math.ceil(i / 4)] ** 2 +
                        x[i - 1] ** 3) ** 7
    return result


if __name__ == "__main__":
    print(main([-0.69, -0.44, 0.55, 0.98],
               [-0.42, -0.62, -0.71, 0.8],
               [0.33, -0.52, 0.48, 0.78]))
