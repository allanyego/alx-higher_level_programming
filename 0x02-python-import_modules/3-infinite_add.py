#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        total += int(arg)
    print("{}".format(total))
