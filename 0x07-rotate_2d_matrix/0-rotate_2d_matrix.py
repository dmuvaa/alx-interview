#!/usr/bin/python3

"""Create a Function"""


def rotate_2d_matrix(matrix):
    """Function that handles rotation of the matrix"""
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
