import math


def f(x: int) -> int:
    if x < 13:
        return x ** 5
    elif x < 87:
        return x ** 7 - 1 - math.floor(x) ** 3 / 54
    else:
        return math.ceil(x) ** 3


def main():
    print(f(14))


if __name__ == "__main__":
    main()
