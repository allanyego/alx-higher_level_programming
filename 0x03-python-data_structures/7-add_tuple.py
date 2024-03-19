#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = b = 0
    if len(tuple_a) >= 1:
        a = tuple_a[0]
    if len(tuple_b) >= 1:
        b = tuple_b[0]

    res_a = a + b

    # reset vars
    a = b = 0
    if len(tuple_a) >= 2:
        a = tuple_a[1]
    if len(tuple_b) >= 2:
        b = tuple_b[1]

    res_b = a + b
    return res_a, res_b
