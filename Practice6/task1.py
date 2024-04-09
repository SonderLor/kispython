import copy


def smalldet(matrix):
    temp = copy.deepcopy(matrix)
    return temp[0][0] * temp[1][1] - temp[0][1] * temp[1][0]


def submatrix(matrix, i, j):
    temp = copy.deepcopy(matrix)
    return [row[:j] + row[j+1:] for row in (temp[:i] + temp[i + 1:])]


def determinant(a):
    size = len(a)
    if size == 1:
        return a[0][0]
    elif size == 2:
        return smalldet(a)
    else:
        det = 0
        for j in range(size):
            minor = submatrix(a, 0, j)
            det += ((-1) ** j) * a[0][j] * determinant(minor)
        return det


def minor(matrix, i, j):
    return determinant(submatrix(matrix, i, j))


def algebraic_addition(matrix, i, j):
    return (-1) ** (i + j) * minor(matrix, i, j)


def algmatrix(matrix):
    return [[algebraic_addition(matrix, i, j) for j in range(len(matrix))] for i in range(len(matrix[0]))]


def transpose_matrix(matrix):
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[j][i]
    return result


def invmatrix(matrix):
    b = transpose_matrix(algmatrix(matrix))
    return [[b[i][j] / determinant(matrix) for j in range(len(matrix[0]))] for i in range(len(matrix))]


def matrix_multiply(matrix1, matrix2):
    temp1 = copy.deepcopy(matrix1)
    temp2 = copy.deepcopy(matrix2)
    result = [[0 for _ in range(len(temp2[0]))] for _ in range(len(temp1))]
    for i in range(len(temp1)):
        for j in range(len(temp2[0])):
            for k in range(len(temp2)):
                result[i][j] += temp1[i][k] * temp2[k][j]
    return result


def moore_penrose(matrix):
    temp = copy.deepcopy(matrix)
    return matrix_multiply(invmatrix(matrix_multiply(transpose_matrix(temp), temp)), transpose_matrix(temp))


A = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]
print(invmatrix(A))
print(moore_penrose(A))
