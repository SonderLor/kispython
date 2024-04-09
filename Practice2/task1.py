def f(n: int, m: int, a: int) -> float:
    result = 1
    for c in range(1, a + 1):
        p = 1
        for j in range(1, m + 1):
            s = 0
            for i in range(1, n + 1):
                s += (28 * c ** 2) ** 6 / 5 + 16 * (j ** 3 / 44 + i ** 2) ** 5
            p *= s
        result *= p
    return result


def main() -> None:
    print(f(4, 2, 8))


if __name__ == "__main__":
    main()
