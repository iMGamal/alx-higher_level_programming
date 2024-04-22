#!/usr/bin/python3

"""Defining Module for class Base."""


class Base:
    """Representing the base of all other classes in out project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
