#!/usr/bin/python3
"""Define a rectangle class"""
from models.base import Base
import sys


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle

        Args:
            width  (int): width of the rectangle
            height (int): height of the rectangle
            x      (int): x coordinater of the rectangle
            y      (int): y coordinater of the rectangle
            id     (int): id of the rectangle

        Raises:
            TypeError: If either of width or height is not an int
            ValueError: If either of width or height <= 0
            TypeError: If either of x or y is not an int
            ValueError: If either of x or y < 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Get the x coordinater of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinator of the rectangle"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Get the y coordinater of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinater of the rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle with "#" character"""
        numy = self.__y
        for x in range(self.__height + self.__y):
            if numy > 0:
                numy -= 1
                sys.stdout.write("")
                print()
            else:
                numx = self.__x
                for y in range(self.__width + self.__x):
                    if numx > 0:
                        numx -= 1
                        sys.stdout.write(" ")
                    else:
                        sys.stdout.write("#")
                print()

    def __str__(self):
        """Return print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Update the Rectangle

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            num = 0
            for arg in args:
                if num == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif num == 1:
                    self.width = arg
                elif num == 2:
                    self.height = arg
                elif num == 3:
                    self.x = arg
                elif num == 4:
                    self.y = arg
                num += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {
                    'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y
                }
