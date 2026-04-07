#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys (alphabetic order).
    Only sorts the first level.
    """
    # 1. 'sorted()' funksiyası ilə bütün açarları əlifba sırasına düzürük
    sorted_keys = sorted(a_dictionary.keys())

    # 2. Sıralanmış açarların üzərində dövr (loop) qururuq
    for key in sorted_keys:
        # 3. Hər açarı və ona uyğun dəyəri (value) çap edirik
        print("{}: {}".format(key, a_dictionary[key]))
