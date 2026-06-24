#!/usr/bin/python3
"""Module that defines Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return square area"""
        return self.__size * self.__size

    def __str__(self):
        """Return square description"""
        return f"[Square] {self.__size}/{self.__size}"
