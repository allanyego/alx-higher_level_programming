#!/usr/bin/python3
for el in range(ord('a'), ord('z')+1):
    if chr(el) == 'e' or chr(el) == 'q':
        continue
    print("{}".format(chr(el)), end='')
