#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    out = {}
    for k, v in a_dictionary.items():
        out[k] = v * 2
    return out
