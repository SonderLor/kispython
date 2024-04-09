def f(b: int, n: int, a: int) -> int:
    first = 0
    for j in range(1, n + 1):
        for c in range(1, b + 1):
            first += ((34 * j + 41) ** 4) - 93 * (c + 79 + c ** 3) ** 5
    second = 1
    for k in range(1, a + 1):
        second_sum = 0
        for c in range(1, b + 1):
            second_sum += 22 * (c - 8) ** 5 - k ** 4
        second *= second_sum
    return first - second


def main():
    print(f(2, 2, 6))


if __name__ == "__main__":
    main()
