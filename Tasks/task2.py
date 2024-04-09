import math


def main(z: float) -> float:
    return (
        z ** 3 + 5 * z ** 7 if z < 126 else
        74 * math.sin(85 * z ** 3) ** 7 - 41 * z if z < 181 else
        48 * z ** 3 - (98 * z ** 3 + 71 * z ** 2) ** 5 - (2 * z - z ** 3)
        if z < 229 else
        735 * z ** 2 - 4 * (math.floor(52 * z ** 2)) ** 4 if z < 279 else
        15 * math.log(75 + 30 * z ** 2 + 62 * z ** 3, 2) ** 3 -
        math.tan(z) ** 5 / 81
    )


if __name__ == "__main__":
    print(main(97))
