from typing import List, Optional


def multiply(a: List[List[int]], b: List[List[int]]) -> Optional[List[List[int]]]:
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None
    result = list()
    for i in range(len(a)):
        r = list()
        for j in range(len(a[i])):
            r.append(a[i][j] * b[i][j])
        result.append(r)
    return result


for row in multiply([[0, 2], [3, 0]], [[1, 4], [2, 0]]):
    print(row)
