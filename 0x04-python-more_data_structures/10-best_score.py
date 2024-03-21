#!/usr/bin/python3
def best_score(a_dictionary):
    lgst = None
    if a_dictionary is not None:
        for k, v in a_dictionary:
            if lgst is None or v > lgst:
                lgst = k
    return lgst
