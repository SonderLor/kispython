def extract_bits(num, n):
    mask = (1 << n) - 1
    return num & mask


def main(string: str):
    num = int(string, 16)
    result = list()
    shifts = (3, 3, 8, 9, 2, 5)
    for i in range(6):
        result.append(("B" + str(i + 1), extract_bits(num, shifts[i])))
        num >>= shifts[i]
    return result


if __name__ == "__main__":
    print(main("0x29476b0b"))
