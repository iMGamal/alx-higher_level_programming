#!/usr/bin/python3

"""
Module for class Base.
"""


class Base:
    """
    class representing the base of our project.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        class constructor.
        """
        if cond is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
