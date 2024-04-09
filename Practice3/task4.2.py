from typing import List


def transpose(a: List[List[int]]):
    return [list(r) for r in zip(*a)]


for row in transpose([[0, 2, 1], [1, 0, 3], [0, 1, 1], [0, 0, 0]]):
    print(row)
