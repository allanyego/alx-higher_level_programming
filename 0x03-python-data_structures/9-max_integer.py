#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = None
    for num in my_list:
        if max_num is None:
            max_num = num
        elif num > max_num:
            max_num = num

    return max_num
