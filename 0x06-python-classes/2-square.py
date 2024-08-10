#!/usr/bin/python3
"""There are no modules so far."""


class Square:
    """Updated first class in OOP."""
    def __init__(self, size=0):
        """Class constructor."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
