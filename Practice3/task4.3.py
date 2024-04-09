from typing import List, Optional


def dot(a: List[List[int]], b: List[List[int]]) -> Optional[List[List[int]]]:
    if len(a[0]) != len(b):
        return None
    result = list()
    for i in range(len(a)):
        r = list()
        for j in range(len(a)):
            r.append(sum(a[i][k] * b[k][j] for k in range(len(b))))
        result.append(r)
    return result


for row in dot([[1, 2], [3, 4], [5, 6]], [[1, 2, 3], [4, 5, 6]]):
    print(row)
