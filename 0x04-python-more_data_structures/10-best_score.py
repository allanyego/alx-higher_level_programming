#!/usr/bin/python3
def best_score(a_dictionary):
    lgst_k = None
    lgst = None
    if a_dictionary is not None:
        for k, v in a_dictionary.items():
            if lgst is None or v > lgst:
                lgst_k, lgst = k, v
    return lgst_k
