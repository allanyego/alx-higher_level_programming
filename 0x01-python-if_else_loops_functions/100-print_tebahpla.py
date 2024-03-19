#!/usr/bin/python3
reversed_ords = reversed(range(ord('a'), ord('z')+1))
start = 1
for co in reversed_ords:
    if start % 2 == 0:
        print_c = chr(co - 32)
        print(print_c, end='')
    else:
        print(chr(co), end='')
    start += 1
