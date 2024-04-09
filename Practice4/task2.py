from typing import Tuple


def main(nums: Tuple[int]):
    s = 0
    i = 0
    shifts = (0, 9, 18, 19, 23, 24)
    for num in nums:
        s += num << shifts[i]
        i += 1
    return s


if __name__ == "__main__":
    print(main((396, 444, 0, 14, 0, 33)))
