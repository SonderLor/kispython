import copy


# 1
def smalldet(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


matr = [[4, 3], [1, 1]]
print("1)", smalldet(matr))


# 2
def submatrix(a, i, j):
    b = copy.deepcopy(a)
    b.pop(i)
    for y in range(len(b)):
        b[y].pop(j)

    return b


a = [[0, 2, 1], [1, 4, 3], [2, 1, 1]]
print("2)")
print(submatrix(a, 0, 0))
print(submatrix(a, 1, 1))
print(submatrix(a, 2, 1))


# 3
def det(a):
    size = len(a)
    if size == 1:
        return a[0][0]
    elif size == 2:
        return smalldet(a)
    else:
        det_ = 0
        for j in range(size):
            minor = submatrix(a, 0, j)
            det_ += ((-1) ** j) * a[0][j] * det(minor)
        return det_


a = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]
print("3)", det(a))


# 4
def minor(a, i, j):
    return det(submatrix(a, i, j))


print("4)", minor(a, 0, 1))


# 5
def alg(a, i, j):
    return (-1)**(i + j) * minor(a, i, j)


print(alg(a, 1, 1))


# 6
def algmatrix(a):
    return [[alg(a, i, j) for j in range(len(a))] for i in range(len(a[0]))]


print("6)", algmatrix(a))


# 7
def transpose(a):
    b = [[0 for j in range(len(a))] for i in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[i][j] = a[j][i]
    return b


def inv(a):
    b = transpose(algmatrix(a))
    return [[b[i][j] / det(a) for j in range(len(a[0]))] for i in range(len(a))]


print("7)", inv(a))


# 8
def multiply(a, b):
    res = [[0 for i in range(len(b[0]))] for j in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k] * b[k][j]

    return res


def moore_penrose(a):
    return multiply(inv(multiply(transpose(a), a)), transpose(a))


print("8)", moore_penrose(a))