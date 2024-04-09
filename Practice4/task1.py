from typing import Dict


def main(dictionary: Dict[str, str]):
    s = 0
    i = 0
    shifts = (0, 3, 9, 17, 23)
    for key, value in dictionary.items():
        s |= int(value) << shifts[i]
        i += 1
    return hex(s)


if __name__ == "__main__":
    print(main({'Z1': '3', 'z2': '2', 'Z3': '11', 'Z5': '32', 'Z6': '525'}))
