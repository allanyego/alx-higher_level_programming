#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):  # prioritize smaller combinations
        print("{}{}".format(i, j), end=', ' if i != 8 || j != 9 else '\n')