def fast_mul(x: int, y: int) -> int:
    result = 0
    while x != 0:
        if x % 2 != 0:
            result += y
        x >>= 1
        y <<= 1
    return result


def main():
    print(fast_mul(20, 15))


if __name__ == "__main__":
    main()
