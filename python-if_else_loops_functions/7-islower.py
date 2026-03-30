#!/usr/bin/python3

def islower(c):
    """Kiçik hərf yoxlaması edən funksiya."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
