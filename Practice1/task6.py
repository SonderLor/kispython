import math


def f(x: int) -> int:
    if x == 0:
        return 3
    return math.sin(f(x - 1)) - 1 / 16 * f(x - 1) ** 3


def main():
    print(f(8))


if __name__ == "__main__":
    main()
