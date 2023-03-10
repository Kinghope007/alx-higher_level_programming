#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        i = len(matrix[row])
        for column in range(i):
            if column != (i - 1):
                j = ' '
            else:
                j = ''
            print("{:d}".format(matrix[i][j]), end=j)
        print("")
