import math


def main(a: int, m: int, z: float) -> float:
    total_sum = 0
    i = 1
    while i <= m:
        c = 1
        while c <= a:
            total_sum += (1 + 99 * (z ** 3 + 43 * c ** 2 + z / 88) ** 6 +
                          math.log(27 * i ** 2, 10) ** 7)
            c += 1
        i += 1
    return total_sum


if __name__ == "__main__":
    print(main(4, 3, -0.89))
