def distance(y: list, z: list) -> float:
    return sum((yi - zi) ** 2 for yi, zi in zip(y, z))


def main() -> None:
    print(distance([1, 0.5, 1], [0.5, 2, 1]))


if __name__ == "__main__":
    main()
