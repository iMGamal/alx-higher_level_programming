#!/usr/bin/python3
"""
Module containing class Rectangle, inheritance of class Base.
"""
from base import Base


class Rectangle(Base):
    """
    class representing Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """
        Width getter.
        """
        return self.__width

    @width.setter
    def width(self, a):
        """
        width setter.
        """
        self.__width = a

    @property
    def height(self):
        """
        height getter.
        """
        return self.__height

    @height.setter
    def height(self, b):
        """
        height setter.
        """
        self.__height = b

    @property
    def x(self):
        """
        x getter.
        """
        return self.__x

    @x.setter
    def x(self, c):
        """
        x setter.
        """
        self.__x = c

    @property
    def y(self):
        """
        y getter.
        """
        return self.__y

    @y.setter
    def y(self, d):
        """
        y setter.
        """
        self.__y = d
