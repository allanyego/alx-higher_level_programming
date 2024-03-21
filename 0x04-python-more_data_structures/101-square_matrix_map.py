#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squared = map(lambda row:
                  list(map(lambda col: col ** 2, row)),
                  matrix)
    return list(squared)
