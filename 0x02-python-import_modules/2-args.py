#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg_len = len(sys.argv) - 1
    print("{} argument{}".format(arg_len, "" if arg_len == 1 else "s"), end='')
    print("{}".format("." if arg_len == 0 else ":"))
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        print("{}: {}".format(i, arg))
