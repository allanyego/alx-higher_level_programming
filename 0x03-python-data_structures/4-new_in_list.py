#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    l_cpy = my_list.copy()
    if idx < 0 or idx >= len(l_cpy):
        return l_cpy
    l_cpy[idx] = element
    return l_cpy
