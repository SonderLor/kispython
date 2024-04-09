def fast_mul(x: int, y: int) -> int:
    result = 0
    while x != 0:
        if x % 2 != 0:
            result += y
        x >>= 1
        y <<= 1
    return result


def fast_pow(x: int, n: int) -> int:
    result = 1
    for _ in range(n):
        result = fast_mul(result, x)
    return result


def main():
    print(fast_pow(2, 11))


if __name__ == "__main__":
    main()
