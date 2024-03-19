#!/usr/bin/python3
def uppercase(str):
    out = ""
    for l in str:
        co = ord(l)
        print(l, co, sep=' - ')
        # add uppercased as is
        if co >= 65 and co <= 90:
            print(f"{l} is upper!")
            out += l
        elif co == 32:  # whitespace
            out += l
        else:
            out += chr(ord(l) - 32)  # A is 32 less a
    return out
