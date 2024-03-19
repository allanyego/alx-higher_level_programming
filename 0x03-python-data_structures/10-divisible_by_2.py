#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    out = []
    for num in my_list:
        out.append(True if num % 2 == 0 else False)
    return out
