#!/usr/bin/python3
def best_score(a_dictionary):
    lgst = None
    if a_dictionary is None:
        for k, v in a_dictionary.items():
            if lgst is None or v > lgst:
                lgst = k
    return lgst
