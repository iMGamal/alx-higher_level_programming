#!/usr/bin/python3
"""There are no modules for now."""


class Square:
    """Updated first class of OOP."""
    def __init__(self, size=0):
        """Class constructor."""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an intger")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size
