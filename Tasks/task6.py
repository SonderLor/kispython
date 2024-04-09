from typing import List

data = {
    1983: {
        'CSV': {
            'X10': {
                1965: 0,
                2020: 1
            },
            'ELM': 2
        },
        'AGDA': {
            1965: 3,
            2020: {
                'JSON5': 4,
                'JAVA': 5,
                'HTTP': 6
            }
        }
    },
    1978: 7,
    2001: {
        'JSON5': 8,
        'JAVA': {
            1965: {
                'X10': 9,
                'ELM': 10
            },
            2020: 11
        },
        'HTTP': 12
    }
}


def main(x: List[int]) -> int:
    temp = data
    while isinstance(temp, dict):
        for key in x:
            if key in temp.keys():
                temp = temp[key]
                break
    return temp


if __name__ == "__main__":
    print(main([2020, 1983, 'X10', 'JSON5', 'AGDA']))
