#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    - If key exists, value is replaced.
    - If key doesn't exist, it is created.
    """
    # Python-da bu sintaksis hər iki halı (yeniləmə və əlavə etmə) əhatə edir
    a_dictionary[key] = value
    return a_dictionary
