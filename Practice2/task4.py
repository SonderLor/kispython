def distance(y: list, z: list) -> float:
    m = None
    for yi, zi in zip(y, z):
        if not m or abs(yi - zi) > m:
            m = abs(yi - zi)
    return m


def main() -> None:
    print(distance([1, 0.5, 1], [0.5, 2, 1]))


if __name__ == "__main__":
    main()
