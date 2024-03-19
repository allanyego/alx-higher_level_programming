#!/usr/bin/python3
def uppercase(str):
    out = ""
    for l in str:
        co = ord(l)
        # convert lowercase
        if co >= 97 and co <= 122:
            out += chr(co - 32)  # A is 32 less aout += l
        # print others as is
        else:
            out += l
    print("{}".format(out))
