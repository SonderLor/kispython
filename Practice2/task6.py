def distance(y: list, z: list) -> float:
    h = 5
    return sum(abs(yi - zi) ** h for yi, zi in zip(y, z)) ** (1 / h)


def main() -> None:
    print(distance([1, 0.5, 1], [0.5, 2, 1]))


if __name__ == "__main__":
    main()
