#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
ops = ["+", "-", "*", "/"]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, op, b = sys.argv[1:]

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, b = int(a), int(b)
    if op == "+":
        res = add(a, b)
    elif op == "-":
        res = sub(a, b)
    elif op == "*":
        res = mul(a, b)
    elif op == "/":
        res = div(a, b)

    print("{} {} {} = {}".format(a, op, b, res))
