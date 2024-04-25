#!/usr/bin/python3
from base import Base
"""
Module for class Base that is inherited by class Rectangle.
"""


class Rectangle(Base):
    """
    class representing Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, a):
        self.__width = a

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, b):
        self.__height = b

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, c):
        self.__x = c

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, d):
        self.__y = d
