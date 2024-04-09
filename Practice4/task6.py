def extract_bits(num, n):
    mask = (1 << n) - 1
    return num & mask


def main(code):
    res = dict()
    code = int(code)
    shifts = [0, 7, 10, 16][::-1]
    for i, r in enumerate(shifts):
        res[f'C{len(shifts) - i}'] = str(code >> shifts[i])
        code = extract_bits(code, shifts[i])
    bit_dict = res
    res = 0
    res += int(bit_dict['C1']) << 0
    res += int(bit_dict['C3']) << 7
    res += int(bit_dict['C4']) << 13
    res += int(bit_dict['C2']) << 17
    return str(res)


if __name__ == "__main__":
    print(main('743096'))
