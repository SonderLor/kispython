from math import sqrt as s
from math import sin as i
from math import exp as e


def main(z: float, y: float, x: float) -> float:
    a = (s((i(z) ** 4 + (y + x ** 3 + x ** 2) ** 6 / 87)
           / (77 * (88 * z + y ** 2 + x ** 3) ** 7)))
    b = ((z ** 2 / 48 - x - y ** 3 / 77) ** 4 /
         (31 * e(18 + x ** 2 + 9 * y) ** 6 - 83 * (z ** 3 - y) ** 5))
    return a + b


if __name__ == "__main__":
    print(main(0.6, 0.41, -0.5))
