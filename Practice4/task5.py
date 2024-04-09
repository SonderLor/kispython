def extract_bits(num, n):
    mask = (1 << n) - 1
    return num & mask


def main(code):
    res = dict()
    code = int(code)
    shifts = [0, 3, 7, 17, 27][::-1]
    for i, r in enumerate(shifts):
        if i == 2:
            code = extract_bits(code, shifts[i])
            continue
        res[f'S{len(shifts) - i}'] = str(code >> shifts[i])
        code = extract_bits(code, shifts[i])
    bit_dict = res
    res = 0
    res += int(bit_dict['S4']) << 0
    res += int(bit_dict['S1']) << 20
    res += int(bit_dict['S5']) << 23
    res += int(bit_dict['S2']) << 33
    return hex(res)


if __name__ == "__main__":
    print(main('239948252'))
    print(main('128390864606'))
    print(main('51700518902'))
    print(main('94668019137'))
