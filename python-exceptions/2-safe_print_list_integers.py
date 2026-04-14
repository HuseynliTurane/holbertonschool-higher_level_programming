#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Siyahıdakı ilk x element arasından yalnız tam ədədləri çap edir."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Əgər element integer deyilsə, heç nə etmirik (skip)
            continue
    print("")  # Sonda yeni sətir
    return count
