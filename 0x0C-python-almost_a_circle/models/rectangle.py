#!/usr/bin/python3
"""Module for class rectangle."""
from base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """height of rectangrl"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def validate(self, name, value):
        """Method for validating value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif name < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Method to calculate rectangle area"""
        return (self.width * self.height)

    def display(self):
        """Method to display rectangle"""
        string = (self.width * '#' + '\n') * self.height
        return(string)
    def __str__(self, width, height, x, y, id=None):
        s = '[Rectangle]' + ' ' + '(' + str(self.id) + ')' + ' ' + str(self.x) + '/' + str(self.y) + ' ' + '-' + ' ' + str(self.width) + '/' + str(self.height)
        return (s)
