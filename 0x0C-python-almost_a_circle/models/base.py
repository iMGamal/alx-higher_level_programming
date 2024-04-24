#!/usr/bin/python3

"""
Module for class Base.
"""


class Base:
    """
    class representing the base of my project.
    """
    def __init__(self, id=None):
        """
        class constructor.
        """
        __nb_objects = 0
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
