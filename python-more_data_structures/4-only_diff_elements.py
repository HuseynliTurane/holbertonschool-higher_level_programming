#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.
    This is the symmetric difference of two sets.
    """
    # '^' operatoru simmetrik fərqi hesablayır
    return set_1 ^ set_2
