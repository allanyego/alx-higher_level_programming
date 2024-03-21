#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced = map(
        lambda el: replace if el == search else el,
        my_list)
    return list(replaced)
