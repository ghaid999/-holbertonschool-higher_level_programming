#!/usr/bin/python3
"""Module defines MyList"""


class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        print(sorted(self))
