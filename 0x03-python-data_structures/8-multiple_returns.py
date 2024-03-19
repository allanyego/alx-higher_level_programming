#!/usr/bin/python3
def multiple_returns(sentence):
    str_ln = len(sentence)
    first_ch = None if str_ln == 0 else sentence[0]

    return str_ln, first_ch
