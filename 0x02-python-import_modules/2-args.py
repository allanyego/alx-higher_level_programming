#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_len = len(sys.argv)
    print("{} argument{}:".format(arg_len, "s" if arg_len > 1 else ""))
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        print("{}: {}".format(i, arg))
