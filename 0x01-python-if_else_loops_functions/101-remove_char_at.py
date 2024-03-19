#!/usr/bin/python3
def remove_char_at(str, n):
    indx, out = 0, ""
    for lttr in str:
        if indx != n:
            out += lttr
        indx += 1
    return out
