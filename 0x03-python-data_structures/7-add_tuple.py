#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    out = []
    # choose the control
    cntrl, othr = tuple_b, tuple_a
    if len(tuple_a) > len(tuple_b):
        cntrl, othr = tuple_a, tuple_b

    for i, num_a in enumerate(cntrl):
        num_b = 0
        if i < len(othr):
            num_b = othr[i] 
        out.append(num_a + num_b)
    return tuple(out)
