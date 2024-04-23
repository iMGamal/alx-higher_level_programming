#!/usr/bin/python3
"""Module for class Rectangle and inheritance of class Base."""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    def update(self, *args):
        """Method for passing arguments"""
        self.id = args[0]
        self.width = args[1]
        self.height = args[2]
        self.x = args[3]
        self.y = args[4]
