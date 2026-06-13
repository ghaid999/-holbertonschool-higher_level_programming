#!/usr/bin/python3
"""Defines a function that adds two integers.

add_integer validates that both arguments are integers
or floats, casts any float to an integer, then returns
the integer sum of the two values.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Floats are cast to int; non-numbers raise TypeError.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
