#!/usr/bin/python3
def uppercase(str):
    out = ""
    for letter in str:
        l_ord = ord(letter)
        # convert lowercase
        if l_ord >= 97 and l_ord <= 122:
            out += chr(l_ord - 32)  # A is 32 less aout += l_ord
        # print others as is
        else:
            out += letter
    print("{}".format(out))
