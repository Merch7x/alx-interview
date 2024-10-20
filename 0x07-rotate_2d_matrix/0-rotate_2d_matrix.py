#!/usr/bin/python3
"""Rotate a 2d matrix"""


def rotate_2d_matrix(matrix):
    matrix.reverse()

    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
