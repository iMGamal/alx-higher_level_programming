#!/usr/bin/python3
"""There are no modules for now."""


class Square:
    """Updated first class in OOP."""
    def __init__(self, size=0):
        """Class constructor."""
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints to stdout the square with #"""
        if self.size == 0:
            print()
        else:
            for item in range(1, self.size + 1):
                print(self.__size * '#')
