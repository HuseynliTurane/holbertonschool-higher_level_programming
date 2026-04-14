#!/usr/bin/python3
def safe_print_integer(value):
    """Tam ədədi {:d}.format() ilə çap edir."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
