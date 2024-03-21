#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    
    averaged = 0
    total = 0
    for a, b in my_list:
        averaged += a * b
        total += b

    return averaged / total
