from functools import reduce


def main(n: int) -> float:
    def recursion_func(acc, _):
        return acc ** 3 + (9 * acc ** 3) ** 2 + acc
    return reduce(recursion_func, range(n), -0.45)


if __name__ == "__main__":
    print(main(1))
