#!/usr/bin/python3
def best_score(a_dictionary):
    lgst = None
    for k, v in a_dictionary:
        if lgst is None and v > lgst:
            lgst = v
