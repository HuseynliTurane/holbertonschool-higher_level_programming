#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).
    Returns the sum of unique elements.
    """
    # 1. 'set(my_list)' ilə təkrarlanan elementləri silirik
    # 2. 'sum()' funksiyası ilə həmin unikal rəqəmləri toplayırıq
    return sum(set(my_list))
