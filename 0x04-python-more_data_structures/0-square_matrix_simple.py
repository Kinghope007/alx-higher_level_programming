#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(list(matrix)):
        new_matrix = list(map(lamda x: x**2, matrix[i]))

    return (new_matrix)
