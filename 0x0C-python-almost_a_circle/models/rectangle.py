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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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

    def area(self):
        """
        Rectangle area calculator.
        """
        return (self.height * self.width)

    def display(self):
        """
        Method to display attributes.
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print((" " * self.x) + ('#' * self.width))

    def __str__(self):
        """
        Method that returns string representation of an object.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args):
        self.id = args[0]
        self.width = args[1]
        self.height = args[2]
        self.x = args[3]
        self.y = args[4]
        print(Rectangle.__str__(self))
