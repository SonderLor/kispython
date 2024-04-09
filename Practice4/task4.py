def extract_bits(num, n):
    mask = (1 << n) - 1
    return num & mask


def main(string: str):
    num = int(string, 16)
    result = list()
    i = 0
    shifts = (6, 6, 7, 2, 3)
    for _ in range(5):
        result.append(("N" + str(i + 1), str(extract_bits(num, shifts[i]))))
        num >>= shifts[i]
        i += 1
    return result


if __name__ == "__main__":
    print(main("0xb9a562"))
