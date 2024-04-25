#!/usr/bin/python3
"""Module that contains class Rectangle, inheritance of class Base."""
from models.base import Base


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
    def width(self, value):
        """
        width setter.
        """
        self.validate = ('width', value, False)
        self.__width = value

    @property
    def height(self):
        """
        height getter.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter.
        """
        self.validate = ("height", value, False)
        self.__height = value

    @property
    def x(self):
        """
        x getter.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter.
        """
        self.validate = ("x", value)
        self.__x = value

    @property
    def y(self):
        """
        y getter.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter.
        """
        self.__y = value
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

do = Rectangle(2, 7, 9, -4)
print(do.y)
