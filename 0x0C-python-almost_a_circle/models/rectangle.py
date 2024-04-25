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
        self.__width = value
        self.validate = ("width", value)

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
        self.__height = value
        self.validate = ("height", value)

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
        self.__x = value
        self.validate = ("x", value)

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
        self.validate("y", value)
        self.__y = value

    def validate(self, name, value):
        """
        validation method.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(value))
