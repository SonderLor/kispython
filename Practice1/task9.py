from typing import List


def get_primary_nums(x: int) -> List[int]:
    primary_nums = list()
    while x > 1:
        for d in range(2, x + 1):
            if x % d == 0:
                x //= d
                primary_nums.append(d)
                break
    return primary_nums


def fast_mul_gen(y: int) -> str:
    result = ""
    for num in get_primary_nums(y):
        result += "x = "
        for _ in range(num - 1):
            result += "x + "
        result += "x\n"
    return result


def main():
    print(fast_mul_gen(16))


if __name__ == "__main__":
    main()
