#!/usr/bin/python3

"""create a function for pascal's triangle"""


def pascal_triangle(n):
    """function returns a list of lists of integers for Pascal’s triangle"""
    triangle = []
    if n <= 0:
        triangle
    else:
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
    return triangle
