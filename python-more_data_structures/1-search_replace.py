#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""
    # List comprehension istifadə edərək yeni siyahı yaradırıq.
    # Əgər element 'search' rəqəminə bərabərdirsə, 'replace' yazırıq,
    # əks halda elementin özünü saxlayırıq.
    return [replace if x == search else x for x in my_list]
